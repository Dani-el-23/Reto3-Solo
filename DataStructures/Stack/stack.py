from DataStructures.List import list_node as ln

def new_stack():
    """Crea una nueva pila vacía."""
    stack = {
        "first": None,
        "last": None,
        "size": 0
    }
    return stack


def push(my_stack, element):
    """Agrega un elemento a la pila."""
    nodo = ln.new_single_node(element)
    nodo["next"] = my_stack["first"]
    my_stack["first"] = nodo
    my_stack["size"] +=1
    
    if size(my_stack) == 1:
        my_stack["last"] = nodo
        
    return my_stack
        


def pop(my_stack):
    """Quita un elemento de la pila."""
    if size(my_stack) == 0:
        raise Exception('EmptyStructureError: stack is empty')
    
    elemento = my_stack["first"]
    if size(my_stack) == 1:
        my_stack["first"] = None
        my_stack["last"] = None
    else:
        my_stack["first"] = my_stack["first"]["next"]
        
    my_stack["size"] -=1
    
    return elemento["info"]
    
def is_empty(my_stack):
    """Indica si la cola está vacía."""
    return size(my_stack) == 0
    
    
    


def top(my_stack):
    """Devuelve el primer elemento de la cola sin quitarlo."""
    if size(my_stack) == 0:
        raise Exception('EmptyStructureError: stack is empty')
    return my_stack["first"]["info"]





def size(my_stack):
    """Devuelve la cantidad de elementos en la cola."""
    return my_stack["size"]