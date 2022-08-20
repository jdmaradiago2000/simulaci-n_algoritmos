from Queue import Queue
from Printer import Printer
from Task import Task
import random


def simulation(num_seconds, pages_per_minute):
    """Este método simula el comportamiento de las tareas de la impresora.

    Args:
        num_seconds (number): Recibe por parametros el número total de segundos en los cuales se va a realizar la simulación.
        pages_per_minute (number): Recipe por parametro las paginas a imprimir por minuto.
    """

    # Objeto instancia de la Clase Printer y tiene como parametro las paginas por minuto
    lab_printer = Printer(pages_per_minute)

    # Objeto instancia de la Clase Printer
    print_queue = Queue()

    # Segundos de espera que se guardan en un arreglo.
    waiting_times = []

    # Ciclo for que recorre cada unos de los 3600 seg en los cuales se va a realizar la simulación.
    for currentSecond in range(num_seconds):

        # Si se ha creado una nueva tarea de impresión, entonces añada una tarea al final de la cola de impresión.
        if new_print_task():
            task = Task(currentSecond)
            print_queue.enqueue(task)

        # Si la impresora no está ocupada y si la cola de impresión no está vacia, entonces:
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            # Elimine la primera tarea de la cola y guarda el elemento en la variable "next_task"
            next_task = print_queue.dequeue()
            # Agrega a la lista "waiting_times" el tiempo que se tomó en realizar la impresión después de haber entrado a la cola de tareas.
            waiting_times.append(next_task.wait_time(currentSecond))
            # Inicia con una nueva tarea.
            lab_printer.start_next(next_task)

        lab_printer.tick()

    # Variable que guarda el promedio en segundos de los tiempos de espera.
    average_wait = sum(waiting_times)/len(waiting_times)
    # Imprime el promedio de los tiempos de espera y las tareas pendientes.
    print("Average Wait %6.2f secs %d tasks remaining." %
          (average_wait, print_queue.size()))


def new_print_task():
    """Este metodo decide si se ha creado una nueva tarea de impresión.

    Returns:
        boolean: Retorna verdadero o falso dependiendo si el número aleatoria es igual a 180 o no.
    """
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


# Crea un ciclo for en un rango de 0 a 9 y llama al método simulación con el
# tiempo que dure la simulación y el número de paginas a imprimir.
for i in range(10):
    simulation(3600, 5)
