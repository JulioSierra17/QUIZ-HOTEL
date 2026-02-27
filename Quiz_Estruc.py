# Julio Sierra 2251503
class nodo:
    def __init__(self, cedula, nombre, habitacion, orden):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion
        self.orden = orden
        self.siguiente = None

class hotel:
    def __init__(self, total_habitaciones):
        self.cabeza = None     # Huéspedes actuales
        self.entradas = None   # Historial total (Libro de entradas)
        self.salidas = None    # Historial de retiros (Libro de salidas)
        self.total_habitaciones = total_habitaciones
        self.contador_llegadas = 0 

    def registro_entrada(self, cedula, nombre, habitacion):
        # Validar si la habitación está ocupada actualmente
        actual = self.cabeza
        while actual:
            if actual.habitacion == habitacion:
                print("La habitación", habitacion, "está ocupada.")
                return
            actual = actual.siguiente

        self.contador_llegadas += 1
        
        # Insertar en lista de huéspedes activos
        nuevo = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        
        # Insertar en libro de entradas (histórico)
        entrada_historial = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        entrada_historial.siguiente = self.entradas
        self.entradas = entrada_historial
        
        print("Entrada registrada: ", nombre, " en habitación ", habitacion)

    def registro_salida(self, cedula):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.cedula == cedula:
                # 1. Registrar en libro de salidas
                nueva_salida = nodo(actual.cedula, actual.nombre, actual.habitacion, actual.orden)
                nueva_salida.siguiente = self.salidas
                self.salidas = nueva_salida
                
                # 2. Eliminar de la lista de activos
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                print("Salida registrada para:", actual.nombre)
                return
            
            anterior = actual
            actual = actual.siguiente
        
        print("No se encontró un registro activo para la cédula:", cedula)

    # Consulta Individual por Cédula
    def consultar_por_cedula(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                print("Huésped:", actual.nombre, "| Habitación:", actual.habitacion)
                return
            actual = actual.siguiente
        print("No se encontró el huésped.")

    # Consulta de Habitaciones Disponibles
    def consultar_disponibles(self):
        print("Habitaciones libres:")
        for i in range(1, self.total_habitaciones + 1):
            ocupada = False
            actual = self.cabeza
            while actual:
                if actual.habitacion == i:
                    ocupada = True
                    break
                actual = actual.siguiente
            if not ocupada:
                print("- Habitación", i)

    # Consulta de Habitaciones Ocupadas
    def consultar_ocupadas(self):
        print("Habitaciones ocupadas:")
        actual = self.cabeza
        if not actual:
            print("No hay habitaciones ocupadas.")
        while actual:
            print("- Habitación", actual.habitacion, "por", actual.nombre)
            actual = actual.siguiente