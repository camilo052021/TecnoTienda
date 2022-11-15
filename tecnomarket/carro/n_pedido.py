
from secrets import choice
cadena = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+¿?')
cadena = str(cadena)


def consecutivo():
    longitud = 10  # La longitud que queremos
    cadena_aleatoria = ''.join(choice(cadena) for caracter in range(longitud))
    return cadena_aleatoria

