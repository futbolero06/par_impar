# programa para saber si un numero es par o impar
print("-----------------------------")
print("--------digite su numero-----")
print("-----------------------------")

# input
x= int(input("digite el numero: "))

# processing
r=x%2
if r==0:
    msj="par"
else:
    msj="impar"

# output
print("-----------------------------")
print("-------resulatados-----------")
print("-----------------------------")
print("el numero es: " + str(r) + " es: " + msj)

