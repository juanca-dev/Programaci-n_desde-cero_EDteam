
# numero mayor 
a = 80
b = 16
c = 14

mayor = 0

if a > b:
    if a > c:
        mayor = a
elif b > c:
    mayor = b
else:
    mayor = c
print(mayor)
             
 # numero menor
  
a = 80
b = 16
c = 14

menor = 0

if a < b:
    if a < c:
        menor = a
elif b < c:
    menor = b
else:
    menor = c
print(menor) 

#
def mayor(x, y):
    if x > y:
         return x
     return y