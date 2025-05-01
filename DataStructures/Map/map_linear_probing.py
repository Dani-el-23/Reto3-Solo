import random
import sys
import os
import math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me

def new_map(num_elements,load_factor,prime=109345121):

    my_map = {
        "prime": prime,
        "capacity":mf.next_prime(num_elements/load_factor),
        "scale":random.randint(1,prime-1),
        "shift":random.randint(0,prime-1),
        "table":al.new_list(),
        "current_factor":0,
        "limit_factor":load_factor,
        "size":0
    }

    
    element = me.new_map_entry(None,None)
    
    for _ in range(my_map["capacity"]):
        
        my_map["table"] = al.add_last(my_map["table"],element)
    
    return my_map

def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def find_slot(my_map,key,hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      elm = al.get_element(my_map["table"], hash_value)
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            if me.get_key(elm) == None or me.get_key(elm) == "__EMPTY__":
               found = True
      elif default_compare(key, elm) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def default_compare(key, entry):

   if key in me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def put(my_map,key,value):
    
   indice = mf.hash_value(my_map,key)
    
   ocupado,indice = find_slot(my_map,key,indice)
    
   if ocupado:
      entry = al.get_element(my_map["table"], indice)
      me.set_value(entry, value)
   else :
      elemento = me.new_map_entry(key,value)
    
      al.change_info(my_map["table"], indice, elemento)
      my_map["size"]+=1
      my_map["current_factor"] = my_map["size"]/my_map["capacity"]
    
      if my_map["current_factor"] > my_map["limit_factor"]:
         my_map = rehash(my_map)
   return my_map

def rehash(my_map):
   new_capacity = mf.next_prime(2 * my_map["capacity"])
   load_factor = my_map["limit_factor"]
   
   new_table = al.new_list()
   for _ in range(new_capacity):
      new_table = al.add_last(new_table, me.new_map_entry(None,None))
         
   
   for entry in new_table["elements"]:
      if entry["key"] is not None and entry["key"] != "__EMPTY__":
         _, pos = find_slot(my_map, entry["key"], mf.hash_value(my_map, entry["key"]))
         al.change_info(new_table, pos, entry)
   my_map["table"] = new_table
   my_map["capacity"] = new_capacity
   return my_map


def contains(my_map, key):
   indice = mf.hash_value(my_map,key)
   i = indice
   for _ in range(i, my_map["capacity"]):
      if default_compare(key, al.get_element(my_map["table"], indice)) == 0:
         return True
      indice += 1
   return False


def remove(my_map, key):
   if contains(my_map, key):
      indice = mf.hash_value(my_map,key)
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
   for entry in my_map["table"]["elements"]:
      if entry["key"] is not None:
         key_set = al.add_last(key_set, entry["key"])
   return key_set


def value_set(my_map):
   value_set = al.new_list()
   for entry in my_map["table"]["elements"]:
      if entry["key"] is not None:
         value_set = al.add_last(value_set, entry["value"])
   return value_set


def get(my_map, key):

   hash_value = mf.hash_value(my_map, key)

   pos = find_slot(my_map, key, hash_value)

   if pos[0]:

      entry = al.get_element(my_map["table"], pos[1])

      return me.get_value(entry)

   return None
