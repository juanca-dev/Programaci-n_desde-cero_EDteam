#Ejercicio: adivina el número
num = 7
usuario = 0
while usuario != num:
  usuario = int(input("cual es el número? "))
  if usuario > num:   
   print("digita un número menor")
  elif usuario < num:
   print("digita un número menor")
  else:
    print("correcto")                