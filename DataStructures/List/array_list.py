from datetime import datetime

def new_list():
    """Crea una lista (de tipo array_list) vacía"""
    new_list = {
        "size": 0,
        "elements":[]
    }
    return new_list


def is_empty(my_list):
    """Verifica si la lista está vacía."""
    if my_list["size"] == 0:
        return True
    else :
        return False


def size(my_list):
    """Retorna el tamaño de la lista."""
    return my_list["size"]


def add_first(my_list, element):
    """Agrega un elemento al inicio de la lista."""
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list,element):
    """Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1."""
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def first_element(my_list):
    """Retorna el primer elemento de la lista. Si la lista está vacía, 
    lanza un error IndexError: list index out of range. Esta función no 
    elimina el elemento de la lista."""
    if my_list["size"] != 0:
        return my_list["elements"][0]
    else :
        return "IndexError: list index out of range"


def last_element(my_list):
    """Retorna el último elemento de la lista. Si la lista está vacía, 
    lanza un error IndexError: list index out of range. Esta función no 
    elimina el elemento de la lista."""
    if my_list["size"] != 0:
        return my_list["elements"][-1]
    else :
        return "IndexError: list index out of range"
    
    
def get_element(my_list,pos):
    """Retorna el elemento en la posición pos, la cual debe ser igual o mayor
    a cero y menor al tamaño de la lista. 0 <= pos < size(my_list).
    Si la posición no es válida, lanza un error IndexError: list index out of range. 
    Esta función no elimina el elemento de la lista."""
    if 0 <= pos < size(my_list):
        return my_list["elements"][pos]
    else :
        return "IndexError: list index out of range"


def delete_element(my_list, pos):
    """Elimina el elemento en la posición pos, la cual debe ser igual o mayor a cero 
    y menor al tamaño de la lista. 0 <= pos < size(my_list). Si la posición no es válida, 
    lanza un error IndexError: list index out of range."""
    if 0 <= pos < size(my_list):
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list
    else :
        return "IndexError: list index out of range"


def remove_first(my_list):
    """Elimina el primer elemento de la lista y disminuye el tamaño de la lista en 1. 
    Si la lista está vacía, lanza un error IndexError: list index out of range."""
    if size(my_list) != 0:
        removed_element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return removed_element
    else:
        return "IndexError: list index out of range"


def remove_last(my_list):
    """Elimina el último elemento de la lista y disminuye el tamaño de la lista en 1. 
    Si la lista está vacía, lanza un error IndexError: list index out of range."""
    if size(my_list) != 0:
        removed_element = my_list["elements"].pop(-1)
        my_list["size"] -= 1
        return removed_element
    else:
        return "IndexError: list index out of range"


def insert_element(my_list, element, pos):
    """Inserta el elemento en la posición pos. La lista puede estar vacia o tener elementos. 
    Se incrementa el tamaño de la lista en 1."""
    my_list["size"] += 1
    my_list["elements"][pos] = element
    return my_list
    

def default_function(element_1, element_2):
    """Esta función de comparación por defecto compara dos elementos y retorna 0 si son iguales, 
    1 si el element_1 es mayor que element_2 y -1 si element_1 es menor que element_2."""
    if element_1 == element_2:
        return 0
    elif element_1 > element_2:
        return 1
    else :
        return -1
    
def default_function2(element_1, element_2):
    """Esta función de comparación por defecto compara dos elementos y retorna 0 si son iguales, 
    1 si el element_1 es mayor que element_2 y -1 si element_1 es menor que element_2."""
    if element_1 == element_2:
        return 0
    elif element_1 < element_2:
        return 1
    else :
        return -1


def is_present(my_list, element, cmp_function):
    """Para comparar los elementos, se utiliza la función de comparación cmp_function. 
    Si el elemento está presente retorna su posición, en caso contrario retorna -1."""
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1



def change_info(my_list, pos, new_info):
    """Cambia la información del elemento en la posición pos por la información new_info. 
    Si la posición no es válida, lanza un error IndexError: list index out of range."""
    if pos < size(my_list):
        my_list["elements"][pos] = new_info
        return my_list
    else :
        return "IndexError: list index out of range"


def exchange(my_list, pos_1, pos_2):
    """Intercambia la información de los elementos en las posiciones pos_1 y pos_2. 
    Si alguna de las posiciones no es válida, lanza un error IndexError: list index out of range."""
    current_size = size(my_list)
    if 0 <= pos_1 < current_size and 0 <= pos_2 < current_size:
        temp = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = temp
        return my_list
    else :
        return "IndexError: list index out of range"


def sub_list(my_list, pos_i, num_elements):
    """Retorna una sublista de la lista original que inicia en la posición pos_i y contiene num_elements elementos. 
    Si la posición inicial no es válida, lanza un error IndexError: list index out of range."""
    current_size = size(my_list)
    if 0 <= pos_i < current_size:
        end_pos = pos_i + num_elements
        end_pos = min(end_pos, current_size)
        elements = my_list["elements"][pos_i:end_pos]
        return {"size": len(elements), "elements": elements}
    else :
        return "IndexError: list index out of range"
    
