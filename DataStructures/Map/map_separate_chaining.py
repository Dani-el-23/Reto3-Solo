import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_entry as me
from DataStructures.List import list_node as ln

def new_map(num_elements, load_factor, prime=109345121):
   estimated_capacity = int(round(num_elements / load_factor))
   capacity = mf.next_prime(estimated_capacity)  

   my_map = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
   }
   for _ in range(capacity):
     al.add_last(my_map["table"], sll.new_list())

   return my_map
 

def get(my_map, key):
   indice = mf.hash_value(my_map,key)
   
   lista = al.get_element(my_map["table"],indice)
   
   elemento = None
   
   if not sll.is_empty(lista):
      list_el = sll.first_element(lista)
      
      while list_el is not None:
         if list_el["info"]["key"] == key:
            elemento = list_el
            break
         else:
            list_el = list_el["next"]
         
   
   return elemento        


def put(my_map, key, value):
    indice = mf.hash_value(my_map, key)
    elemento = me.new_map_entry(key, value)

    lista = al.get_element(my_map["table"], indice)

    if not sll.is_empty(lista):  # Si la lista NO está vacía, buscar la clave
        list_el = sll.first_element(lista)

        while list_el is not None:
            if list_el["info"]["key"] == key:
                list_el["info"] = elemento  # Si la clave existe, actualizar el valor
                return my_map  # Salir sin modificar la estructura
            list_el = list_el["next"]  # Continuar al siguiente nodo

        # Si la clave no estaba, agregar un nuevo nodo sin anidar listas
        sll.add_last(lista, elemento)

    else:  # Si la lista está vacía, inicializarla y agregar el nuevo nodo
        lista = sll.new_list()  # Crear una nueva lista enlazada vacía
        my_map["table"][indice] = lista  # Asignarla al índice
        sll.add_last(lista, elemento)  # Agregar el nodo

    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map



def rehash(my_map):
    
   new_capacity = mf.next_prime(2*my_map["capacity"])
   load_factor = my_map["limit_factor"]
   new_num_elements = load_factor*new_capacity
    
   n_map = new_map(new_num_elements,load_factor,my_map["prime"])
    
   for bucket in my_map["table"]["elements"]:
      if not sll.is_empty(bucket):
         list_el = sll.first_element(my_map)
         while list_el is not None:
            n_map = put(n_map,list_el["key"],list_el["value"])
        
   return n_map

 
 
def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def contains(my_map, key):
   indice = mf.hash_value(my_map, key)
   map_list = al.get_element(my_map["table"], indice) 

   if sll.is_empty(map_list): 
      return False

   node = sll.first_element(map_list)  
   while node is not None: 
      if default_compare(key, node["info"]) == 0:
         return True
      node = node["next"] 

   return False


def remove(my_map, key):
   if contains(my_map, key):
      indice = mf.hash_value(my_map,key)
      while default_compare(key, al.get_element(my_map["table"], indice)) != 0:
         indice += 1
         if indice == my_map["capacity"]:
            return "KeyError: key not found"
      entry = al.get_element(my_map["table"], indice)
      entry["key"] = "__EMPTY__"
      entry["value"] = "__EMPTY__"
      my_map["size"] -= 1
      return my_map

def size(my_map):
   return my_map["size"]


def is_empty(my_map):
   return my_map["size"] == 0


def key_set(my_map):
   key_set = al.new_list()
   for map_row in my_map["table"]:
      
      if not sll.is_empty(map_row):   
         entry = sll.first_element(map_row)
      
         while entry is not None:
            al.add_last(key_set, entry["info"]["info"]["key"])
            entry = entry["next"]
      
   return key_set


def value_set(my_map):
   value_set = al.new_list()
   for entry in my_map["table"]["elements"]:
      if entry["key"] is not None:
         value_set = al.add_last(value_set, entry["value"])
   return value_set


def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def get_(my_map, key):
   
   indice = mf.hash_value(my_map,key)
   
   lista = al.get_element(my_map["table"],indice)
   
   elemento = None
   
   if not sll.is_empty(lista):
      
      list_el = sll.first_element(lista)

      while list_el is not None:
         if list_el["info"]["key"] == key:
            elemento = list_el["info"]["value"]
            break
         else:
            list_el = list_el["next"]
         
   
   return elemento 