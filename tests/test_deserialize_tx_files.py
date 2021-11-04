import hashlib
import json
import os

import bech32
import cbor
import nacl
from nacl import encoding
from nacl.bindings import crypto_sign

from tests import check_assertion_enabled

_EXPECTED_TX_HASH = bytes.fromhex('e7b9a137e8c3cd3dda1c6219d990316d2bf0f21c6debbfe2ddffd9e6cd87344c')
_EXPECTED_SIG_PAYMENT = bytes.fromhex('eba10fef053f982a103db4ac77fe8d578e51453f64a22cb6e61f104c30558b4b2dad11d37c72f5f0730da03083e2fec7b4490263f02a18c7ce47181b1f158e01')
_EXPECTED_SIG_OWNER = bytes.fromhex('df9b33017abb0742c687f53e487b0a8574ecda455898bb79845e3c25fafe0d494c161b33c0239532a25a45cdf4ce2f0b0ca6e460d16bbf54008c9d6638977909')


def sign(message, signing_key, encoder=encoding.RawEncoder):
    """
    Sign a message using this key.

    :param message: [:class:`bytes`] The data to be signed.
    :param encoder: A class that is used to encode the signed message.
    :rtype: :class:`~nacl.signing.SignedMessage`
    """
    raw_signed = nacl.bindings.crypto_sign(message, signing_key)

    crypto_sign_BYTES = nacl.bindings.crypto_sign_BYTES
    signature = encoder.encode(raw_signed[:crypto_sign_BYTES])
    message = encoder.encode(raw_signed[crypto_sign_BYTES:])
    signed = encoder.encode(raw_signed)
    # print('signature', signature.hex())
    # print('message', message.hex())
    # print('signed', signed.hex())
    return signature


def _get_bytes_from_cbor_file(filename: str) -> bytes:
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', filename), 'r') as f:
        return cbor.loads(bytes.fromhex(json.load(f)['cborHex']))


def _sign(data: bytes, basename: str) -> bytes:
    skey_bytes = _get_bytes_from_cbor_file(f'{basename}.skey')
    vkey_bytes = _get_bytes_from_cbor_file(f'{basename}.vkey')
    return sign(data, skey_bytes + vkey_bytes)


def mybech32encode(d: bytes) -> str:
    # address_type = d[0] >> 4
    network = d[0] & 0xf
    hrp = 'addr' + ('' if network else '_test')
    bresult = b''
    bits = ''.join(f'{x:08b}' for x in d)
    for i in range((len(bits) - 1) // 5 + 1):
        bresult += int(bits[i * 5: i * 5 + 5], base=2).to_bytes(1, 'big')
    return bech32.bech32_encode(hrp, bresult)


def _print_tx_file(filename: str) -> None:
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', filename), 'r') as f:
        _print_tx(json.load(f)['cborHex'])


def _print(*a, **kw):
    print('\t', end='')
    print(*a, **kw)


def _print_tx(tx: str) -> None:
    tx_decoded, signatures, mah = cbor.loads(bytes.fromhex(tx))
    tx_hash = hashlib.blake2b(cbor.dumps(tx_decoded), digest_size=256 // 8).digest()
    assert _EXPECTED_TX_HASH == tx_hash
    print('TX hash:', tx_hash.hex())
    print('tx_decoded', tx_decoded)
    print('mah', mah)
    assert mah is None
    # tx_decoded = cbor2.loads(bytes.fromhex(tx))
    inputs = tx_decoded[0]
    outputs = tx_decoded[1]
    fee = tx_decoded[2]
    validity_upper_bound = tx_decoded[3]
    certificates = tx_decoded[4]
    for i, cur_input in enumerate(inputs):
        _print('input', i)
        input_tx, input_tx_idx = cur_input

        _print('\tinput tx', input_tx.hex())
        _print('\tinput tx idx', input_tx_idx)

    for i, cur_output in enumerate(outputs):
        _print('output', i)
        outpout_data_bytes, amount = cur_output
        address = mybech32encode(outpout_data_bytes)
        _print('\tamount', amount)
        _print('\taddress', address)
    _print('fee:', fee)
    _print('upper bound validity', validity_upper_bound)

    _print('Certificates')
    for i, certificate in enumerate(certificates):
        _print('\tcertificate', i)
        _print('\t', certificate)

    if signatures:
        _print(f'Signatures')
        for k, sigs in signatures.items():
            _print(f'Signature {k}')
            for sig_pair in sigs:
                pub, signature = sig_pair
                _print(f'\tpub {pub.hex()}')
                _print(f'\tsig {signature.hex()}\n')


def _print_signatures():
    payment_signature = _sign(_EXPECTED_TX_HASH, 'op_pay')
    owner_signature = _sign(_EXPECTED_TX_HASH, 'staking')
    _print('Payment signature', payment_signature.hex())
    assert _EXPECTED_SIG_PAYMENT, payment_signature
    _print('Staking signature', owner_signature.hex())
    assert _EXPECTED_SIG_OWNER, owner_signature


if __name__ == '__main__':
    check_assertion_enabled()
    print('FILE tx.raw')
    _print_tx_file('tx.raw')
    print('FILE tx.signed')
    _print_tx_file('tx.signed')
    for _ in range(100):
        print('Signatures recomputed')
        _print_signatures()
