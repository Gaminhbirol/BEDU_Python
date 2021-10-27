
# Haz un programa que solicite al usuario los siguientes datos
#   -Nombre de la tarjeta
#   -Tasa de interés
#   -Deuda
#   -Pago a realizar
#   -Nuevos cargos
# El programa deberá devolver un resumen de la información y calcular el monto del próximo pago mensual.
# El programa deberá considerar que no es posible realizar un pago superior al total de la deuda del mes pasado.

nom_card = input("Inserte nombre de la tarjeta: ")
tasa_interes = input("Inserte su tasa de interes: ")
deuda = input("Inserte su deuda actual: ")
pago_realizar = input("Inserte la cantidad del pago a realizar: ")
nuevos_cargos = input("Inserte el total de los nuevos cargos: ")

Var1 = float(tasa_interes)
Var2 = float(deuda)
Var3 = float(pago_realizar)
Var4 = float(nuevos_cargos)

if Var3 > Var2:
    print ("No se puede hacer un pago mayor a la deuda actual")

interes_mensual = Var1/12
deuda_recaulculada = (Var2 - Var3)*(1+interes_mensual)
nueva_deuda = deuda_recaulculada + Var4

print("Hola {} usted cuenta con una tasa de interes de: {}%. \nActualemente tiene una deuda de: ${} y quiere realizar un pago de: ${}. \nCon los nuevos cargos que introdujo que son: ${} tiene una nueva deuda de: ${}".format(nom_card,tasa_interes, deuda, pago_realizar, nuevos_cargos, nueva_deuda))






