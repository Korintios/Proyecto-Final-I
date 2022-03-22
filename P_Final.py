from os import system
system("cls")

CAC = 0 #Cantidad de Fotocopias Carta.
CAO = 0 #Cantidad de Fotocopias Oficio.
CAEO = 0 #Cantidad de Fotocopias Extra Oficio.

TC = 0 #Cantidad de Fotocopias Carta Vendidas por Concepto.
TO = 0 #Cantidad de Fotocopias Oficio Vendidas por Concepto.
TEO = 0 #Cantidad de Fotocopias Extra Oficio Vendidas por Concepto.

CCH = 0 #Cantidad de Fotocopias Carta de Hombres.
COH = 0 #Cantidad de Fotocopias Oficio de Hombres.
CEOH = 0 #Cantidad de Fotocopias Extra Oficio de Hombres.

CCM = 0 #Cantidad de Fotocopias Carta de Mujeres.
COM = 0 #Cantidad de Fotocopias Oficio de Mujeres.
CEOM = 0 #Cantidad de Fotocopias Extra Oficio de Mujeres.

FOM = "" #Nombre de la Fotocopia mas vendida.

HTC = 0 #Hombres que compraron fotocopias carta.

MEO = 0 #Mujeres entre 25 y 35 años que compraron Extra Oficio.

CLM = 0 #Clientes mayores de 60 años.

CCL = 0 #Fotocopias Carta vendidas los lunes.
COL = 0 #Fotocopias Oficio vendidas los lunes.
CEOL = 0 #Fotocopias ExtraOficio vendidas los lunes.

def clientes():
    C = True
    N = True
    S = True
    E = True
    F = True
    FE = True

    global CAC #Cantidad de Fotocopias Carta Globales.
    global CAO #Cantidad de Fotocopias Oficio Globales.
    global CAEO #Cantidad de Fotocopias Extra Oficio Globales.

    global TC #Cantidad de Fotocopias Carta Vendidas por Concepto.
    global TO #Cantidad de Fotocopias Oficio Vendidas por Concepto.
    global TEO #Cantidad de Fotocopias Extra Oficio Vendidas por Concepto.

    global CCH #Cantidad de Fotocopias Carta de Hombres.
    global COH #Cantidad de Fotocopias Oficio de Hombres.
    global CEOH #Cantidad de Fotocopias Extra Oficio de Hombres.

    global CCM #Cantidad de Fotocopias Carta de Mujeres.
    global COM #Cantidad de Fotocopias Oficio de Mujeres.
    global CEOM #Cantidad de Fotocopias Extra Oficio de Mujeres.

    global FOM #Nombre de la Fotocopia mas vendida.
    
    global HTC #Hombre que compraron fotocopias carta.

    global MEO #Mujeres entre 25 y 35 anos que compraron Extra Oficio.

    global CLM #Clientes mayores de 60 años.

    global CCL #Fotocopias Carta vendidas los lunes.
    global COL #Fotocopias Oficio vendidas los lunes.
    global CEOL #Fotocopias Extra Oficio vendidas los lunes.

    cliente = 1
    while (True):
        archivo = open('Registros.txt','a')
        while FE:
            try:
                print("- Lunes")
                print("- Martes")
                print("- Miercoles")
                print("- Jueves")
                print("- Viernes")
                print("- Sabado")
                print("- Domingo")
                fecha = str(input(f"Ingresar fecha del cliente {cliente}: "))
                break
            except ValueError:
                print("Error, ingresa la fecha nuevamente.")
        while C:
            try:
                codigo = int(input(f"Ingresar codigo del cliente {cliente}: "))
                break
            except ValueError:
                print("Error, ingresa el codigo nuevamente.")
        while N:
            try:
                nombre = str(input(f"Ingresar nombre del cliente {cliente}: "))
                break
            except ValueError:
                print("Error, ingresa el nombre nuevamente.")
        while S:
            try:
                print(f"Ingresar sexo del cliente {cliente}: ")
                print("M - Masculino")
                print("F - Femenino")
                sexo = str(input())
                if sexo == "M":
                    sexo = "Hombre"

                elif sexo == "F":
                    sexo = "Mujer"
                else:
                    print("Error, Ingresa el sexo nuevamente.")
                break
            except ValueError:
                print("Error, ingresa el sexo nuevamente.")
        while E:
            try:
                edad = int(input(f"Ingresar edad del cliente {cliente}: "))
                break
            except ValueError:
                print("Error, ingresa la edad nuevamente.")
        while F:
            print("- Carta")
            print("- Oficio")
            print("- Extraoficio")
            FO = str(input("Ingresa el tipo de fotocopia que deseas elegir: "))
            if FO == "Carta":
                TFO = "Carta"
                CC = int(input("Ingresar cantidad de Fotocopias Carta: "))
                CAC = CAC + CC
                CAN = CC
                if sexo == "Hombre":
                    CCH = CCH + CAC
                elif sexo == "Mujer":
                    CCM = CCM + CAC
                if fecha == "Lunes":
                    CCL = CCL + CC
            if FO == "Oficio":
                TFO = "Oficio"
                CO = int(input("Ingresar cantidad de Fotocopias Oficio: "))
                CAO = CAO + CO
                CAN = CO
                if sexo == "Hombre":
                    COH = COH + CAO
                elif sexo == "Mujer":
                    COM = COM + CAO
                if fecha == "Lunes":
                    COL = COL + CO
            if FO == "ExtraOficio":
                TFO = "Extra Oficio"
                CEO = int(input("Ingresar cantidad de Fotocopias ExtraOficio: "))
                CAEO = CAEO + CEO
                CAN = CEO
                if sexo == "Hombre":
                    CEOH = CEOH + CAEO
                elif sexo == "Mujer":
                    CEOM = CEOM + CAEO
                if fecha == "Lunes":
                    CEOL = CEOL + CEO
            if sexo == "Hombre" and fecha == "Lunes":
                HTC = HTC + 1
            if sexo == "Mujer" and FO == "ExtraOficio":
                if edad > 25 and edad < 35:
                    MEO = MEO + 1
            TC = (CAC * 50) 
            TO = (CAO * 100) 
            TEO = (CAEO * 150) 
            if fecha == "Lunes":
                TC = TC - (TC * 0.10)
                TO = TO - (TO * 0.10)
                TEO = TEO - (TEO * 0.10)
            if edad > 60:
                CLM = CLM + 1

            archivo.write(f"\nFecha: {fecha} \nCliente: {cliente} \nCodigo: {codigo} \nNombre: {nombre} \nSexo: {sexo} \nEdad: {edad} \nTipo de Fotocopia: {TFO} \nCantidad de Fotocopias: {CAN} \n")
            archivo.close()
            O = str(input("¿Deseas agregar otro cliente?"))
            if O == "Si" or O == "si" or O == "SI":
                C = True
                cliente = cliente + 1
            else:
                menu()
            break
