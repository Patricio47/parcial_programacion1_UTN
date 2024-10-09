pacientes = []

def cargar_pacientes(pacientes):
    """Permite al usuario ingresar los datos de los pacientes, almacenando la informacion
    en una lista anidada y la cantidad de pacientes a ingresar lo determina el usuario. """
    cantidad = int(input("Ingrese la cantidad de pacientes a cargar: "))
    for _ in range(cantidad):
        numero_historia = int(input("Numero de historia clinica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnostico: ")
        dias_internacion = int(input("Cantidad de dias de internacion: "))
        pacientes.append([numero_historia,nombre,edad,diagnostico,dias_internacion])
    
def mostrar_pacientes(pacientes):
    """Imprime por pantalla todos los datos del paciente almacenado"""
    if not pacientes:
        print("No hay pacientes registrados: ")
    else:
        for paciente in pacientes:
            print(f"Numero de historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad{paciente[2]}, diagnostico: {paciente[3]}, dias de internacion: {paciente[4]}")

def buscar_paciente(pacientes):
    """Busca en la lista pacientes por el numero de historia clinica y muestra todos los datos.
    Si no se encuentra el paciente, imprime 'paciente no encontrado'"""
    numero_historia = int(input("Ingrese el numero de historia de clinica del paciente: "))
    for paciente in pacientes:
        if paciente[0] == numero_historia:
            print(f"Numero de historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad: {paciente[2]}, diagnostico: {paciente[3]}, dias de internacion: {paciente[4]}")
    print("paciente no encontrado.")

def ordenar_pacientes(pacientes):
    """Ordena la lista de pacientes por el numero de historia clinica en forma ascendente,
    utilizando el algoritmo de burbuja"""
    n = len(pacientes)        
    if n > 0:
        for i in range(n-1):
            for j in range(0, n-i-1):
                if pacientes[j][0] > pacientes[j+1][0]:
                    pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    print("Pacientes ordenados.")
    
    for paciente in pacientes:
        print(f"Numero de historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad: {paciente[2]}, diagnostico: {paciente[3]}, dias de internacion: {paciente[4]}")

def pacientes_mas_dias(pacientes):
    """Calcula e imprime el paciente con mas dias de internacion, mostrando sus datos completos """
    if not pacientes:
        print("No hay pacientes registrados")
    else:
        pacientes_max = pacientes[0]
        for paciente in pacientes:
            if paciente[4] > pacientes_max[4]:
                pacientes_max = paciente
        print(f"Paciente con mas dias de internacion es: {pacientes_max}")

def paciente_menos_dias(pacientes):
    """Calcula e imprime el paciente con menos dias de internacion, mostrando sus datos completos """
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        paciente_min = pacientes[0]
        for paciente in pacientes:
            if paciente[4] < paciente_min[4]:
                paciente_min = paciente
        print(f"Paciente con menos dias de internacion es: {paciente_min}")

def cantidad_pacientes_mas_5_dias(pacientes):
    """Recorre la lista de pacientes y cuenta cuantos pacientes tienen mas de 5 dias de internacion"""
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        contador_pacientes = 0
        for paciente in pacientes:
            if paciente[4] > 5:
                contador_pacientes +=1
        print(f"cantidad de pacientes con mas de 5 dias de internacion: {contador_pacientes}")

def promedio_dias_internacion(pacientes):
    """Calcula el promedio de dias de internacion de todos los pacientes registrados"""
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        total_dias = 0
        for paciente in pacientes:
            total_dias += paciente[4]
        promedio = total_dias / len(pacientes)
        print(f"Promedio de dias de internacion de todos los pacientes {promedio:2f}")