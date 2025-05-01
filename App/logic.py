import time
import csv
import os
from DataStructures.List import array_list as arr
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt 
from DataStructures.Map import map_linear_probing as mlp
from datetime import datetime

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    catalog = {
        "data": arr.new_list(),
        "bst_fechas": bst.new_tree(),
        "bst_edades": bst.new_tree(),
        "hash_nombres": mlp.new_map(113, 0.7)
    }
    return catalog

def load_data(catalog, filename):
    strt = get_time()
    date_fields = ["Date Rptd", "DATE OCC"]
    file = data_dir + filename
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=",")

    for dcase in input_file:
        for date_field in date_fields:
            dcase[date_field] = datetime.strptime(dcase[date_field], "%m/%d/%Y %I:%M:%S %p")

        # BST por fecha
        caso_fecha = add_bst(catalog["bst_fechas"], dcase, "DATE OCC")
        bst.put(catalog["bst_fechas"], dcase["DATE OCC"], caso_fecha)

        # BST por edad
        caso_edad = add_bst(catalog["bst_edades"], dcase, "Vict Age")
        bst.put(catalog["bst_edades"], dcase["Vict Age"], caso_edad)

        # MLP por nombre de área
        caso_area = add_mlp(catalog["hash_nombres"], dcase, "AREA NAME")
        mlp.put(catalog["hash_nombres"], dcase["AREA NAME"], caso_area)

        arr.add_last(catalog["data"], dcase)

    end = get_time()
    tiempo = delta_time(strt, end)
    return catalog, tiempo

def add_bst(bst_tree, dcase, shortc="Vict Age"):
    cas = bst.get(bst_tree, dcase[shortc])
    if cas is None:
        cas = arr.new_list()
    arr.add_last(cas, dcase)
    return cas

def add_mlp(hashmp, dcase, shortc="AREA NAME"):
    cas = mlp.get(hashmp, dcase[shortc])
    if cas is None:
        cas = arr.new_list()
    arr.add_last(cas, dcase)
    return cas

def get_data(catalog, id):
    return bst.get(catalog["bst_fechas"], id)

def req_1(catalog, fecha_inicial, fecha_final):
    """
    Retorna los crímenes ocurridos entre dos fechas.
    """
    lista_resultado = arr.new_list()
    fecha_ini = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_final, "%Y-%m-%d")

    fechas = bst.keys(catalog["bst_fechas"])

    for i in range(arr.size(fechas)):
        fecha_actual = arr.get_element(fechas, i)
        if fecha_ini <= fecha_actual <= fecha_fin:
            casos = bst.get(catalog["bst_fechas"], fecha_actual)
            for j in range(arr.size(casos)):
                crimen = arr.get_element(casos, j)
                arr.add_last(lista_resultado, crimen)

    # Ordenar por fecha y hora descendente sin comparador personalizado
    n = arr.size(lista_resultado)
    for i in range(n):
        for j in range(i + 1, n):
            a = arr.get_element(lista_resultado, i)
            b = arr.get_element(lista_resultado, j)
            fecha_a = a["DATE OCC"]
            fecha_b = b["DATE OCC"]
            hora_a = int(a["TIME OCC"])
            hora_b = int(b["TIME OCC"])
            if fecha_a < fecha_b or (fecha_a == fecha_b and hora_a < hora_b):
                arr.exchange(lista_resultado, i, j)

    return lista_resultado






def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, nombre_area, N):
    """
    Retorna los N crímenes más recientes para un área dada.
    """
    lista_area = arr.new_list()

    for i in range(arr.size(catalog["crimes_list"])):
        crimen = arr.get_element(catalog["crimes_list"], i)
        if crimen["AREA NAME"].lower() == nombre_area.lower():
            arr.add_last(lista_area, crimen)

    # Orden descendente por fecha y hora
    def comparador(c1, c2):
        f1 = datetime.strptime(c1["DATE OCC"], "%m/%d/%Y")
        f2 = datetime.strptime(c2["DATE OCC"], "%m/%d/%Y")
        if f1 != f2:
            return -1 if f1 > f2 else 1
        elif c1["TIME OCC"] != c2["TIME OCC"]:
            return int(c2["TIME OCC"]) - int(c1["TIME OCC"])
        else:
            return int(c2["AREA"]) - int(c1["AREA"])

    lista_ordenada = arr.merge_sort_list_of_dict(lista_area, "DATE OCC", comparador)
    N = min(N, arr.size(lista_ordenada))
    return lista_ordenada, arr.size(lista_area), N