def merge_sort(my_list):
    
    if size(my_list) > 1:
        top = size(my_list)
        mid = (top)//2
        
        
        list_1 = sub_list(my_list,0,mid)
        list_2 = sub_list(my_list,mid,size(my_list)-1)
        
        list_1 = merge_sort(list_1)
        list_2 = merge_sort(list_2)
    
    if size(my_list)==1:
        return my_list
    else:
        return merge_lists(list_1,list_2)
    
def merge_lists(list_1,list_2):
    merged_list = new_list()
    
    while not is_empty(list_1) and not is_empty(list_2):
        element_1 = first_element(list_1)
        element_2 = first_element(list_2)
        
        if element_1 < element_2:
            add_last(merged_list,element_1)
            remove_first(list_1)
        else:
            add_last(merged_list,element_2)
            remove_first(list_2)
    
    while not is_empty(list_1):
        element_1 = first_element(list_1)
        merged_list = add_last(merged_list,element_1)
        list_1 = delete_element(list_1,0)
            
    while not is_empty(list_2):
        element_2 = first_element(list_2)
        merged_list = add_last(merged_list,element_2)
        list_2 = delete_element(list_2,0)
            
    return merged_list

def merge_sort_ext(my_list,sorting_key,extsorting_key,cmp_function=default_function):
    
    if size(my_list) > 1:
        top = size(my_list)
        mid = (top)//2
        
        
        list_1 = sub_list(my_list,0,mid)
        list_2 = sub_list(my_list,mid,size(my_list)-1)
        
        list_1 = merge_sort_ext(list_1,sorting_key,extsorting_key, cmp_function)
        list_2 = merge_sort_ext(list_2,sorting_key,extsorting_key, cmp_function)
    
    if size(my_list)==1:
        return my_list
    else:
        return merge_list_ext(list_1,list_2,sorting_key,extsorting_key,cmp_function)
    
def merge_list_ext(list_1,list_2,sorting_key,extsorting_key, cmp_function=default_function):
    merged_list = new_list()
    
    while not is_empty(list_1) and not is_empty(list_2):
        element_1 = first_element(list_1)
        element_2 = first_element(list_2)
        
        criteria_1 = first_element(list_1)[sorting_key]
        criteria_2 = first_element(list_2)[sorting_key]
        
        if cmp_function(criteria_1,criteria_2) ==-1:
            add_last(merged_list,element_1)
            remove_first(list_1)
        elif cmp_function(criteria_1,criteria_2) == 0:
            criteria_1 = first_element(list_1)[extsorting_key]
            criteria_2 = first_element(list_2)[extsorting_key]
            
            if cmp_function(criteria_1,criteria_2) == -1:
                add_last(merged_list,element_1)
                remove_first(list_1)
            else:
                add_last(merged_list,element_2)
                remove_first(list_2)
        else:
            add_last(merged_list,element_2)
            remove_first(list_2)
    
    while not is_empty(list_1):
        element_1 = first_element(list_1)
        merged_list = add_last(merged_list,element_1)
        list_1 = delete_element(list_1,0)
            
    while not is_empty(list_2):
        element_2 = first_element(list_2)
        merged_list = add_last(merged_list,element_2)
        list_2 = delete_element(list_2,0)
            
    return merged_list



def concatenate_lists(list_1,list_2):
    concatenated_list = new_list()
    
    concatenate_lists = concatenate_lists["elements"].append(list_1["elements"])
    concatenate_lists = concatenate_lists["elements"].append(list_2["elements"])
    concatenated_list["size"] = size(list_1)+size(list_2)
    
    return concatenated_list

def count_elements_lists_of_lists(my_list,count_index,info):
    counter = 0
    
    for i in range(size(my_list)):
        
        elemento = get_element(get_element(my_list,i),count_index)
        
        if default_function(elemento,info) == 0:
            counter+=1
            
    return counter

def find_minimum(my_list,field=None,minimum=float('inf'),baseline=None):
    min_index = -1
    for i in range(size(my_list)):
        elemento = get_element(my_list,i)
        
        if field is not None:
            elemento = elemento[field]
        
        try:
            elemento = int(elemento)
        except:
            pass
        
        if baseline is not None:
            if default_function(elemento,minimum) == -1 and default_function(elemento,baseline) != -1:
                minimum = elemento
                min_index = i
        else:
            if default_function(elemento,minimum) == -1:
                minimum = elemento
                min_index = i
    return (minimum,min_index) 

def find_maximum(my_list,field=None,maximum=float('-inf'),top=None):
    max_index = -1
    for i in range(size(my_list)):
        
        elemento = get_element(my_list,i)
        
        if field is not None:
            elemento = elemento[field]
        
        try:
            elemento = int(elemento)
        except:
            pass
        
        
        
        if top is not None:
            if default_function(elemento,maximum) == 1 and default_function(elemento,top) != 1:
                maximum = elemento
                max_index = i
        else:
            if default_function(elemento,maximum) == 1:
                maximum = elemento
                max_index = i
            
    return (maximum,max_index)

