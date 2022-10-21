#CRC module
from crc import CrcCalculator, Crc8


respuesta = {}

trama = ''
#-90 90
lat = '88'
#-180 180
lng = '88'
###
#each 2 charcaters represent a hex
p_id = "0038383838383838"
#9  hex: 39, dec:57
#8 hex:38, dec:56
hora_satelite = '999'
calidad_senal = '88'
p_velocidad = '8'
p_rumbo = '8'
fecha_satelite = '8'
# p_alertas=" 11"
p_alertas = "00"
p_altura = '8'
p_estado = '00'
p_odometro = '8'
p_senal = ''
p_latitud = lat
p_longitud = lng

vl_contar = ""
vl_checksum = ""
v_client = ""

#convert each character of a string to a string of its hexadecimal representation separated by space
#888 -> 38 38 38
#AƐΠ -> 41 190 3a0
def str_to_hex(p_data: str):
    # data = 'AƐΠ'
    #ord(s: str) -> int
    #unicode_dec = ord(data)
    #hex(n: int) -> str
    # unicode_hex = hex(unicode_dec)
    p_data_hex = " ".join(f"{ord(c):02x}" for c in p_data)
    # p_data_hex = " ".join(f"{ord(c):02x}" for c in data)
    
    return p_data_hex

def convertir_checksum(data: str):
    #array of integers to bytes
    # data = bytes([56,56,56])
    #b'888'

    # data = '01 02 03 04 05'
    # data = '38 38 38'
    hexa = '38 38 38'
    hexad = []
    hexad = hexa.split(' ')
    bytes_byte = bytearray()
    vl_check = ""

    buffer = bytearray(len(hexad))
    #VB.Net
    #UBOUND maximum length of the array
    #chrW dec -> character, 65 -> 'A', 56 -> '8'
    #ASC char to decimal, 'A' -> 65, '8' -> 56
    #AscW  0 through 65535. decimal
    for index, val in enumerate(hexad):
        buffer[index] = int(val,16)
    
    data = data.replace(" ", "")

    # bytes_byte = bytearray.fromhex(data)
    bytes_byte = bytes.fromhex(data)


    #using CRC module
    crc_calculator = CrcCalculator(Crc8.CCITT)
    vl_check: int = crc_calculator.calculate_checksum(bytes_byte)
    #convert to hex and remove 0x
    vl_check = hex(vl_check)[2:]

    match len(vl_check):
        case 2:
            vl_check = "00" + vl_check
        case 3:
            vl_check = "0" + vl_check

    return vl_check


print(f"p_id: {p_id}")
match p_id.strip()[0]:
    case '0':
        trama = "24 24"
        trama += " LL LL "
        for y in range(0,13,2):
            trama += p_id[y:y+2]
            if (y < 12):
                trama += " "
        if p_alertas == '00':
            trama += ' 99 55'
        else:
            trama += ' 99 99'
            trama += " " + p_alertas.strip()
        trama += " " + str_to_hex(hora_satelite + ".000") + " 2c"
        trama += " " + str_to_hex(calidad_senal) + " 2c"
        trama += " " + str_to_hex(p_latitud) + " 2c 53 2c"
        trama += " " + str_to_hex(p_longitud) + " 2c 57 2c"
        trama += " " + str_to_hex(p_velocidad) + " 2c"
        trama += " " + str_to_hex(p_rumbo) + " 2c"
        trama += " " + str_to_hex(fecha_satelite) + " 2c 2c 2c"
        trama += " 41 2a 36 33 7c"
        trama += " 31 2e 31 7c"
        trama += " " + str_to_hex(p_altura) + " 7c"
        trama += " " + p_estado + " 7c"
        trama += " 30 30 30 33 2c 30 30 30 42 7c"
        trama += " " + str_to_hex(p_odometro) + " 7c"
        
        vl_contar_number = (len(trama) + 1 )/ 3
        #round 61.5 -> 62
        vl_contar_round = round(vl_contar_number)
        #convert vl_contar_round:int -> vl_contar:hex
        vl_contar = f"{vl_contar_round:02x}"
        trama = trama.replace("LL LL", "00 " + vl_contar)

        #checksum
        vl_checksum = convertir_checksum(trama)
        # print(f"checksum: {vl_checksum} {vl_checksum[0:2]} {vl_checksum[2:4]}")
        trama += f" {vl_checksum[0:2]} {vl_checksum[2:4]}" 
        trama += f" 0d 0a"
        # print(f"{trama}")
    case _:
        print(f"else default")

respuesta['trama'] = trama
print(f"trama: {respuesta['trama']}")