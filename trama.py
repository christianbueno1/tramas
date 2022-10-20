respuesta = {}

trama = ''
#-90 90
lat = '88'
#-180 180
lng = '88'
###
p_id = "001122334455667788"
#9  hex: 39, dec:57
hora_satelite = '999'
# hora_satelite = 'ABC'
# 8 hex:38, dec:56
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

#  p_id.strip()[0]
#1 - 13
#0 - 12

#convert each character to hexadecimal
def str_to_hex(p_data):
    # s_val = ""
    # s_hex = ""
    # data = p_data
    #can return hex of DBCS like 190
    #hex 41 190 3a0
    # data = ''
    # data = 'AƐΠ'
    # print(f"{data}")
    # data = data[0:3]
    #ord: str -> int
    #unicode_dec = ord(data)
    # unicode_hex = hex(unicode_dec)
    #hex: int -> str
    # unicode_hex = hex(5)
    # print(f"{data} {unicode_dec} {unicode_hex}")    
    p_data_hex = " ".join(f"{ord(c):02x}" for c in p_data)
    # p_data_hex = " ".join(f"{ord(c):02x}" for c in data)
    
    # print(f"p_data_hex:&{p_data_hex}&")

    return p_data_hex

def convertir_checksum(data: str):
    # hexa = data
    #65 A, 66 B, 67 C
    #hex:2c dec:44, 'comma'
    # hexa = '2c 2c 2c'
    # 8 hex:38, dec:56
    hexa = '38 38 38'
    hexad = []
    hexad = hexa.split(' ')
    vl_check = ""

    #byte 0-255
    #VB.net prefix "&h" exadecimal literall
    #buffer(I) 0-255
    buffer = bytearray(len(hexad))
    # print(f"hexad: {len(hexad)} {len(buffer)}")
    #UBOUND maximum length of the array
    # 8 hex:38, dec:56
    #chrW dec -> character, 65 -> 'A', 56 -> '8'
    #ASC char to decimal, 'A' -> 65, '8' -> 56
    #AscW  0 through 65535. decimal
    for index, val in enumerate(hexad):
        buffer[index] = int(val,16)
        print(f"{buffer[index]}")
    print(f"buffer {buffer} {type(buffer[0])}")

    # vl_check = hexad
    return vl_check



match p_id.strip()[0]:
    case '0':
        print(f"case 0")
        trama = "24 24"
        trama += " LL LL "
        for y in range(0,13,2):
            trama += p_id[y:y+2]
            if (y < 12):
                trama += " "
            print(f"{y}: {trama}")
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
        # vl_contar_round_hex = hex(vl_contar_round)
        # print(f"81: {vl_contar_number}\n{vl_contar_round}\n{vl_contar_round:02x}\n{vl_contar_round_hex}")
        vl_contar = f"{vl_contar_round:02x}"
        # print(f"86: {vl_contar}")
        print(f"{trama}")
        trama = trama.replace("LL LL", "00 " + vl_contar)
        vl_checksum = convertir_checksum(trama)
        print(f"checksum: {vl_checksum}")
    case _:
        print(f"else default")




respuesta['trama'] = trama
print(f"trama: {respuesta['trama']}")