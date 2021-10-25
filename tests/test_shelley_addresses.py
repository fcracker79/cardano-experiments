import bech32


def mybech32_decode(bech: str) -> bytes:
    s = ''.join((map(lambda x: f'{x:08b}'[3:], bech32.bech32_decode(bech)[1])))
    return bytes(map(lambda b: int(b, 2), map(''.join, zip(*[iter(s)] * 8))))



_ADDRESSES = (
    ('type-00', 'addr1qx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer3n0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgse35a3x'),
    ('type-01', 'addr1z8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gten0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgs9yc0hh'),
    ('type-02', 'addr1yx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzerkr0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shs2z78ve'),
    ('type-03', 'addr1x8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gt7r0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shskhj42g'),
    ('type-04', 'addr1gx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer5pnz75xxcrzqf96k'),
    ('type-05', 'addr128phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtupnz75xxcrtw79hu'),
    ('type-06', 'addr1vx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzers66hrl8'),
    ('type-07', 'addr1w8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcyjy7wx'),
    ('type-08', 'stake1uyehkck0lajq8gr28t9uxnuvgcqrc6070x3k9r8048z8y5gh6ffgw'),
    ('type-09', 'stake178phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcccycj5'),
)

_ADDRESSES_TESTNET = (
    ('type-00', 'addr_test1qz2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer3n0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgs68faae'),
    ('type-01', 'addr_test1zrphkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gten0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgsxj90mg'),
    ('type-02', 'addr_test1yz2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzerkr0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shsf5r8qx'),
    ('type-03', 'addr_test1xrphkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gt7r0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shs4p04xh'),
    ('type-04', 'addr_test1gz2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer5pnz75xxcrdw5vky'),
    ('type-05', 'addr_test12rphkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtupnz75xxcryqrvmw'),
    ('type-06', 'addr_test1vz2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzerspjrlsz'),
    ('type-07', 'addr_test1wrphkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcl6szpr'),
    ('type-08', 'stake_test1uqehkck0lajq8gr28t9uxnuvgcqrc6070x3k9r8048z8y5gssrtvn'),
    ('type-09', 'stake_test17rphkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcljw6kf'),
)
if __name__ == '__main__':
    # Verification key
    addr = 'addr_vk1w0l2sr2zgfm26ztc6nl9xy8ghsk5sh6ldwemlpmp9xylzy4dtf7st80zhd'
    print(addr)
    addr_bytes = mybech32_decode(addr)
    print(bytes(addr_bytes).hex())
    # 0e0f1f0a10030a0208091b0a1a020b181a131f05060407081710161410171a1f0d0e191b1f011b010506041f0204150d0b091e10
    print(len(addr_bytes))
    for x in _ADDRESSES:
        address_type, address = x
        print('Address type', address_type)
        addr_bytes = mybech32_decode(address)
        print(bytes(addr_bytes).hex())
    '''
    Address type type-00
    019493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type type-01
    11c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type type-02
    219493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8ec37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type type-03
    31c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542fc37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type type-04
    419493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e8198bd431b03
    Address type type-05
    51c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f8198bd431b03
    Address type type-06
    619493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e
    Address type type-07
    71c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type type-08
    e1337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type type-09
    f1c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    '''
    for x in _ADDRESSES_TESTNET:
        address_type, address = x
        print('Address type (testnet)', address_type)
        addr_bytes = mybech32_decode(address)
        print(bytes(addr_bytes).hex())
    '''
    Address type (testnet) type-00
    009493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type (testnet) type-01
    10c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type (testnet) type-02
    209493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8ec37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type (testnet) type-03
    30c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542fc37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type (testnet) type-04
    409493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e8198bd431b03
    Address type (testnet) type-05
    50c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f8198bd431b03
    Address type (testnet) type-06
    609493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e
    Address type (testnet) type-07
    70c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    Address type (testnet) type-08
    e0337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251
    Address type (testnet) type-09
    f0c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f
    '''
