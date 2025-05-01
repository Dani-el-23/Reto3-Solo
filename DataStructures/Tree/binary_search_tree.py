from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sl

def new_map():
    """Crea una nueva tabla de simbolos (map) ordenada basada en un árbol binario de búsqueda (BST)."""
    return {"root": None}

def new_tree():
    return {"root": None}

def put(bst_tree, key, value):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). Si la llave ya existe, se actualiza el value del nodo."""
    
    node = insert_node(bst_tree["root"], key, value)
    bst_tree["root"] = node
    return bst_tree


def insert_node(node, key, value):
    """Inserta un nuevo nodo en el árbol binario de búsqueda (BST). Si la llave ya existe, se actualiza el value del nodo."""
    
    if node is None:
        return bn.new_node(key, value)

    if key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value
        return node
    
    left_size = node["left"]["size"] if node["left"] is not None else 0
    right_size = node["right"]["size"] if node["right"] is not None else 0
    node["size"] = 1 + left_size + right_size
    return node

def get(bst_tree, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su value."""
    
    node = get_node(bst_tree["root"], key)
    if node is not None:
        return node["value"]
    return None


def get_node(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve el nodo."""
    
    if root is None or root["key"] == key:
        return root
    if key < root["key"]:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)
    

def remove(bst_tree, key):
    """Elimina un nodo del árbol binario de búsqueda (BST)."""    
    node = remove_node(bst_tree["root"], key)
    bst_tree["root"] = node
    return bst_tree


def remove_node(root, key):
    """Elimina un nodo del árbol binario de búsqueda (BST)."""    
        
    if root is None:
        return root
    
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
    else:
        if root["left"] is None:
            temp = get_max_node(root["left"])
            root["key"] = temp["key"]
            root["value"] = temp["value"]
            root["right"] = remove_node(root["right"], temp["key"])
        else:
            temp = get_min_node(root["right"])
            root["key"] = temp["key"]
            root["value"] = temp["value"]
            root["left"] = remove_node(root["left"], temp["key"])
    return root


def contains(bst_tree, key):
    """Verifica si una llave existe en el árbol binario de búsqueda (BST)."""    
    return get(bst_tree, key) is not None


def size(bst_tree):
    """Devuelve el tamaño del árbol binario de búsqueda (BST)."""    
    return size_tree(bst_tree["root"])


def size_tree(root):
    """Devuelve el tamaño del árbol binario de búsqueda (BST)."""    
    if root is None:
        return 0
    return root["size"]


def is_empty(bst_tree):
    """Verifica si el árbol binario de búsqueda (BST) está vacío."""    
    return bst_tree["root"] is None


def key_set(bst_tree):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (BST)."""    
    keys = sl.new_list()
    key_set_tree(bst_tree["root"], keys)
    return keys

def key_set_tree(root, keys):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (BST)."""    
    if root is not None:
        key_set_tree(root["left"], keys)
        sl.add_last(keys, root["key"])
        key_set_tree(root["right"], keys)
        

def value_set(bst_tree):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (BST)."""    
    values = sl.new_list()
    value_set_tree(bst_tree["root"], values)
    return values


def value_set_tree(root, values):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (BST)."""    
    if root is not None:
        value_set_tree(root["left"], values)
        sl.add_last(values, root["value"])
        value_set_tree(root["right"], values)
        

def get_min(bst_tree):
    """Devuelve el nodo con la llave mínima en el árbol binario de búsqueda (BST)."""    
    return get_min_node(bst_tree["root"])

def get_min_node(root):
    """Devuelve el nodo con la llave mínima en el árbol binario de búsqueda (BST)."""    
    if root is None:
        return None
    if root["left"] is None:
        return root["key"]
    return get_min_node(root["left"])


def get_max(bst_tree):
    """Devuelve el nodo con la llave máxima en el árbol binario de búsqueda (BST)."""    
    return get_max_node(bst_tree["root"])


def get_max_node(root):
    """Devuelve el nodo con la llave máxima en el árbol binario de búsqueda (BST)."""    
    if root is None:
        return None
    if root["right"] is None:
        return root["key"]
    return get_max_node(root["right"])


def delete_min(bst_tree):
    """Elimina el nodo con la llave mínima en el árbol binario de búsqueda (BST)."""    
    bst_tree["root"] = delete_min_node(bst_tree["root"])
    return bst_tree


def delete_min_node(root):
    """Elimina el nodo con la llave mínima en el árbol binario de búsqueda (BST)."""    
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_node(root["left"])
    return root


def delete_max(bst_tree):
    """Elimina el nodo con la llave máxima en el árbol binario de búsqueda (BST)."""    
    bst_tree["root"] = delete_max_node(bst_tree["root"])
    return bst_tree


def delete_max_node(root):
    """Elimina el nodo con la llave máxima en el árbol binario de búsqueda (BST)."""    
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_node(root["right"])
    return root

def floor(bst_tree, key):
    """Devuelve la llave más grande menor o igual a la llave dada."""    
    return floor_key(bst_tree["root"], key)


def floor_key(root, key):
    """Devuelve la llave más grande menor o igual a la llave dada."""    
    if root is None:
        return None
    if key == root["key"]:
        return root["key"]
    if key < root["key"]:
        return floor_key(root["left"], key)
    
    right_floor = floor_key(root["right"], key)
    if right_floor is not None:
        return right_floor
    return root["key"]


def ceiling(bst_tree, key):
    """Devuelve la llave más pequeña mayor o igual a la llave dada."""    
    return ceiling_key(bst_tree["root"], key)


def ceiling_key(root, key):
    """Devuelve la llave más pequeña mayor o igual a la llave dada."""    
    if root is None:
        return None
    if key == root["key"]:
        return root["key"]
    if key > root["key"]:
        return ceiling_key(root["right"], key)
    
    left_ceiling = ceiling_key(root["left"], key)
    if left_ceiling is not None:
        return left_ceiling
    return root["key"]


def select(bst_tree, k):
    """Devuelve la llave del nodo en la posición k."""    
    return select_key(bst_tree["root"], k)


def select_key(root, k):
    """Devuelve la llave del nodo en la posición k."""    
    if root is None:
        return None
    left_size = size_tree(root["left"]) if root["left"] is not None else 0
    if k < left_size:
        return select_key(root["left"], k)
    elif k > left_size:
        return select_key(root["right"], k - left_size - 1)
    return root["key"]


def rank(bst_tree, key):
    """Devuelve el número de llaves menores que la llave dada."""    
    return rank_key(bst_tree["root"], key)


def rank_key(root, key):
    """Devuelve el número de llaves menores que la llave dada."""    
    nd = get_node(root, key)
    if nd is None:
        return 0
    else:
        return size_tree(nd)-1
    
    

def height(bst_tree):
    """Devuelve la altura del árbol binario de búsqueda (BST)."""    
    return height_tree(bst_tree["root"])


def height_tree(root):
    """Devuelve la altura del árbol binario de búsqueda (BST)."""    
    if root is None:
        return 0
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    return 1 + max(left_height, right_height)


def keys(bst_tree, key_initial, key_final):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (BST)."""    
    keys = sl.new_list()
    keys_range(bst_tree["root"],key_initial, key_final, keys)
    return keys


def keys_range(root, key_initial, key_final, keys):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (BST)."""    
    if root is None:
        return
    if key_initial > root["key"]:
        keys_range(root["right"], key_initial, key_final, keys)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(keys, root["key"])
        keys_range(root["right"], key_initial, key_final, keys)
        keys_range(root["left"], key_initial, key_final, keys)
    if key_final < root["key"]:
        keys_range(root["left"], key_initial, key_final, keys)
    


def values(rbt_tree, key_initial, key_final):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (RBT) en el rango dado."""    
    values = sl.new_list()
    values_range(rbt_tree["root"], key_initial, key_final, values)
    return values


def values_range(root, key_initial, key_final, values):
    """Agrega a 'values' todos los valores entre key_initial y key_final (inclusive)."""    
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, values)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(values, root["value"])
    if key_final > root["key"]:
        values_range(root["right"], key_initial, key_final, values)

        


def default_compare(key, entry):
    """Compara dos llaves."""    
    if key == bn.get_key(entry):
      return 0
    elif key > bn.get_key(entry):
      return 1
    return -1