# Crea la función crea_tarjeta, esta debe contener la captura de datos de una tarjeta y devolver un diccionario con la información. En caso de que se indique un monto mayor de pago del posible, debe indicar el error con un mensaje y solicitar la información nuevamente.

# Crea la función captura_nueva_deuda, la cual debe recibir un diccionario con los datos de una tarjeta y hacer los cálculos vistos en el postwork 1, agregando la nueva deuda como un cargo adicional del diccionario.

# Crea la función generar_reporte, esta debe escribir

# Crea una función que itere sobre una lista de tarjetas e imprima los reportes de todas.

# Crea la función pago_recurrente, la cual proyectará una serie de pagos del mismo monto en una tarjeta, para una deuda que no tendrá nuevos cargos. Hasta convertir el valor de la deuda en 0. Para cada mes proyectado se debe imprimir el reporte correspondiente.

# Haz llamadas y prueba las funciones que has creado

def Crea_Tarjeta():

    nom_card = input("Inserte nombre de la tarjeta: ")
    tasa_interes = float(input("Inserte su tasa de interes: "))
    deuda = float(input("Inserte su deuda actual: "))
    pago_realizar = float(input("Inserte la cantidad del pago a realizar: "))
    nuevos_cargos = float(input("Inserte el total de los nuevos cargos: "))

    while pago_realizar > deuda:
        print ("No se puede hacer un pago mayor a la deuda actual")
        nuevo_pago_realizar = input("Inserte un nuevo valor para el pago a realizar: ")
        pago_realizar = float(nuevo_pago_realizar)

    Info_Nueva_Tarjeta = {"Nombre":nom_card, "Tasa de interes":tasa_interes, "Deuda actual":deuda, "Pago a realizar": pago_realizar, "Cargos nuevos":nuevos_cargos}

    print("Esta es la informacion de su tarjeta: ",Info_Nueva_Tarjeta)
def Captura_Nueva_Deuda():
    nom_card = input("Inserte nombre de la tarjeta: ")
    tasa_interes = float(input("Inserte su tasa de interes: "))
    deuda = float(input("Inserte su deuda actual: "))
    pago_realizar = float(input("Inserte la cantidad del pago a realizar: "))
    nuevos_cargos = float(input("Inserte el total de los nuevos cargos: "))

    Info_Tarjeta = {"Nombre":nom_card, "Tasa de interes":tasa_interes, "Deuda actual":deuda, "Pago a realizar": pago_realizar, "Cargos nuevos":nuevos_cargos}

    print("Esta es la informacion de su tarjeta: ",Info_Tarjeta)

    while pago_realizar > deuda:
        print ("No se puede hacer un pago mayor a la deuda actual")
        nuevo_pago_realizar = input("Inserte un nuevo valor para el pago a realizar: ")
        pago_realizar = float(nuevo_pago_realizar)
        
    interes_mensual = tasa_interes/12
    deuda_recaulculada = (deuda - pago_realizar)*(1+interes_mensual)
    nueva_deuda = deuda_recaulculada + nuevos_cargos

    Info_Tarjeta["Nueva deuda"] = nueva_deuda
    print("Esta es la nueva informacion de su tarjeta", Info_Tarjeta)

#Crea_Tarjeta()
Captura_Nueva_Deuda()






