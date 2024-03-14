from random import randint
def juego_del_dado():
  c=0;a=0;b=0
  while a<30 and b<30:
    if c==0:
      c+=1
      n=input("Oprima Enter")
      a+=randint(1,6)
    elif c==1:
      c-=1
      b+=randint(1,6)
    print("");print(f"JUGADOR: {a}\nMÁQUINA: {b}")

  print("")
  if a>=30:
    print("¡¡¡GANASTEEE!!!")
  else:
    print("Más suerte la próxima...")

juego_del_dado()
