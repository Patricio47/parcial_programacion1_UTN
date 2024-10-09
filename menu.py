def mostrar_menu():
    """Muestra un menu para que el usuario pueda elegir las opciones del sistema"""
    print("""
    Menú:
    1. Cargar pacientes
    2. Mostrar lista de pacientes
    3. Buscar paciente por Historia Clínica
    4. Ordenar pacientes por número de Historia Clínica
    5. Mostrar paciente con más días de internación
    6. Mostrar paciente con menos días de internación
    7. Cantidad de pacientes con días de internación mayor a 5 días
    8. Promedio de días de internación de todos los pacientes
    9. Salir
    """)

def obtener_opcion():
    return input("Seleccione una opcion: ")