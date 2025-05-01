from DataStructures.Tree import rbt_node as rn
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al

def new_map():
    """
    Crea un nuevo mapa.
    """
    return {"root": None}

def balance(root):
    """
    Balancea el árbol Red-Black Tree luego de una operación.
    """
    if rn.is_red(root["right"]) and not rn.is_red(root["left"]):
        root = rotate_left(root)
    if rn.is_red(root["left"]) and rn.is_red(root["left"]["left"]):
        root = rotate_right(root)
    if rn.is_red(root["left"]) and rn.is_red(root["right"]):
        root = flip_colors(root)

    return root

    

def put(rbt_tree, key, value):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (RBT). Si la llave ya existe, se actualiza el value del nodo."""
    node = insert_node(rbt_tree["root"], key, value)
    rbt_tree["root"] = node
    rn.change_color(node,rn.BLACK)
    return rbt_tree


def insert_node(node, key, value):
    """Inserta un nuevo nodo en el árbol binario de búsqueda (RBT). Si la llave ya existe, se actualiza el value del nodo."""
    
    if node is None:
        return rn.new_node(key, value)
    compare = default_compare(key, node)
    if compare < 0:
        node["left"] = insert_node(node["left"], key, value)
    elif compare > 0:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value
    
    node = balance(node)
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return node


def get(rbt_tree, key):
    """Busca un nodo en el árbol binario de búsqueda (RBT) y devuelve su value."""
    return get_node(rbt_tree["root"], key)


def get_node(root, key):
    """Busca un nodo en el árbol binario de búsqueda (RBT) y devuelve el nodo."""
    
    if root is None:
        return None
    elif root["key"] == key:
        return root["value"]
    elif key < root["key"]:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)
    

def remove(rbt_tree, key):
    """Elimina un nodo del árbol binario de búsqueda (RBT)."""    
    node = remove_node(rbt_tree["root"], key)
    rbt_tree["root"] = node
    if rbt_tree["root"] is not None:
        rbt_tree["root"]["color"] = rn.BLACK
    return rbt_tree


def remove_node(root, key):
    if root is None:
        return None

    if default_compare(key, root) < 0:
        if root["left"] is not None:
            if not rn.is_red(root["left"]) and not rn.is_red(root["left"].get("left")):
                root = move_red_left(root)
            root["left"] = remove_node(root["left"], key)
    else:
        if rn.is_red(root["left"]):
            root = rotate_right(root)
        if default_compare(key, root) == 0 and root["right"] is None:
            return None
        if root["right"] is not None:
            if not rn.is_red(root["right"]) and not rn.is_red(root["right"].get("left")):
                root = move_red_right(root)
            if default_compare(key, root) == 0:
                temp = get_min_node(root["right"])
                root["key"] = temp["key"]
                root["value"] = temp["value"]
                root["right"] = remove_node(root["right"], temp["key"])
            else:
                root["right"] = remove_node(root["right"], key)

    root = balance(root)
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root




def contains(rbt_tree, key):
    """Verifica si una llave existe en el árbol binario de búsqueda (RBT)."""    
    return get(rbt_tree, key) is not None


def size(rbt_tree):
    """Devuelve el tamaño del árbol binario de búsqueda (RBT)."""    
    return size_tree(rbt_tree["root"])


def size_tree(root):
    """Devuelve el tamaño del árbol binario de búsqueda (RBT)."""    
    if root is None:
        return 0
    return root["size"]


def is_empty(rbt_tree):
    """Verifica si el árbol binario de búsqueda (RBT) está vacío."""    
    return rbt_tree["root"] is None


def key_set(rbt_tree):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    keys = sl.new_list()
    key_set_tree(rbt_tree["root"], keys)
    return keys

def key_set_al(rbt_tree):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    keys = al.new_list()
    key_set_tree_al(rbt_tree["root"], keys)
    return keys

def key_set_tree(root, keys):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    if root is not None:
        key_set_tree(root["left"], keys)
        sl.add_last(keys, root["key"])
        key_set_tree(root["right"], keys)
        
def key_set_tree_al(root, keys):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    if root is not None:
        key_set_tree_al(root["left"], keys)
        al.add_last(keys, root["key"])
        key_set_tree_al(root["right"], keys)
        

def value_set(rbt_tree):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (RBT)."""    
    values = sl.new_list()
    value_set_tree(rbt_tree["root"], values)
    return values


