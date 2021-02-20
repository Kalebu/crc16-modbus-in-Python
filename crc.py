
def crc16_modbus(data: str, poly: hex = 0xA001) -> str:
    '''
        CRC-16 MODBUS HASHING ALGORITHM
    '''
    crc = 0xFFFF
    for byte in data:
        crc ^= ord(byte)
        for j in reversed(range(1, 9)):
            if crc & 0x0001:
                crc = (crc >> 1) ^ poly
            else:
                crc = crc >> 1

    hv = hex(crc).upper()[2:]
    blueprint = '0000'
    return (blueprint if len(hv) == 0 else blueprint[:-len(hv)] + hv)
