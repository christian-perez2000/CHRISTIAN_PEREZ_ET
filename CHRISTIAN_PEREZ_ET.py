import random
import csv

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
diccionario = {}

def asignar_Sueldo():
    for nombres in trabajadores:
        aleatorio = random.randint(300000,2500000)
        diccionario[nombres]=aleatorio
    return diccionario

def clasificar_Sueldos():
    lista = []
    print(f"{"Nombre empleado":24}{"Sueldo":24}")
    for nombre,sueldo in diccionario.items():
        if sueldo < 800000:
            lista.append(sueldo)
            print(f"{nombre:24}{sueldo}")
    print("\nSueldos menores a $800.000 TOTAL:", len(lista),"\n")

    print(f"{"Nombre empleado":24}{"Sueldo":24}")
    lista = []
    for nombre,sueldo in diccionario.items():
        if 800000 <= sueldo <= 2000000:
            print(f"{nombre:24}{sueldo}")
            lista.append(sueldo)
    print("\nSueldos entre $800.000 y 2.000.000 TOTAL:", len(lista),"\n")

    print(f"{"Nombre empleado":24}{"Sueldo":24}")
    lista = []
    for nombre,sueldo in diccionario.items():
        if sueldo > 2000000:
            print(f"{nombre:24}{sueldo}")
            lista.append(sueldo)
    print("\nSueldos menores a $800.000 TOTAL:", len(lista),"\n")

    print("TOTAL SUELDOS: $",sum(diccionario.values()))
def ver_Estadisticas():
    for sueldo in diccionario.values():
        if sueldo == max(diccionario.values()):
            print("Sueldo mas alto: $",sueldo)

    for sueldo in diccionario.values():
        if sueldo == min(diccionario.values()):
            print("Sueldo mas bajo: $",sueldo)
    valor = 0
    for sueldo in diccionario.values():
        valor = valor + sueldo
    print("Promedio de sueldos: $",valor/10)

    valor_media = 1
    for sueldo in diccionario.values():
        valor_media = sueldo *valor_media
    media_geometrica = (valor_media)**(1/10)
    print("Media geometrica: ",media_geometrica)

def reporte_Sueldos():
    print(f"{"Nombre empleado":24}{"Sueldo Base":24}{"Descuento Salud":24}{"Descuento AFP":24}{"Sueldo Liquido"}")
    for nombre,sueldo in diccionario.items():
        salud = sueldo*0.07
        afp = sueldo*0.12
        liquido = sueldo - (salud + afp)
        print(f"{nombre:24}{"$"+str(sueldo):24}{"$"+str(salud):24}{"$"+str(afp):24}{"$"+str(liquido)}")

def exportar():
    with open('trabajadores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(("nombre","sueldo"))
        for nombre, sueldo in diccionario.items():
            writer.writerow((nombre, sueldo))

while True:
    try:
        menu = int(input("""
        
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa

    """))
        match menu:
            case 1:
                asignar_Sueldo()
                print("Se le ha asignado un sueldo a los trabajadores.")
            case 2:
                clasificar_Sueldos()
            case 3:
                ver_Estadisticas()
            case 4:
                reporte_Sueldos()
                exportar()
            case 5:
                print("""
Finalizando programa...
Desarrollado por Christian Perez                
RUT 20.489.473-6    
                """)
                break
            case _:
                print("Opcion Invalida, intente nuevamente.")
    except:
        print("""
                   Opcion invalida
              Eliga una opcion del menu.""")