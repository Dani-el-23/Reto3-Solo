import sys
import App.logic as logic
from datetime import datetime
from tabulate import tabulate
import time
from DataStructures.List import array_list as arr



def new_logic():
    """
        Se crea una instancia del controlador
    """
    return logic.new_logic()

    #TODO: Se crea una instancia del controlador
    pass

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    cond = int(input("Ingrese el porcentaje de datos a cargar (20-40-60-80-100): "))
    if cond == 20:
        data_dir = 'Crime_in_LA/Crime_in_LA_20.csv'
    elif cond == 40:
        data_dir = 'Crime_in_LA/Crime_in_LA_40.csv'
    elif cond == 60:
        data_dir = 'Crime_in_LA/Crime_in_LA_60.csv'
    elif cond == 80:
        data_dir = 'Crime_in_LA/Crime_in_LA_80.csv'
    elif cond == 100:
        data_dir = 'Crime_in_LA/Crime_in_LA_100.csv'
    else:
        print("Porcentaje no válido, se cargará el 100% de los datos")
        data_dir = 'Crime_in_LA/Crime_in_LA_100.csv'

    print("Cargando información de los archivos ....\n")
    data, tiempo = logic.load_data(control, data_dir)

    print(f"Se han cargado {data['data']['size']} elementos")
    print(f"El tiempo de carga fue de: {tiempo} milisegundos\n")

    prim_cinco = data["data"]["elements"][:5]
    ult_cinco = data["data"]["elements"][-5:]
    llaves_deseadas = ["DR_NO", "Date Rptd", "DATE OCC", "AREA NAME", "Crm Cd"]

    print("Los primeros cinco elementos son:")
    for crimen in prim_cinco:
        print(" - ", {k: crimen[k] for k in llaves_deseadas})

    print("\nLos últimos cinco elementos son:")
    for crimen in ult_cinco:
        print(" - ", {k: crimen[k] for k in llaves_deseadas})
    

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = logic.get_data(control, id)
    if data == None:
        print("No se encontró el dato")
    else:
        print(tabulate(data, headers="keys", tablefmt="pretty"))







def print_req_1(control):
    """
    Imprime los crímenes ocurridos entre dos fechas (requerimiento 1).
    """
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")

    resultado = logic.requerimiento_1(control, fecha_inicial, fecha_final)

    total = arr.size(resultado)
    print(f"\nTotal de crímenes entre {fecha_inicial} y {fecha_final}: {total}\n")

    llaves = ["DR_NO", "DATE OCC", "TIME OCC", "AREA NAME", "Crm Cd"]

    if total == 0:
        print("No se encontraron crímenes en el rango de fechas.")
        return

    primeros = arr.sublist(resultado, 1, min(5, total))["elements"]
    ultimos = arr.sublist(resultado, max(1, total - 4), min(5, total))["elements"]

    print("Primeros 5 crímenes (más recientes):")
    for crimen in primeros:
        print(" -", {k: crimen[k] for k in llaves})

    print("\nÚltimos 5 crímenes (menos recientes):")
    for crimen in ultimos:
        print(" -", {k: crimen[k] for k in llaves})


    



