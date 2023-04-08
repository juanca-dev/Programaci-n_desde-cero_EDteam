usuarioEnBD  = "neo"
claveEnBD = "123456"
saldo = 1000000 

def validaUsuario(u, c):
    if u == usuarioEnBD and c == claveEnBD:
        return True
    return False
def login():
  print("Bienvenido")  
  usuario = input("digite usuario ")
  clave = input("digite contraseña ")
  return validaUsuario(usuario, clave)  
def retirar(valor):
    if valor > saldo:
      return False, saldo  
    return True, saldo - valor
def depositar(valor):
    return True, saldo + valor 

def accion(opcion):
    if opcion == 1:
      valor = int(input("Digite el valor a depositar "))
      return depositar(valor)
  
    if opcion == 2:
       valor = int(input("Digite el valor a retirar ")) 
       return  retirar(valor)
   
    return False, saldo

def ejecutar():
    if not login():
       print("usuario o contraseña inválido")
       return
    
    print("Qué desea hacer?")
    opcion = int(input("1. Depositar o 2. Retirar "))
    
    ok, saldo = accion(opcion)
    if not ok:
      print("no se realizó la acción, saldo:", saldo)
    else:
      print("acción realizada correctamente, saldo:", saldo)
ejecutar()            
    
    