def value_set_tree(root, values):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (RBT)."""    
    if root is not None:
        value_set_tree(root["left"], values)
        sl.add_last(values, root["value"])
        value_set_tree(root["right"], values)
        

def value_set_al(rbt_tree):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (RBT)."""    
    values = al.new_list()
    value_set_tree_al(rbt_tree["root"], values)
    return values


def value_set_tree_al(root, values):
    """Devuelve un conjunto de todos los valores en el árbol binario de búsqueda (RBT)."""    
    if root is not None:
        value_set_tree_al(root["left"], values)
        al.add_last(values, root["value"])
        value_set_tree_al(root["right"], values)
        
def get_min(rbt_tree):
    """Devuelve el nodo con la llave mínima en el árbol binario de búsqueda (RBT)."""    
    return get_min_node(rbt_tree["root"])

def get_min_node(root):
    """Devuelve el nodo con la llave mínima en el árbol binario de búsqueda (RBT)."""    
    if root is None:
        return None
    if root["left"] is None:
        return root["key"]
    return get_min_node(root["left"])


def get_max(rbt_tree):
    """Devuelve el nodo con la llave máxima en el árbol binario de búsqueda (RBT)."""    
    return get_max_node(rbt_tree["root"])


def get_max_node(root):
    """Devuelve el nodo con la llave máxima en el árbol binario de búsqueda (RBT)."""    
    if root is None:
        return None
    if root["right"] is None:
        return root["key"]
    return get_max_node(root["right"])


def delete_min(rbt_tree):
    """Elimina el nodo con la llave mínima en el árbol binario de búsqueda (RBT)."""    
    rbt_tree["root"] = delete_min_node(rbt_tree["root"])
    if rbt_tree["root"] is not None:
        rbt_tree["root"]["color"] = rn.BLACK
    return rbt_tree


def delete_min_node(root):
    """Elimina el nodo con la llave mínima en el árbol binario de búsqueda (RBT)."""    
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_node(root["left"])
    root = balance(root)
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def delete_max(rbt_tree):
    """Elimina el nodo con la llave máxima en el árbol binario de búsqueda (RBT)."""    
    rbt_tree["root"] = delete_max_node(rbt_tree["root"])
    if rbt_tree["root"] is not None:
        rbt_tree["root"]["color"] = rn.BLACK
    return rbt_tree


def delete_max_node(root):
    """Elimina el nodo con la llave máxima en el árbol binario de búsqueda (RBT)."""    
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_node(root["right"])
    root = balance(root)
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def floor(rbt_tree, key):
    """Devuelve la llave más grande menor o igual a la llave dada."""    
    return floor_key(rbt_tree["root"], key)


def floor_key(root, key):
    """Devuelve la llave más grande menor o igual a la llave dada."""    
    if root is None:
        return None
    compare = default_compare(key, root)
    if compare == 0:
        return root["key"]
    if compare < 0:
        return floor_key(root["left"], key)
    
    right_floor = floor_key(root["right"], key)
    if right_floor is not None:
        return right_floor
    return root["key"]


def ceiling(rbt_tree, key):
    """Devuelve la llave más pequeña mayor o igual a la llave dada."""    
    return ceiling_key(rbt_tree["root"], key)


def ceiling_key(root, key):
    """Devuelve la llave más pequeña mayor o igual a la llave dada."""    
    if root is None:
        return None
    compare = default_compare(key, root)
    if compare == 0:
        return root["key"]
    if compare > 0:
        return ceiling_key(root["right"], key)
    
    left_ceiling = ceiling_key(root["left"], key)
    if left_ceiling is not None:
        return left_ceiling
    return root["key"]