def print_req_2(control):
    
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
    Imprime los crímenes ocurridos entre dos edades de víctimas (requerimiento 3).
    """
    edad_min = int(input("Ingrese la edad mínima de la víctima: "))
    edad_max = int(input("Ingrese la edad máxima de la víctima: "))

    resultado = logic.requerimiento_3(control, edad_min, edad_max)

    total = arr.size(resultado)
    print(f"\nTotal de crímenes con edades entre {edad_min} y {edad_max}: {total}\n")

    llaves = ["DR_NO", "DATE OCC", "Vict Age", "Vict Descent", "Crm Cd"]

    if total == 0:
        print("No se encontraron crímenes en el rango de edades.")
        return

    primeros = arr.sublist(resultado, 1, min(5, total))["elements"]
    ultimos = arr.sublist(resultado, max(1, total - 4), min(5, total))["elements"]

    print("Primeros 5 crímenes:")
    for crimen in primeros:
        print(" -", {k: crimen[k] for k in llaves})

    print("\nÚltimos 5 crímenes:")
    for crimen in ultimos:
        print(" -", {k: crimen[k] for k in llaves})




def print_req_4(control):
    """
    Imprime los N crímenes con víctimas en un rango de edad, ordenados por gravedad y edad
    """
    print("Consulta de crímenes por rango de edad y gravedad")
    edad_min = input("Ingrese la edad mínima: ")
    edad_max = input("Ingrese la edad máxima: ")
    N = input("Ingrese el número de crímenes a consultar: ")

    if edad_min.isdigit() and edad_max.isdigit() and N.isdigit():
        edad_min = int(edad_min)
        edad_max = int(edad_max)
        N = int(N)
        resultado, total = logic.req_4(control, edad_min, edad_max, N)

        print(f"\nTotal de crímenes encontrados: {total}")
        print(f"Mostrando los primeros {len(resultado)} crímenes:\n")

        i = 1
        while i <= len(resultado):
            c = resultado[i - 1]
            print(f"Crimen #{i}")
            print(f"  DR_NO: {c['DR_NO']}")
            print(f"  Fecha: {c['DATE OCC']}")
            print(f"  Hora: {c['TIME OCC']}")
            print(f"  Área: {c['AREA NAME']}")
            print(f"  Subárea: {c['Rpt Dist No']}")
            print(f"  Gravedad: {c['Part 1-2']}")
            print(f"  Código Crimen: {c['Crm Cd']}")
            print(f"  Descripción: {c['Crm Cd Desc']}")
            print(f"  Edad Víctima: {c['Vict Age']}")
            print(f"  Sexo Víctima: {c['Vict Sex']}")
            print(f"  Estado del Caso: {c['Status']}")
            print(f"  Dirección: {c['LOCATION']}")
            print("-" * 40)
            i += 1
    else:
        print("Todos los valores deben ser números enteros válidos.")




def print_req_5(control):
    """
    Imprime los N tipos de crimen más frecuentes
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
    Imprime las N áreas más seguras para un sexo en un mes específico del año
    """
    print("Consulta de las áreas más seguras por sexo y mes")

    sexo = input("Ingrese el sexo a consultar (ej. 'M' o 'F'): ")
    mes_str = input("Ingrese el mes como número (1 a 12): ")
    N_str = input("Ingrese cuántas áreas desea consultar (Top N): ")

    if mes_str.isdigit() and N_str.isdigit():
        mes = int(mes_str)
        N = int(N_str)

        resultado = logic.req_6(control, sexo, mes, N)

        print(f"\nTop {len(resultado)} áreas más seguras para víctimas de sexo '{sexo}' en el mes {mes}:\n")

        i = 0
        while i < len(resultado):
            r = resultado[i]
            print(f"Área #{i + 1}")
            print(f"  Nombre del área: {r['area']}")
            print(f"  Mes y Año: ({r['mes']}, {r['año']})")
            print(f"  Crímenes en ese mes: {r['cantidad_mes']}")
            print(f"  Total crímenes en el área: {r['cantidad_total']}")
            print("-" * 40)
            i += 1
    else:
        print("Por favor, ingrese valores numéricos válidos para mes y cantidad.")





def print_req_7(control):
    """
    Imprime los N crímenes más comunes para víctimas de un sexo en un rango de edad
    """
    print("Consulta de crímenes más comunes por sexo y edad")

    sexo = input("Ingrese el sexo de la víctima (ej. 'M' o 'F'): ")
    edad_min_str = input("Edad mínima: ")
    edad_max_str = input("Edad máxima: ")
    N_str = input("Cantidad de crímenes a listar: ")

    if edad_min_str.isdigit() and edad_max_str.isdigit() and N_str.isdigit():
        edad_min = int(edad_min_str)
        edad_max = int(edad_max_str)
        N = int(N_str)

        resultado = logic.req_7(control, sexo, edad_min, edad_max, N)

        print(f"\nCrímenes más comunes para sexo '{sexo}' entre edades {edad_min}-{edad_max}:\n")
        i = 1
        while i <= len(resultado):
            c = resultado[i - 1]
            print(f"Crimen #{i}")
            print(f"  Código del crimen: {c['codigo']}")
            print(f"  Total de crímenes: {c['total']}")

            print("  Crímenes por edad:")
            for edad in sorted(c["por_edad"]):
                print(f"    Edad {edad}: {c['por_edad'][edad]}")

            print("  Crímenes por año:")
            for año in sorted(c["por_año"]):
                print(f"    Año {año}: {c['por_año'][año]}")
            print("-" * 40)
            i += 1
    else:
        print("Debe ingresar valores numéricos válidos.")



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
    
def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
