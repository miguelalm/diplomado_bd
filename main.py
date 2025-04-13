
from services import pacientes, camas, medicos

def menu():
    while True:
        print("\n--- Menú Clínica ---")
        print("1. Mostrar pacientes")
        print("2. Mostrar detalle de paciente")
        print("3. Cambiar paciente de cama")
        print("4. Cambiar paciente de médico")
        print("5. Crear habitaciones y camas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pacientes.mostrar_pacientes()
        elif opcion == "2":
            pacientes.mostrar_detalle_paciente()
        elif opcion == "3":
            camas.cambiar_cama()
        elif opcion == "4":
            medicos.cambiar_medico()
        elif opcion == "5":
            camas.crear_habitacion_y_camas()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
