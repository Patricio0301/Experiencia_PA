def cachipun():
  from random import choice
  a=input("Ingrese elección:  ").lower()
  while a!="piedra" and a!="papel" and a!="tijeras":
    print("Inválido, intente de nuevo")
    a=input().lower()
  b = choice(["piedra","papel","tijeras"])
  print(f"RESULTADO JUGADOR:\n{a}\nRESULTADO MÁQINA:\n{b}")
  if a == b:
    print ('Empate')
  elif (a == 'piedra' and b == 'tijeras') or (a == 'papel' and b == 'piedra') or (a == 'tijeras' and b == 'papel'):
    print ('Ganaste!')
  else:
    print ('Perdiste :(')

  

