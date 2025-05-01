from DataStructures.List import list_node as ln

def new_list():
    """
    Crea una lista nueva del tipo lista simple encadenada.
    
    
    :returns:
    :rtype: single_linked_list
    """
    new_list = {"size": 0,
                "first": None,
                "last": None}
    return new_list

def is_empty(my_list):
    """
    Verifica si una lista está vacia. Retorna True si está vacía. 
    Retorna False si tiene al menos un elemento

    :param my_list: Lista la cual se va a verificar si está vacía
    :type my_list: single_linked_list
    
    :returns: True si la lista está vacía, False si tiene al menos un elemento
    :rtype: :class:`bool`
    """
    if my_list["first"] == None:
        return True
    else:
        return False

def size(my_list):
    """
    Verifica el tamaño en número de elementos de la lista

    :param my_list: Lista la cual se va a verificar el tamaño
    :type my_list: single_linked_list

    :returns: Tamaño de la lista
    :rtype: :class:`int`
    """
    return my_list["size"]

def add_first(my_list,element):
    """
    Añade un elemento al comienzo de la lista

    :param my_list: Lista a la cual se le va a añadir un elemento al comienzo
    :type my_list: single_linked_list
    :param element: Elemento que se va a añadir a la lista
    :type element: list_node
    
    :return: Lista con el elemento añadido al comienzo
    :rtype: single_linked_list
    """
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = node
        my_list["last"] = node
        
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
        
    my_list["size"] += 1
    return my_list

def add_last(my_list,element):
    """
    Añade un elemento al final de la lista

    :param my_list: Lista a la cual se le va a añadir un elemento al final
    :type my_list: single_linked_list
    :param element: Elemento que se va a añadir a la lista
    :type element: list_node
    
    :return: Lista con el elemento añadido al final
    :rtype: single_linked_list
    """
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = node
        my_list["last"] = node
    
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
        
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía. Si la lista está vacía, lanza un error.
    Esta función no elimina el elemento de la lista

    :param my_list: Lista de la cual se va a verificar el primer elemento
    :type my_list: single_linked_list
    
    :returns: Primer elemento de la lista
    :rtype: list_node
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return my_list["first"]

def last_element(my_list):
    """
    Retorna el último elemento de una lista no vacía. Si la lista está vacía, lanza un error.
    Esta función no elimina el elemento de la lista

    :param my_list: Lista de la cual se va a verificar el último elemento
    :type my_list: single_linked_list
    
    :returns: Último elemento de la lista
    :rtype: list_node
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return my_list["last"]

def get_element(my_list,pos):
    """
    Añade un elemento al final de la lista

    :param my_list: Lista a la cual se va a verificar un elemento dada su posición
    :type my_list: single_linked_list
    :param pos: Posición a verificar en la lista
    :type post: :class:`int`
    
    :return: Lista con el elemento añadido al final
    :rtype: single_linked_list
    """
    if pos<0 or pos>=size(my_list):
        raise Exception('IndexError: list index out of range')
    
    i=0
    elemento = my_list["first"]
    while i < pos:
        elemento = elemento["next"]
        i+=1
        
    return elemento

def delete_element(my_list,pos):
    """
    Remueve un elemento de la lista

    :param my_list: Lista a la cual se va a remover un elemento dada su posición
    :type my_list: single_linked_list
    :param pos: Posición a remover en la lista
    :type post: :class:`int`
    
    :return: Lista con el elemento removido
    :rtype: single_linked_list
    """
    
    
    if pos<0 or pos>=size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if size(my_list) == 1:  
            my_list["last"] = None

    else:
        prev_node = get_element(my_list, pos - 1)
        node_to_remove = prev_node["next"]
        prev_node["next"] = node_to_remove["next"]

        
    return my_list

def remove_first(my_list):
    """
    Remueve el primer elemento de la lista y lo retorna.

    :param my_list: Lista de la cual se va a remover el primer elemento
    :type my_list: single_linked_list

    :returns: Información del primer elemento removido
    :rtype: list_node
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elemento = my_list["first"]
    my_list = delete_element(my_list,0)
    
    return elemento["info"]

