respuesta = {}

trama = ''
#-90 90
lat = '10'
#-180 180
lng = '20'

p_id = "001122334455667788"
hora_satelite = 'ABC'
calidad_senal = ''
p_velocidad = ''
p_rumbo = ''
fecha_satelite = ''
# p_alertas=" 11"
p_alertas = "00"
p_altura = ''
p_estado = ''
p_odometro = ''
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
    s_val = ""
    s_hex = ""
    # data = p_data
    # print(f"{data}")
    # data = data[0:3]
    #ord: str -> int
    #unicode_dec = ord(data)
    # unicode_hex = hex(unicode_dec)
    #hex: int -> str
    # unicode_hex = hex(5)
    # print(f"{data} {unicode_dec} {unicode_hex}")    
    p_data_hex = " ".join(f"{ord(c):02x}" for c in p_data)
    print(f"{p_data_hex}&")

    return p_data_hex

def convertir_checksum(trama):

    return '10'



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
        print(f"{vl_checksum}")
    case _:
        print(f"else default")




respuesta['trama'] = trama
print(f"{respuesta['trama']}")