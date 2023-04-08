
# # numero mayor 
# a = 80
# b = 16
# c = 14
# d = 5

# mayor = 0

# if a > b:
#     if a > c:
#         mayor = a
# elif b > c:
#     mayor = b
# else:
#     mayor = c
# print(mayor)
             
#  # numero menor
  
# a = 80
# b = 16
# c = 14

# menor = 0

# if a < b:
#     if a < c:
#         menor = a
# elif b < c:
#     menor = b
# else:
#     menor = c
# print(menor) 

# # # #
# Sacar el número mayor.
def mayor(x, y):
    if x > y:
        return x
    return y 

a = 100000
b = 16
c = 5
d = 50

maximo = mayor(mayor(a,b), mayor(c,d))
print(maximo)


# Sacar el número menor.

def menor(x, y):
    if x < y:
        return x
    return y 

a = 100000
b = 16
c = 5

minimo = menor(a, b)
minimo = menor(minimo, c)
print (minimo)