def remove_last(my_list):
    """
    Remueve el último elemento de la lista y lo retorna.

    :param my_list: Lista de la cual se va a remover el último elemento
    :type my_list: single_linked_list

    :returns: Información del último elemento removido
    :rtype: list_node
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elemento = my_list["last"]
    my_list = delete_element(my_list,size(my_list)-1)
    
    return elemento["info"]

def insert_element(my_list,element,pos):
    """
    Inserta un elemento en una posición específica de la lista.

    :param my_list: Lista en la cual se insertará el elemento
    :type my_list: single_linked_list
    :param element: Elemento que se va a insertar en la lista
    :type element: list_node
    :param pos: Posición en la cual se va a insertar el elemento
    :type pos: :class:`int`

    :return: Lista con el elemento insertado
    :rtype: single_linked_list
    """
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        return add_first(my_list,element)
    elif pos == size(my_list)-1:
        return add_last(my_list,element)
    else:
        nodo = ln.new_single_node(element)
        i=0
        nodo_actual = my_list["first"]
        while i < pos-1:
            nodo_actual = nodo_actual["next"]
            i+=1
        nodo["next"] = nodo_actual["next"]
        nodo_actual["next"] = nodo
        
    return my_list

def default_function(elemen_1, element_2):
    """
    Función de comparación predeterminada para comparar dos elementos.

    :param elemen_1: Primer elemento a comparar
    :type elemen_1: list_node
    :param element_2: Segundo elemento a comparar
    :type element_2: list_node

    :returns: 1 si el primer elemento es mayor, -1 si es menor, 0 si son iguales
    :rtype: :class:`int`
    """
    if elemen_1["info"] > element_2["info"]:
        return 1
    elif elemen_1["info"] < element_2["info"]:
        return -1
    return 0

def is_present(my_list,element,cmp_function):
    """
    Verifica si un elemento está presente en la lista usando una función de comparación.

    :param my_list: Lista en la cual se va a buscar el elemento
    :type my_list: single_linked_list
    :param element: Elemento a buscar en la lista
    :type element: list_node
    :param cmp_function: Función de comparación entre los elementos de la lista
    :type cmp_function: function

    :return: Posición del elemento si está presente, None si no está
    :rtype: :class:`int` o `None`
    """
    present = -1
    i=0
    elemento = my_list["first"]
    
    while elemento is not None:
        if cmp_function(elemento["info"], element) == 0:
            present = i
            break  
        elemento = elemento["next"]
        i += 1
        
    return present

def change_info(my_list,pos,new_info):
    """
    Modifica la información de un nodo en una posición específica.

    :param my_list: Lista en la cual se va a modificar la información
    :type my_list: single_linked_list
    :param pos: Posición del nodo a modificar
    :type pos: :class:`int`
    :param new_info: Nueva información que se asignará al nodo
    :type new_info: list_node

    :return: Lista con la información modificada
    :rtype: single_linked_list
    """
    elemento = get_element(my_list,pos)
    elemento["info"] = new_info
    return my_list

def exchange(my_list,pos1,pos2):
    """
    Intercambia los valores de dos nodos en posiciones específicas.

    :param my_list: Lista en la cual se van a intercambiar los nodos
    :type my_list: single_linked_list
    :param pos1: Posición del primer nodo
    :type pos1: :class:`int`
    :param pos2: Posición del segundo nodo
    :type pos2: :class:`int`

    :return: Lista con los nodos intercambiados
    :rtype: single_linked_list
    """
    elemento1_info = get_element(my_list,pos1)["info"]
    elemento2_info = get_element(my_list,pos2)["info"]
    
    my_list = change_info(my_list,pos1,elemento2_info)
    my_list = change_info(my_list,pos2,elemento1_info)
    
    return my_list

def sub_list(my_list,pos,num_elements):
    """
    Crea una sublista a partir de una lista dada, desde una posición inicial y con un número específico de elementos.

    :param my_list: Lista original de la cual se extraerá la sublista
    :type my_list: single_linked_list
    :param pos: Posición inicial de la sublista
    :type pos: :class:`int`
    :param num_elements: Número de elementos a incluir en la sublista
    :type num_elements: :class:`int`

    :return: Nueva sublista con los elementos seleccionados
    :rtype: single_linked_list
    """
    if pos+num_elements>size(my_list):
        raise Exception('IndexError: list index out of range')
    n_l = new_list()
    elemento_inicial = get_element(my_list,pos)
    n_l = add_first(n_l,elemento_inicial).copy()
    for i in range(1,num_elements-1):
        n_l = add_last(n_l,get_element(my_list,pos+i).copy())
    n_l["last"]["next"] = None
    
    return n_l


def default_sort_criteria(elemento1,elemento2):
    """
    Compara elementos en la llave ["imfo"] de los elementos1 y 2 (se asume que son nodos de lista)
    Verifica si el primer elemento es menor que el segundo
    
    :param elemento1: Elemento 1 a ser comparado
    :type elemento1: list_node
    :param elemento2: Elemento 2 a ser comparado
    :type elemento2: list_node

    :return: is_sorted
    :rtype: `bool`
    """
    is_sorted = False
    el1_info = elemento1["info"]
    el2_info = elemento2["info"]
    if el1_info < el2_info:
        is_sorted = True
    return is_sorted
    
def selection_sort(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif size(my_list) == 1: # Una lista de 1 elemento ya está ordenada
        
        return my_list

    else:
        
        punto_partida = first_element(my_list)
        while punto_partida is not None: # Itero sobre el pivote
            
            comparacion = punto_partida["next"]
            
            while comparacion is not None: # Itero sobre el pointer comparador
                if default_sort_criteria(comparacion,punto_partida):
                    
                    ln.exchange_info(comparacion,punto_partida)

                comparacion = comparacion["next"]
            
            punto_partida = punto_partida["next"]
        
    return my_list

def insertion_sort(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif size(my_list) == 1: # Una lista de 1 elemento ya está ordenada
        
        return my_list
    else:
        bot = my_list["first"]
        top = bot

        while top is not None:
            comparador = bot
            proximo = top["next"]
            if proximo is not None:
                if default_sort_criteria(top,proximo):
                    top = proximo
                else:
                    while comparador is not proximo:
                        if default_sort_criteria(comparador,proximo):
                            comparador = comparador["next"]
                        else:
                            ln.exchange_info(comparador,proximo)
                            comparador = comparador["next"]
            else:
                return my_list
                
    pass
