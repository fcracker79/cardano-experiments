import pprint

import cbor

_STAKE_POOL_SIGNING_KEY = '58200640315f333b166dbac1ac0ce215b1e5f34f1b6a0d6488de68bffa13be02960c'
_STAKE_POOL_VERIFICATION_KEY = '58200ca8cf84a7174ec4a688f160843723d57fae76790b8d361b36f9a33d1418ae89'
_NODE_OPERATIONAL_CERT_ISSUE_COUNTER = '820058200ca8cf84a7174ec4a688f160843723d57fae76790b8d361b36f9a33d1418ae89'
_KES_SIGNING_KEY = '590260a0690d7f03005ecf3a36cad3eed39ce5031fb36bf964bfce155103f34898dffa80353fb18400299af87ad0185a9ab9e4f148c763ef55babf36c4842aa9e86308d612bef0f3d42617597e810c6040119adcf5404d26a5d02dde6f573dce250392dcb092691df1a69161f9a23ecf9f6ce61ed58c00eabea6b5eac5ebe789ae6904d542f3d7f3da661d59f102aa2cc2d8852407078325092a8a6526cece92c2d71b1244e49589445170be7db38128ecef247c202c50ee435c837b3e8eefde4da95802196b900adf660e701f17e31443258ccf0a35a99f0b9aafab4cc4392fcffffb09485aeee77619116ecef9b5a7dc7926ffbd5523e0f66ee19c3744b27bab67a06f88690343fa901123787e46d8dd54a1e48f84cb617fbe05079a7d89104953f49c1c9e0108c24be11b1d10a71e03b1f46fadd350fb52c92257251934b8dd30cc6130a01aa983adcb8cb94c5fe4ac5d4992d5675f7433b9396b0a7ab5dd1eea2ddb0dd3e548df3cba24720843aaf09fa2ef2a4ad40697499f39f78197a1bc7e17af2fe045cc971e08f5b984e84d71bcd86949369ee0455aa5cd7794041ae1eb9666c202b9b7bfdda5dabee5e01eef5dc7dc5a6112ae454ce90420ad0f0d7ce946fdb7a1d671fa43ae8c916fe1000c848ed91c84b11fd42c804f90c5c956630d9ff14d89d10e1c90d2dad8c9c3e6762b0deff6fbe0e4a2b355a0ee3c5a47c4014044af6511a52528840c9b2a70e88d83a56c5231ebabcb26fc0d0ca67a31cb46640818c6d2995a7b66362760aae3841bceff720ed4108e3ee1926ef9ef4926d690dcc688c6776c971ebcbf0c049a1afc7c663dcbdbb967703e54cf89a1058a3173'
_KES_VERIFICATION_KEY = '5820daabb00a1d8049cdde6acc2625c60b108347185aba26a1aa18858c18b9103b3c'
_NODE_OPERATIONAL_CERT = '82845820daabb00a1d8049cdde6acc2625c60b108347185aba26a1aa18858c18b9103b3c00005840b9bf7333b74000ade786663eec05ddb488444711de6a5fc352b594f5d37744108de060adff9904afe3afeebd0052f83ecd6b8c3f354cb8d919d9072c17393f0358200ca8cf84a7174ec4a688f160843723d57fae76790b8d361b36f9a33d1418ae89'
_VRF_SIGNING_KEY = '5840def2ffe761e03332966d14f822905fff5d598a55887d94ba4e1fd560906066e012c00c949156a1bab95142e3c9f30df6533c24649ea47426475337dd8a21268b'
_VRF_VERIFICATION_KEY = '582012c00c949156a1bab95142e3c9f30df6533c24649ea47426475337dd8a21268b'


_STAKE_POOL_SIGNING_KEY = bytes.fromhex(_STAKE_POOL_SIGNING_KEY)
_STAKE_POOL_VERIFICATION_KEY = bytes.fromhex(_STAKE_POOL_VERIFICATION_KEY)
_NODE_OPERATIONAL_CERT_ISSUE_COUNTER = bytes.fromhex(_NODE_OPERATIONAL_CERT_ISSUE_COUNTER)
_KES_SIGNING_KEY = bytes.fromhex(_KES_SIGNING_KEY)
_KES_VERIFICATION_KEY = bytes.fromhex(_KES_VERIFICATION_KEY)
_NODE_OPERATIONAL_CERT = bytes.fromhex(_NODE_OPERATIONAL_CERT)
_VRF_SIGNING_KEY = bytes.fromhex(_VRF_SIGNING_KEY)
_VRF_VERIFICATION_KEY = bytes.fromhex(_VRF_VERIFICATION_KEY)


def _bprint(*a, b: bytes) -> None:
    if len(b) > 80:
        print(*a)
        for x in range(0, (len(b) - 1) // 80 + 1):
            print(f'\t{b[x * 80: x * 80 + 80]}')
        print(f'\t({len(b)} bytes')
    else:
        print(*a, f'{b.hex()} ({len(b)} bytes)')


def _check_assertion_enabled():
    try:
        assert False
        # noinspection PyUnreachableCode
        raise ValueError('Please enable assertions')
    except AssertionError:
        return


if __name__ == '__main__':
    _check_assertion_enabled()
    _bprint('Stake pool signing key:     ', b=cbor.loads(_STAKE_POOL_SIGNING_KEY))
    stake_pool_verification_key = cbor.loads(_STAKE_POOL_VERIFICATION_KEY)
    _bprint('Stake pool verification key:', b=stake_pool_verification_key)
    node_op_issue_counter, verification_key = cbor.loads(_NODE_OPERATIONAL_CERT_ISSUE_COUNTER)
    print('Node operational cert issue counter:', node_op_issue_counter)
    assert verification_key == stake_pool_verification_key
    _bprint('KES signing key:', b=cbor.loads(_KES_SIGNING_KEY))
    kes_verification_key = cbor.loads(_KES_VERIFICATION_KEY)
    _bprint('KES verification key:', b=kes_verification_key)

    node_operational_cert = cbor.loads(_NODE_OPERATIONAL_CERT)
    node_operational_cert_kes_stuff, verification_key = node_operational_cert
    op_cert_kes_verification_key, n1, n2, unknown_bytes = node_operational_cert_kes_stuff
    assert verification_key == stake_pool_verification_key
    assert op_cert_kes_verification_key == kes_verification_key
    print('Node operational cert:', pprint.pformat(cbor.loads(_NODE_OPERATIONAL_CERT), width=120))
    _bprint('VRF signing key:', b=cbor.loads(_VRF_SIGNING_KEY))
    _bprint('VRF verification key:', b=cbor.loads(_VRF_VERIFICATION_KEY))
