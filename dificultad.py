def seleccionar_un_nivel(nivel):
    minimo, maximo = 0,1_000_000_000_000
    nivel = int(input('Escoge un nivel de dificultad (del 1 al 4): '))
    numero = pedir_numero_incognita(minimo, maximo)
    if nivel == 1:
        return jugar_una_partida(numero, 0, 100)
        
        
    elif nivel == 2:
        return jugar_una_partida(numero, 0, 1000)
    elif nivel == 3:
        return jugar_una_partida(numero, 0, 1_000_000)
    else:
        return jugar_una_partida(numero, 0, 1_000_000_000_000)