import random


class Task:  # Aquí se define la clase Task, la cual es la encargada de crear y manipular las tareas.
    def __init__(self, time):
        """Este es le método constructor de la clase "Task"

        Args:
            time (number): Recibe como parametro el minuto donde se ejecuta la tarea en relación al tiempo general de impresión.
        """
        self.timestamp = time
        # Se genera un número aleatorio entre 1 y 21 que es el número de paginas que puede tener una tarea.
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        """Método que obtiene el tiempo en relación a las tareas realizadas.

        Returns:
            number: El minuto en el cual se ejecuta la tarea.
        """
        return self.timestamp

    def get_pages(self):
        """Este método que obtiene la cantidad de páginas que tiene la tarea.

        Returns:
            number: Retorna el número de paginas a imprimir.
        """
        return self.pages

    def wait_time(self, current_time):
        """Este método sirve para obtener el tiempo de espera para imprimir

        Args:
            current_time (number): Se recibe como parametro el minuto en el cual entró la tarea.

        Returns:
            _type_: La resta entre el minuto en el cual se imprimió la tarea y el minuto en el cual ingreso la tarea. 
        """
        return current_time - self.timestamp
