class Queue:  # Aquí se define la clase Queue
    def __init__(self):
        """Este es el método constructor o inicializador de la clase Printer
        """
        self.items = []

    def is_empty(self):
        """Es método revisa si la cola está vacia.

        Returns:
           array: Retorna la cola vacia
        """
        return self.items == []

    def enqueue(self, item):
        """Este método añade un elemento al final de la cola.

        Args:
            item: Se debe pasar como parametro el elemento a añadir a la cola.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Este método elimina el primer elemento de la Pila.

        Returns:
            item: Retorna el elemento eliminado  
        """
        return self.items.pop()

    def size(self):
        """Este método verifica el tamaño de la cola y lo retorna.

        Returns:
            Array: Devuelve el tamaño de la cola.
        """
        return len(self.items)
