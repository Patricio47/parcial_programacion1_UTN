import os
os.system("cls")
from pacientes import *
from menu import *

def main():
    """La funcion principal que ejecuta el menu interactivo"""
    opcion = None
    while opcion != "6":
        mostrar_menu()
        opcion = obtener_opcion()
        match opcion:
            case "1":
                cargar_pacientes(pacientes)
            case "2":
                mostrar_pacientes(pacientes)
            case "3":
                buscar_paciente(pacientes)
            case "4":
                ordenar_pacientes(pacientes)
            case "5":
                pacientes_mas_dias(pacientes)
            case "6":
                paciente_menos_dias(pacientes)
            case "7":
                cantidad_pacientes_mas_5_dias(pacientes)
            case "8":
                promedio_dias_internacion(pacientes)
            case "9":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opcion no valida, intente de nuevo. ")

main()
