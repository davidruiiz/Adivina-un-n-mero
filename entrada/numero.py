"""
Módulo que agrupa todas las funcionalidades
que permiten pedir entrada de números
"""


import sys


MIN = 0
MAX = 99

def pedir_numero(invitacion):
    """
    Esta función se contenta con comprobar que se obtiene un número
    """
    while True:
        # Se entra en un bucle infinito

        # Se pide un número
        print(invitacion, end=": ")
        entrada = input()

        try:
            entrada = int(entrada)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)
        else:
            # Tenemos lo que queríamos, se sale del bucle saliendo de la función
            return entrada

def pedir_numero_limite(invitacion, minimo=MIN, maximo=MAX):
    """
    Esta función utiliza la anterior y agrega una post-condición
    sobre los límites del número a introducir
    """
    while True:
        # Se entra en un bucle infinito

        # Se pide un número
        invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)
        entrada = pedir_numero(invitacion)

        if minimo <= entrada <= maximo:
            # Tenemos lo que queríamos, se sale del bucle saliendo de la función
            return entrada

