import urllib.request 
import json

key = 0
bus_recorrido = ''
url_base = 'https://red.cl/restservice_v2/rest/conocerecorrido?codsint='

def obtener_primera_coordenada(url_base, bus_recorrido):
    url = f'{url_base}{bus_recorrido}'
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                datos = json.load(response)  # convierte la respuesta en un json
                coordenadas = datos.get('ida', {}).get('path', [])  # obtiene el valor de la llave 'path' del json
                if coordenadas:  # valida que existan coordenadas en el json, si no es asi retorna
                    primera_coordenada = coordenadas[0]  # obtiene la primera coordenada del recorrido
                    return {'latitud': primera_coordenada[0], 'longitud': primera_coordenada[1]}
                else:
                    return 'No se encontraron coordenadas en el JSON.'
            else:
                return f'Error al realizar la petición: {response.status}'
    except Exception as e:
        return f'Error al realizar la petición: {str(e)}'
    
# menú principal del programa
while True:
    print('MENU PRINCIPAL')
    print('1. Buscar recorrido')
    print('2. Salir')
    try:  # valida que el usuario ingrese un numero
        key = int(input('Ingrese una opción: '))
    except ValueError:
        print('Ingrese un número válido')
        continue

    if key == 1:
        bus_recorrido = input('Ingrese recorrido: ')  # obtiene el recorrido ingresado por el usuario
        bus_recorrido = bus_recorrido.upper()  # convierte el recorrido a mayúsculas
        coordenadas = obtener_primera_coordenada(url_base, bus_recorrido)  # obtiene las coordenadas del recorrido
        print(coordenadas)  # imprime las coordenadas del recorrido
    elif key == 2:
        print('Saliendo...')  # mensaje de despedida
        break