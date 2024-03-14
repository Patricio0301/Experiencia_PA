from random import randint
def adivinar_numero():
    prediccion = input ('adivina un numero del uno al diez (en numeral) :')
    n = randint (1,10)
    if prediccion == str(n):
        print (f'Correcto! adivinaste que el número es  {n}')
        return
    print (f'No :( el número es {n}')