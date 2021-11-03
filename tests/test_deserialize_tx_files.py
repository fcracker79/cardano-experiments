import hashlib
import json
import os

import bech32
import cbor


_ADDR_PREFIXES = {
    0: ''
}


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
    print('TX hash:', hashlib.blake2b(cbor.dumps(tx_decoded), digest_size=256 // 8).hexdigest())
    print('tx_decoded', tx_decoded)
    print('mah', mah)
    assert mah is None
    print('signatures', signatures)
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
    for i, certificate in enumerate(certificates):
        _print('certificate', i)
        _print('\t', certificate)


if __name__ == '__main__':
    print('FILE tx.raw')
    _print_tx_file('tx.raw')
    print('FILE tx.signed')
    _print_tx_file('tx.signed')
