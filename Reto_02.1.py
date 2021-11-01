# Crea un programa que solicite 2 numeros e imprima los siguientes resultados
#   -Resta usando el operador -
#   -Modulo usando el operador %
# Ademas realizar el or entre un valor true y un false

var_1 = input("Dame un numero: ")
var_2 = input("Dame otro numero: ")

num_1 = int(var_1)
num_2 = int(var_2)

resta = num_1 - num_2
modulo = num_1 % num_2

var_3  = True
var_4 = False

print("Resta: ", resta)
print("Modulo: ", modulo)
print("Operador OR:", var_3 or var_4)