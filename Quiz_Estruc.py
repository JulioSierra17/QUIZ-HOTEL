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
        self.cabeza = None
        self.entradas = None
        self.salidas = None
        self.total_habitaciones = total_habitaciones
        self.contador_llegadas = 0 

    # Registro de entrada de huéspedes
    def registro_entrada(self, cedula, nombre, habitacion):
        actual = self.cabeza
        while actual:
            if actual.habitacion == habitacion:
                print("La habitación", habitacion, "está ocupada.")
                return
            actual = actual.siguiente

        self.contador_llegadas += 1
        
        nuevo = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        
        entrada_historial = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        entrada_historial.siguiente = self.entradas
        self.entradas = entrada_historial
        
        print("Entrada registrada:", nombre, "en habitación", habitacion)

    # Registro de salida de huéspedes
    def registro_salida(self, cedula):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.cedula == cedula:
                nueva_salida = nodo(actual.cedula, actual.nombre, actual.habitacion, actual.orden)
                nueva_salida.siguiente = self.salidas
                self.salidas = nueva_salida
                
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                print("Salida registrada para:", actual.nombre)
                return
            
            anterior = actual
            actual = actual.siguiente
        
        print("No se encontró un registro activo para la cédula:", cedula)

    # Consulta individual por cédula
    def consultar_por_cedula(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                print("Cédula:", actual.cedula)
                print("Nombre:", actual.nombre)
                print("Habitación:", actual.habitacion)
                print("Orden de llegada:", actual.orden)
                return
            actual = actual.siguiente
        print("No se encontró el huésped.")

    # Consulta total por cédula
    def consulta_total_por_cedula(self):
        actual_externo = self.cabeza

        while actual_externo:
            menor = None
            actual = self.cabeza

            while actual:
                if actual.cedula >= actual_externo.cedula:
                    if menor is None or actual.cedula < menor.cedula:
                        menor = actual
                actual = actual.siguiente

            if menor:
                print("Cédula:", menor.cedula,
                      "| Nombre:", menor.nombre,
                      "| Habitación:", menor.habitacion,
                      "| Orden:", menor.orden)

            actual_externo = actual_externo.siguiente

    # Consulta total por orden de llegada
    def consulta_total_por_orden(self):
        actual_externo = self.cabeza

        while actual_externo:
            menor = None
            actual = self.cabeza

            while actual:
                if actual.orden >= actual_externo.orden:
                    if menor is None or actual.orden < menor.orden:
                        menor = actual
                actual = actual.siguiente

            if menor:
                print("Orden:", menor.orden,
                      "| Cédula:", menor.cedula,
                      "| Nombre:", menor.nombre,
                      "| Habitación:", menor.habitacion)

            actual_externo = actual_externo.siguiente

    # Consulta de habitaciones disponibles
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

    # Consulta de habitaciones ocupadas
    def consultar_ocupadas(self):
        print("Habitaciones ocupadas:")
        actual = self.cabeza
        if not actual:
            print("No hay habitaciones ocupadas.")
        while actual:
            print("- Habitación", actual.habitacion, "por", actual.nombre)
            actual = actual.siguiente