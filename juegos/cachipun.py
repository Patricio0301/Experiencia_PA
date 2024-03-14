def cachipun():
  from random import choice
  a=input("Ingrese elección:  ").lower()
  while a!="piedra" and a!="papel" and a!="tijeras":
    print("Inválido, intente de nuevo")
    a=input().lower()
  b=["piedra","papel","tijeras"];print(f"RESULTADO JUGADOR:\n{a}\nRESULTADO MÁQINA:\n{choice(b)}")

