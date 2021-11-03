import bitcoin
import cbor


# Beware: addresses here are Byron ones.
tx = '839f8200d81858268258204806bbdfa6bbbfea0443ab6c301f6d7d04442f0a146877f654c08da092af3dd8193c508200d818582682582060fc8fbdd6ff6c3b455d8a5b9f86d33f4137c45ece43abb86e04671254e12c08197a8bff9f8282d818585583581ce6e37d78f4326709af13851862e075bce800d06401ad5c370d4d48e8a20058208200581c23f1de5619369c763e19835e0cb62c255c3fca80aa13057a1760e804014f4e4ced4aa010522e84b8e70a121894001ae41ef3231b0075fae341e487158282d818585f83581cfd9104b3efb4c7425d697eeb3efc723ef4ff469e7f37f41a5aff78a9a20058208200581c53345e24a7a30ec701611c7e9d0593c41d6ea335b2eb195c9a0d2238015818578b485adc9d142b1e692de1fd5929acfc5a31332938f192011ad0fcdc751b0003d8257c6b4db7ffa0'
if __name__ == '__main__':
    tx_decoded = cbor.loads(bytes.fromhex(tx))
    # tx_decoded = cbor2.loads(bytes.fromhex(tx))
    inputs, outputs, attributes = tx_decoded
    for i, cur_input in enumerate(inputs):
        print('input', i)
        in_type, input_data_bytes = cur_input
        input_tx, input_tx_idx = cbor.loads(input_data_bytes.value)

        print('\tinput type', in_type)
        print('\tinput tx', input_tx.hex())
        print('\tinput tx idx', input_tx_idx)

    for i, cur_output in enumerate(outputs):
        print('output', i)
        outpout_data_bytes_with_checksum, amount = cur_output
        output_data_bytes, checksum = outpout_data_bytes_with_checksum
        output_address_root, output_address_attributes, output_address_type = cbor.loads(output_data_bytes.value)
        output_stack_distribution = output_address_attributes[0].hex()
        output_pk_derivation_path = output_address_attributes[1].hex()
        print('\tamount', amount)
        print('\taddress root', output_address_root.hex(), bitcoin.changebase(cbor.dumps(outpout_data_bytes_with_checksum), 256, 58))
        print('\taddress type', output_address_type)
        print('\tchecksum', checksum)
        print('\toutput stack distribution', output_stack_distribution)
        print('\toutput pk derivation path', output_pk_derivation_path)
    print('attributes:', attributes)
