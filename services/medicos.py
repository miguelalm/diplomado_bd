
from database.models import cambiar_medico_paciente

def cambiar_medico():
    rut = input("Ingrese RUT de paciente: ")
    nuevo_medico_id = input("Ingrese ID de nuevo médico: ")
    cambiar_medico_paciente(rut, nuevo_medico_id)
    print("Médico actualizado con éxito.")