def req_4(catalog, edad_min, edad_max, N):
    graves = []
    no_graves = []

    def recorrer_nodo(nodo):
        if nodo is None:
            return
        recorrer_nodo(nodo['left'])
        lista = nodo['value']
        for i in range(arr.size(lista)):
            crimen = arr.get_element(lista, i)
            edad_str = crimen.get("Vict Age", "")
            if edad_str.isdigit():
                edad = int(edad_str)
                if edad_min <= edad <= edad_max:
                    if crimen["Part 1-2"] == "1":
                        graves.append(crimen)
                    elif crimen["Part 1-2"] == "2":
                        no_graves.append(crimen)
        recorrer_nodo(nodo['right'])

    recorrer_nodo(catalog["bst"]["root"])

    graves_ordenados = sorted(
        graves,
        key=lambda c: (
            -int(c["Vict Age"]),
            datetime.strptime(c["DATE OCC"], "%m/%d/%Y"),
            int(c["TIME OCC"])
        )
    )

    no_graves_ordenados = sorted(
        no_graves,
        key=lambda c: (
            -int(c["Vict Age"]),
            datetime.strptime(c["DATE OCC"], "%m/%d/%Y"),
            int(c["TIME OCC"])
        )
    )

    resultado = graves_ordenados[:N]
    if len(resultado) < N:
        resultado += no_graves_ordenados[:N - len(resultado)]

    total = len(graves) + len(no_graves)
    return resultado, total





def req_5(catalog, N):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5


def req_6(catalog, sexo, mes_consulta, N):
    resumen_areas = {}

    def recorrer_nodo(nodo):
        if nodo is None:
            return
        recorrer_nodo(nodo['left'])
        lista = nodo['value']
        for i in range(arr.size(lista)):
            crimen = arr.get_element(lista, i)
            sexo_victima = crimen["Vict Sex"]
            fecha_str = crimen["DATE OCC"]

            partes_fecha = fecha_str.split("/")
            es_fecha_valida = (
                len(partes_fecha) == 3 and
                partes_fecha[0].isdigit() and
                partes_fecha[2].isdigit()
            )

            if (
                sexo_victima == sexo and
                es_fecha_valida and
                int(partes_fecha[0]) == mes_consulta
            ):
                area = crimen["AREA NAME"]
                mes = int(partes_fecha[0])
                año = int(partes_fecha[2])
                clave_mes = (año, mes)

                if area not in resumen_areas:
                    resumen_areas[area] = {"total": 1, "detalle": {clave_mes: 1}}
                else:
                    resumen_areas[area]["total"] += 1
                    if clave_mes in resumen_areas[area]["detalle"]:
                        resumen_areas[area]["detalle"][clave_mes] += 1
                    else:
                        resumen_areas[area]["detalle"][clave_mes] = 1

        recorrer_nodo(nodo['right'])

    recorrer_nodo(catalog["bst"]["root"])

    lista_areas = []
    for area in resumen_areas:
        detalle = resumen_areas[area]["detalle"]
        total = resumen_areas[area]["total"]
        for clave in detalle:
            año, mes = clave
            cantidad_mes = detalle[clave]
            lista_areas.append({
                "area": area,
                "mes": mes,
                "año": año,
                "cantidad_mes": cantidad_mes,
                "cantidad_total": total
            })

    lista_ordenada = sorted(
        lista_areas,
        key=lambda x: (
            x["cantidad_total"],
            x["cantidad_mes"],
            x["año"],
            x["area"].lower()
        )
    )

    return lista_ordenada[:N]



def req_7(catalog, sexo, edad_min, edad_max, N):
    crimenes = {}

    def recorrer_nodo(nodo):
        if nodo is None:
            return
        recorrer_nodo(nodo['left'])
        lista = nodo['value']
        for i in range(arr.size(lista)):
            crimen = arr.get_element(lista, i)

            edad_str = crimen["Vict Age"]
            edad_valida = edad_str.isdigit()
            edad = int(edad_str) if edad_valida else -1

            fecha_str = crimen["DATE OCC"]
            partes_fecha = fecha_str.split("/")
            es_fecha_valida = len(partes_fecha) == 3 and partes_fecha[2].isdigit()
            año = int(partes_fecha[2]) if es_fecha_valida else -1

            if (crimen["Vict Sex"] == sexo and
                edad_valida and edad_min <= edad <= edad_max and
                es_fecha_valida):

                codigo = crimen["Crm Cd"]
                if codigo not in crimenes:
                    crimenes[codigo] = {
                        "total": 0,
                        "por_edad": {},
                        "por_año": {}
                    }

                crimenes[codigo]["total"] += 1

                if edad not in crimenes[codigo]["por_edad"]:
                    crimenes[codigo]["por_edad"][edad] = 1
                else:
                    crimenes[codigo]["por_edad"][edad] += 1

                if año not in crimenes[codigo]["por_año"]:
                    crimenes[codigo]["por_año"][año] = 1
                else:
                    crimenes[codigo]["por_año"][año] += 1

        recorrer_nodo(nodo['right'])

    recorrer_nodo(catalog["bst"]["root"])

    lista = []
    for codigo, data in crimenes.items():
        lista.append({
            "codigo": codigo,
            "total": data["total"],
            "por_edad": data["por_edad"],
            "por_año": data["por_año"]
        })

    lista_ordenada = sorted(lista, key=lambda x: -x["total"])
    return lista_ordenada[:N]





def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

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