def datos_empresa():
    #Cantidad de Fotocopias Procesadas y su tipo.
    print(f"Cantidad de Fotocopias tipo Carta Procesadas: {CAC}")
    print(f"Cantidad de Fotocopias tipo Oficio Procesadas: {CAO}")
    print(f"Cantidad de Fotocopias tipo ExtraOficio Procesadas: {CAEO}")
    #Cantidad Vendida de Fotocopias y su tipo.
    print(f"Cantidad de Fotocopias tipo Carta Vendidas por Concepto: {TC}")
    print(f"Cantidad de Fotocopias tipo Oficio Vendidas por Concepto: {TO}")
    print(f"Cantidad de Fotocopias tipo ExtraOficio Vendidas por Concepto: {TEO}")
    #Cantidad de Fotocopias Vendidas de forma General.
    TF = TC + TO + TEO 
    print(f"Total de Fotocopias Vendidas por Concepto: {TF}")
    #Tipo de Fotocopia mas Vendida.
    if CAC > CAO and CAC > CAEO:
        FOM = "Carta"
        CM = CAC
    elif CAO > CAC and CAO > CAEO:
        FOM = "Oficio" 
        CM = CAO 
    elif CAEO > CAC and CAEO > CAO:
        FOM = "Extra Oficio"
        CM = CAEO
    print(f"El tipo de fotocopia mas Vendida fue {FOM}, con una cantidad de: {CM}")
    #El mayor número de fotocopias vendidas según el sexo de los clientes.
    CTH = CCH + COH + CEOH
    CTM = CCM + COM + CEOM
    if CTH > CTM:
        print(f"Los hombres vendieron la mayor cantidad de copias con una cantidad de: {CTH}")
    else:
        print(f"Las mujeres vendieron la mayor cantidad de copias con una cantidad de: {CTM}")
    if CTH == CTM:
        print(f"Ambos vendieron la misma cantidad de copias con una cantidad de: {CTM}")
    #Cantidad Vendida de Fotocopias tipo Carta a Hombres.
    print(f"Cantidad de Fotocopias tipo Carta Vendida a hombres fue: {CCH}")
    #Mujeres entre 25 y 35 años que compraron Fotocopias tipo ExtraOficio.
    print(f"Cantidad de Mujeres entre 25 y 35 años que compraron Fotocopia tipo Extra Oficio: {MEO}")
    #Cantidad de clientes mayores de 60 años. 
    print(f"Cantidad de clientes mayores de 60 años: {CLM}")
    #Cantidad de Fotocopias vendidas el Lunes.
    print(f"Cantidad de Fotocopias Carta vendidas los Lunes: {CCL}")
    print(f"Cantidad de Fotocopias Oficio vendidas los Lunes: {COL}")
    print(f"Cantidad de Fotocopias ExtraOficio vendidas los Lunes: {CEOL}")

    O3 = str(input("¿Deseas volver al menu?"))
    if O3 == "Si" or O3 == "si" or O3 == "SI":
        menu()
    else:
        datos_empresa()

def datos_clientes():
    archivo = open("Registros.txt")
    print(archivo.read())
    O2 = str(input("¿Deseas volver al menu?"))
    if O2 == "Si" or O2 == "si" or O2 == "SI":
        menu()
    else:
        datos_clientes()

def menu():
    print("Sistema de Empresa.")
    print("1 - Ingresar datos de Cliente.")
    print("2 - Observar datos de Clientes.")
    print("3 - Datos de la Empresa.")
    print("4 - Salir.")
    O1 = int(input())
    if O1 == 1:
        clientes()
    elif O1 == 2:
        datos_clientes()
    elif O1 == 3:
        datos_empresa()
menu()
