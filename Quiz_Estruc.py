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
        
    def registro_entrada(self, cedula, nombre, habitacion):
        if habitacion < 1:
            print("Error: El número de habitación no puede ser menor a 1.")
            return
        if habitacion > self.total_habitaciones:
            print("Error: El hotel solo tiene", self.total_habitaciones, "habitaciones.")
            return

        actual = self.cabeza
        while actual:
            if actual.habitacion == habitacion:
                print("La habitación", habitacion, "ya se encuentra ocupada por otro cliente.")
                return
            actual = actual.siguiente
        
        print("Habitación disponible. Procediendo con el registro...")
        self.contador_llegadas = self.contador_llegadas + 1
        
        nuevo = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        
        historial = nodo(cedula, nombre, habitacion, self.contador_llegadas)
        historial.siguiente = self.entradas
        self.entradas = historial
        
        print("Registro completado con éxito.")
        print("Huésped:", nombre, "| Cédula:", cedula, "| Habitación:", habitacion)
     
    def registro_salida(self, cedula):
        print("Buscando registro de salida para la cédula:", cedula)
        actual = self.cabeza
        anterior = None
        encontrado = False
        
        while actual:
            if actual.cedula == cedula:
                encontrado = True
                print("Huésped localizado. Generando registro en el libro de salidas...")
                
                salida = nodo(actual.cedula, actual.nombre, actual.habitacion, actual.orden)
                salida.siguiente = self.salidas
                self.salidas = salida

                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                print("El huésped", actual.nombre, "ha dejado la habitación", actual.habitacion)
                return
            
            anterior = actual
            actual = actual.siguiente
        
        if encontrado == False:
            print("No se encontró ningún registro activo con esa cédula en el hotel.")

    def consulta_individual(self, cedula):
        print("Consultando información individual del cliente...")
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                print("Nombre Completo:", actual.nombre)
                print("Número de Cédula:", actual.cedula)
                print("Número de Habitación:", actual.habitacion)
                print("Turno de Llegada:", actual.orden)
                return
            actual = actual.siguiente
        print("Error: El cliente con cédula", cedula, "no está registrado actualmente :).")

    def consulta_total_orden(self):
        actual = self.cabeza
        if actual == None:
            print("El hotel se encuentra vacío en este momento.")
            return
            
        print("Listado de Huéspedes Vigentes:")
        while actual:
            print("Orden:", actual.orden)
            print("Nombre:", actual.nombre)
            print("Cédula:", actual.cedula)
            print("Habitación:", actual.habitacion)
            actual = actual.siguiente
        print("Fin del reporte.")

    def consulta_total_cedula(self):
        actual_externo = self.cabeza
        if actual_externo == None:
            print("No hay datos para mostrar.")
            return

        while actual_externo:
            menor_nodo = None
            recorrido = self.cabeza
            while recorrido:
                if recorrido.cedula >= actual_externo.cedula:
                    if menor_nodo == None or recorrido.cedula < menor_nodo.cedula:
                        menor_nodo = recorrido
                recorrido = recorrido.siguiente
            
            if menor_nodo:
                print("Cédula:", menor_nodo.cedula, "| Huésped:", menor_nodo.nombre, "| Habitación:", menor_nodo.habitacion)
            
            actual_externo = actual_externo.siguiente
        print("Reporte finalizado.")

    def consultar_disponibles(self):
        habitaciones_libres = 0
        for i in range(1, self.total_habitaciones + 1):
            esta_ocupada = False
            temp = self.cabeza
            while temp:
                if temp.habitacion == i:
                    esta_ocupada = True
                    break
                temp = temp.siguiente
            
            if esta_ocupada == False:
                print("La habitación número", i, "está LIBRE.")
                habitaciones_libres = habitaciones_libres + 1
        
        print("Total de habitaciones disponibles:", habitaciones_libres)

    def consultar_ocupadas(self):
        actual = self.cabeza
        if actual == None:
            print("No hay habitaciones ocupadas en este momento.")
            return
            
        while actual:
            print("Habitación:", actual.habitacion)
            print("  -> Nombre:", actual.nombre)
            print("  -> Cédula:", actual.cedula)
            print("  -> Orden:", actual.orden)
            actual = actual.siguiente