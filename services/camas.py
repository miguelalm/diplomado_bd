
from database.models import cambiar_cama_paciente, crear_habitacion, crear_cama

def cambiar_cama():
    rut = input("Ingrese el RUT del paciente: ")
    nueva_cama_id = input("Ingrese el ID de la nueva cama: ")
    cambiar_cama_paciente(rut, nueva_cama_id)
    print("Cama actualizada con éxito.")

def crear_habitacion_y_camas():
    num = input("Número de la nueva habitación: ")
    crear_habitacion(num)
    camas = int(input("¿Cuántas camas quieres crear en esta habitación? "))
    for i in range(camas):
        crear_cama(i + 1, num)
    print("Habitación y camas creadas con éxito.")
