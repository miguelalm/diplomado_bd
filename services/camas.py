
from database.models import cambiar_cama_paciente, crear_habitacion, crear_cama, obtener_numero_camas

def cambiar_cama():
    rut = input("Ingrese RUT de paciente: ")
    nueva_cama_id = input("Ingrese ID de nueva cama: ")
    cambiar_cama_paciente(rut, nueva_cama_id)
    print("Cama actualizada con éxito.")

def crear_habitacion_y_camas():
    num = input("Número de nueva habitación: ")
    crear_habitacion(num)
    camas = int(input("¿Cuántas camas se deben crear en habitación? "))
    for i in range(camas):
        crear_cama(i + 1, num)
    print("Habitación y camas creadas con éxito.")

def crear_camas_en_habitación():
    habitacion = input("ID de habitación: ")
    camas = int(input("¿Cuántas camas se agregan a esta habitación? "))
    try:
        num_camas = obtener_numero_camas(habitacion)
    except Exception as e:
        print(f"Ocurrió un error al buscar habitación: {e}")
        return
    for i in range(num_camas, num_camas + camas):
        crear_cama(i + 1, habitacion)
    print("Camas creadas con éxito.")