class Printer:  # Aquí se define la clase Printer
    def __init__(self, ppm):
        """Este es el método constructor o inicializador de la clase Printer

        Args:
            ppm (number): Recibe como argumento o parametro las paginas por minutos que va a imprimir la impresora.
        """
        self.page_rate = ppm

        # Tarea actual inicia en que no hay ninguna
        self.current_task = None

        # Cantidad de tiempo restante e inicia en 0 minutos
        self.time_remaining = 0

    def tick(self):
        """Método que asigna una tarea y asigna un tiempo a la variable "time_remaining"
        """
        if self.current_task is not None:  # Verifica la existencia de una tarea
            self.time_remaining = self.time_remaining - 1  # Calcula el tiempo restante
            if self.time_remaining <= 0:  # Verifica, si el tiempo es menor o igual a cero, entonces,
                # A la tarea actual asignele que no hay ninguna tarea.
                self.current_task = None

    def busy(self):
        """Este Método verifica si la impresora está ocupada con una tarea o no.

        Returns:
            boolean: "True" o "False"
        """
        if self.current_task is not None:  # Si existe una tarea, devuelva "True", sino devuelva "False".
            return True
        else:
            return False

    def start_next(self, new_task):
        """Este método inicia una nueva tarea de impresión

        Args:
            new_task (objeto): Es la tarea extraida de la cola 
        """
        self.current_task = new_task  # A la tarea actual, se le asigna la nueva tarea que entra por parametros.
        # El tiempo de espera es igual a al número de páginas de la nueva tarea multiplicado por 60 y dividido entre las paginas por minuto que la impresora puede imprimir.
        self.time_remaining = new_task.get_pages() * 60/self.page_rate
