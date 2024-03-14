from random import randint
def adivinar_par_o_impar():
    prediccion = input ('Es el número par o impar?:')
    n = randint (0,100000)
    if (n%2 == 0 and prediccion.upper() == 'PAR') or (n%2 != 0 and prediccion.upper() == 'IMPAR'):
        print (f'Correcto!, el número es {prediccion}')
        return n
    print ('No :( te equivocaste')
    return n