def select(rbt_tree, k):
    """Devuelve la llave del nodo en la posición k."""    
    return select_key(rbt_tree["root"], k)


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


def rank(rbt_tree, key):
    """Devuelve el número de llaves menores que la llave dada."""    
    return rank_keys(rbt_tree["root"], key)


def rank_keys(root, key):
    """Devuelve el número de llaves menores que la llave dada."""    
    if root is None:
        return 0
    compare = default_compare(key, root)
    if compare < 0:
        return rank_keys(root["left"], key)
    elif compare > 0:
        return 1 + size_tree(root["left"]) + rank_keys(root["right"], key)
    return size_tree(root["left"])
    
    

def height(rbt_tree):
    """Devuelve la altura del árbol binario de búsqueda (RBT)."""    
    return height_tree(rbt_tree["root"])


def height_tree(root):
    """Devuelve la altura del árbol binario de búsqueda (RBT)."""    
    
    count = 0
    if root is None:
        return count
    else:
        if rn.is_red(root) == False:
            count = 1
        h_i = height_tree(root["left"])
        h_d = height_tree(root["right"])
        
        return count + max(h_i, h_d)
    
    
    # if root is None:
    #     return 0
    # left_height = height_tree(root["left"])
    # right_height = height_tree(root["right"])
    # if root["color"] == rn.BLACK:
    #     return 1 + max(left_height, right_height)
    # return max(left_height, right_height)

def keys(rbt_tree, key_initial, key_final):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    keys = sl.new_list()
    keys_range(rbt_tree["root"],key_initial, key_final, keys)
    return keys


def keys_range(root, key_initial, key_final, values):
    """Devuelve un conjunto de todas las llaves en el árbol binario de búsqueda (RBT)."""    
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, values)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(values, root["value"])
    if key_final > root["key"]:
        values_range(root["right"], key_initial, key_final, values)
    


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
    # print(entry)
    if key == rn.get_key(entry):
        return 0
    elif key > rn.get_key(entry):
        return 1
    return -1

def rotate_left(node):
    """Realiza una rotación a la izquierda en el nodo."""    
    new_root = node["right"]
    node["right"] = new_root["left"]
    new_root["left"] = node
    if not (rn.is_red(new_root) and rn.is_red(new_root["left"])):
        new_root = flip_node_color(new_root)
        new_root["left"] = flip_node_color(new_root["left"])
    return new_root

def rotate_right(node):
    """Realiza una rotación a la derecha en el nodo."""    
    new_root = node["left"]
    node["left"] = new_root["right"]
    new_root["right"] = node
    new_root = flip_node_color(new_root)
    new_root["right"] = flip_node_color(new_root["right"])
    return new_root

def flip_node_color(node):
    """Cambia el color de un nodo."""    
    if node["color"] == rn.RED:
        rn.change_color(node, rn.BLACK)
    else:
        rn.change_color(node, rn.RED)
    return node

def flip_colors(node):
    """Cambia el color de los nodos."""    
    if node["left"] is not None:
        node["left"] = flip_node_color(node["left"])
    if node["right"] is not None:
        node["right"] = flip_node_color(node["right"])
    node = flip_node_color(node)
    return node

def move_red_left(node):
    """
    Prepara el nodo para moverse hacia la izquierda durante una eliminación.
    Hace que el hijo izquierdo tenga un nodo rojo.
    """
    flip_colors(node)
    if rn.is_red(node["right"]["left"]):
        node["right"] = rotate_right(node["right"])
        node = rotate_left(node)
        flip_colors(node)
    return node


def move_red_right(node):
    """
    Prepara el nodo para moverse hacia la derecha durante una eliminación.
    Hace que el hijo derecho tenga un nodo rojo.
    """
    flip_colors(node)
    if rn.is_red(node["left"]["left"]):
        node = rotate_right(node)
        flip_colors(node)
    return node

