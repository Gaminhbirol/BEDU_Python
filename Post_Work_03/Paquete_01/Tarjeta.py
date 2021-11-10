def Crea_Tarjeta():
    """Esta funion es para crear una tarjeta nueva introduciendo los datos reqieridos"""

    nom_card = input("Inserte nombre de la tarjeta: ")
    """Se requiere el nombre del dueño de la tarjeta"""

    tasa_interes = float(input("Inserte su tasa de interes: "))
    """Se requiere la tasa de interes con la que cuenta actualmente"""

    deuda = float(input("Inserte su deuda actual: "))
    """Esta es la deuda que se debe de este mes"""

    pago_realizar = float(input("Inserte la cantidad del pago a realizar: "))
    """Este es el pago que se piensa hacer"""

    nuevos_cargos = float(input("Inserte el total de los nuevos cargos: "))
    """Estos son los gastos que hubo durante el mes"""

    while pago_realizar > deuda:
        """Este while sirve para detectar si el pago a realizar es mayor que la deuda si es el caso, marca un error porque no se puede hacer un pago mayor a la deuda actual"""
        print ("No se puede hacer un pago mayor a la deuda actual")
        nuevo_pago_realizar = input("Inserte un nuevo valor para el pago a realizar: ")
        pago_realizar = float(nuevo_pago_realizar)

    Info_Nueva_Tarjeta = {"Nombre":nom_card, "Tasa de interes":tasa_interes, "Deuda actual":deuda, "Pago a realizar": pago_realizar, "Cargos nuevos":nuevos_cargos}
    """aqui debe de jutnar los datos de la nueva tarjeta"""

    print("Esta es la informacion de su tarjeta: ",Info_Nueva_Tarjeta)
    """aqui se imprimen esos datos"""

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