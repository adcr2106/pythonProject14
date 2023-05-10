import random
import math

CARACTERES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í', 'Ó', 'Ú', '1',
              '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '^', '%', '#', '$', '@', ' ', ',', ';',
              '.', ':', '¿', '?', '¡', '!', '_', '(', ')', '[', ']', '{', '}', '\\', '=', '¬', 'ñ', 'Ñ', 'ü', 'Ü']
HEXADECIMALES = ['0061', '0062', '0063', '0064', '0065', '0066', '0067', '0068', '0069', '006A', '006B', '006C', '006D',
                 '006E', '006F', '0070', '0071', '0072', '0073', '0074', '0075', '0076', '0077', '0078', '0079', '007A',
                 '00E1', '00E9', '00ED', '00F3', '00FA', '0041', '0042', '0043', '0044', '0045', '0046', '0047', '0048',
                 '0049', '004A', '004B', '005C', '004D', '004E', '004F', '0050', '0051', '0052', '0053', '0054', '0055',
                 '0056', '0057', '0058', '0059', '005A', '00C1', '00C9', '00CD', '00D3', '00DA', '0031', '0032', '0033',
                 '0034', '0035', '0036', '0037', '0038', '0039', '001A', '00A2', '002B', '002C', '002D', '002E', '002F',
                 '0023', '0024', '0025', '0040', '003A', '003B', '003C', '003D', '003E', '003F', '00A1', '0021', '005F',
                 '0028', '0029', '005B', '005D', '007B', '007D', '005E', '00AC', '00F1', '00D1', '00FC', '00DC']


def generar_numero_aleatorio_longitud_14():
    num_digitos = random.randint(1, 14)
    numero_aleatorio = "".join(str(random.randint(0, 9)) for _ in range(num_digitos))
    return int(numero_aleatorio)

def generar_coprimos():
    n = len(CARACTERES)
    b = generar_numero_aleatorio_longitud_14()

    while True:
        a = generar_numero_aleatorio_longitud_14()
        if math.gcd(n, a) == 1:
            return a, b, n


def aplicar_formula_encriptacion(letra, a, b):
    if letra == "":
        return

    n = len(CARACTERES)
    indice = (a * CARACTERES.index(letra) + b) % n

    return HEXADECIMALES[indice]


def unir_mensaje_encriptado(a, b, mensaje_encriptado, texto_pc1):
    a_str = str(a)
    b_str = str(b)
    mensaje_completo = [a_str, b_str, mensaje_encriptado]
    random.shuffle(mensaje_completo)
    mensaje = "&".join(mensaje_completo)
    print(f'El mensaje se encriptó correctamente: "{mensaje}"')

    adivinar_mensaje(mensaje, texto_pc1)


def encriptar_mensaje(texto, a, b):
    mensaje_encriptado = ""
    arr = [c for c in texto]
    for i in range(len(arr)):
        letra = arr[i]
        codigo_hex = aplicar_formula_encriptacion(letra, a, b)
        mensaje_encriptado += codigo_hex

    unir_mensaje_encriptado(a, b, mensaje_encriptado, texto)


def separar_mensaje(mensaje):
    partes = mensaje.split("&")
    random.shuffle(partes)
    a = partes[random.randint(0, 2)]

    while True:
        b = partes[random.randint(0, 2)]
        if b == a:
            continue
        else:
            for i in range(2):
                if partes[i] != a and partes[i] != b:
                    mensaje_encriptado = partes[i]
                    return a, b, mensaje_encriptado


def obtener_numeros_hexadecimales(mensaje_arr):
    numeros_hexadecimales = []

    contador = 0
    for i in range(len(mensaje_arr) // 4):
        numero_hexadecimal = ""
        primer_hex = mensaje_arr[contador]
        segundo_hex = mensaje_arr[contador + 1]
        tercer_hex = mensaje_arr[contador + 2]
        cuarto_hex = mensaje_arr[contador + 3]

        numero_hexadecimal += primer_hex + segundo_hex + tercer_hex + cuarto_hex
        numeros_hexadecimales.append(numero_hexadecimal)

        contador += 4

    return obtener_indices_hexadecimales(numeros_hexadecimales)


def obtener_indices_hexadecimales(numeros_hexadecimales):
    indices_hexadecimales = []

    for i in range(len(numeros_hexadecimales)):
        indices_hexadecimales.append(HEXADECIMALES.index(numeros_hexadecimales[i]))

    return indices_hexadecimales


def obtener_indices_simbolos(a, b, indices_hexadecimales):
    indices_simbolos = []
    n = len(CARACTERES)

    try:
        a_resultado = int(a) % n
    except ValueError:
        print(f'el valor de a "{a}" no tiene un inverso.')
        print(f"PC1 GANÓ")

    try:
        b_resultado = int(b) % n
    except ValueError:
        print(f'el valor de b "{b}" no tiene un inverso.')
        print(f"PC1 GANÓ")

    for i in range(len(indices_hexadecimales)):
        indice = (int(indices_hexadecimales[i]) - b_resultado) * a_resultado % n
        indices_simbolos.append(indice)
    return indices_simbolos


def ganador_final(mensaje_pc2, mensaje_pc1):
    if mensaje_pc2 == mensaje_pc1:
        print(f'¡PC2 ganó"{mensaje_pc2}"')
    else:
        print(f'PC1 ganó"{mensaje_pc2}"')


def adivinar_mensaje(mensaje, mensaje_pc1):
    a, b, mensaje_encriptado = separar_mensaje(mensaje)

    mensaje_arr = [c for c in mensaje_encriptado]
    todos_los_indices_hexadecimales = obtener_numeros_hexadecimales(mensaje_arr)
    todos_los_indices_simbolos = obtener_indices_simbolos(a, b, todos_los_indices_hexadecimales)

    print(todos_los_indices_simbolos)

    if len(todos_los_indices_simbolos) < 1:
        return ""

    mensaje_pc2 = ""

    for i in range(len(todos_los_indices_simbolos)):
        mensaje_pc2 += CARACTERES[todos_los_indices_simbolos[i]]

    ganador_final(mensaje_pc2, mensaje_pc1)

def desencriptar():
    mensaje = input("Ingresa el mensaje hexadecimal: ")
    a = int(input("Cual es el valor de a: "))
    b = int(input('Cual es el valor de b: '))
    n = len(CARACTERES)

    if math.gcd(a, n) != 1:
        print(f'{a} y {n} NO SON PRIMOS RELATIVOS')
        return

    mensaje_arr = [c for c in mensaje]
    numeros_hexa = obtener_numeros_hexadecimales(mensaje_arr)
    simbolos_index = obtener_indices_simbolos(a, b, numeros_hexa)

    mensaje_pc2 = ""

    for i in range(len(simbolos_index)):
        mensaje_pc2 += CARACTERES[simbolos_index[i]]

    print(mensaje_pc2)

def main():
    while True:
        a, b, n = generar_coprimos()

        a_resultado = a % n
        b_resultado = b % n

        print("*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+")
        print("""Bienvenido
        -Ingresa la letra 'D' para desencriptar un mensaje 
        -Ingresa la letra 'N' para jugar normalmente """)
        opcion = input("*")

        if opcion == 'D':
            desencriptar()
        elif opcion == 'N':
            texto = input('ingrese un texto a encriptar: ')
            encriptar_mensaje(texto, a_resultado, b_resultado)
        else:
            print('Opcion no valida, Asegurese de poner su opcion en letras mayusculas')

main()
