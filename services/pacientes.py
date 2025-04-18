
from database.models import traer_pacientes, traer_detalle_paciente_por_rut

def mostrar_pacientes():
    pacientes = traer_pacientes()
    for p in pacientes:
        print(f"RUT: {p[0]}, Nombre: {p[1]}, Diagnóstico: {p[2]}, Médico: {p[3]}, Habitación: {p[4]}, Cama: {p[5]}")

def mostrar_detalle_paciente():
    rut = input("Ingrese RUT de paciente: ")
    detalle = traer_detalle_paciente_por_rut(rut)
    if detalle:
        print(f"\nRUT: {detalle[0]}")
        print(f"Nombre: {detalle[1]}")
        print(f"Diagnóstico: {detalle[2] or 'N/A'}")
        print(f"Médico: {detalle[3] or 'N/A'}")
        print(f"Último examen: {detalle[4] or 'N/A'}")
        print(f"Habitación: {detalle[5] or 'N/A'}")
        print(f"Cama: {detalle[6] or 'N/A'}")
    else:
        print("Paciente no encontrado.")
