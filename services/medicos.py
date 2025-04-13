
from database.models import cambiar_medico_paciente

def cambiar_medico():
    rut = input("Ingrese el RUT del paciente: ")
    nuevo_medico_id = input("Ingrese el ID del nuevo médico: ")
    cambiar_medico_paciente(rut, nuevo_medico_id)
    print("Médico actualizado con éxito.")
