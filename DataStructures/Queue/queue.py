def new_queue():
    """Crea una nueva cola vacía."""
    queue = {
        "size": 0,
        "elements": []
    }
    return queue


def enqueue(my_queue, element):
    """Agrega un elemento a la cola."""
    my_queue["elements"].append(element)
    my_queue["size"] += 1
    return my_queue


def dequeue(my_queue):
    """Quita un elemento de la cola."""
    if size(my_queue) == 0:
        return None
    element = my_queue["elements"].pop(0)
    my_queue["size"] -= 1
    return element


def peek(my_queue):
    """Devuelve el primer elemento de la cola sin quitarlo."""
    if size(my_queue) == 0:
        return None
    return my_queue["elements"][0]


def is_empty(my_queue):
    """Indica si la cola está vacía."""
    return size(my_queue) == 0


def size(my_queue):
    """Devuelve la cantidad de elementos en la cola."""
    return my_queue["size"]