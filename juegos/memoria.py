import random
def memoria():
  x=""
  for i in range(10):
    x+=str(random.randint(1,11))+", "
  x=x[:-2]
  print(x)
  a=input("Ingrese la secuencia de números separados por coma y espacio: ")
  if x==a:
    print("ACERTASTEE")
  else:
    print("NO ACERTASTE :(")
