# Julio Sierra 2251503
class nodo:
    def __init__(self,cedula,nombre,habitacion,orden):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion
        self.orden = orden
        self.siguiente = None

class hotel:
    def __init__ (self, total_habitaciones):
        self.cabeza = None
        self.entrada=None
        self.salidas=None
        self.total_habitaciones = total_habitaciones
        self.habitaciones_ocupadas = total_habitaciones
        self.contador_llegadas=0 #contabilizacion de llegadas
        
    def registro_entrada(self, cedula, nombre, habitacion):
        if self.habitaciones_ocupadas(habitacion):
            print("La habitación", habitacion, "está ocupada. Por favor, elija otra habitación :).")
            return
        self.contador_llegadas+=1
        nuevo=nodo(cedula,nombre,habitacion,self.contador_llegadas)
        nuevo.siguiente=self.activos
        self.activos=nuevo
        entrada=nodo(cedula,nombre,habitacion,self.contador_llegadas)
        entrada.siguiente=self.entradas
        self.entradas=entrada
        print("Se registro de manera exitosa la entrada para:", nombre, "en la habitación", habitacion)
     
    def registro_salida(self,cedula):
            actual = self.cabeza
            anterior= None
            while actual:
                if actual.cedula==cedula:
                    if anterior:
                        anterior.siguiente=actual.siguiente
                    else:
                        self.activos=actual.siguiente
                        salida=nodo(actual.cedula,actual.nombre,actual.habitacion,actual.orden)
                        salida.siguiente=self.salidas
                        self.salidas=salida
                    print("Se registro de manera exitosa la salida para:", actual.nombre, "de la habitación", actual.habitacion)
                    return
                anterior=actual
                actual=actual.siguiente
                print("No se encontró un registro de entrada para este huesped.")

#Para consultar los huespedes activos
    def consultar_por_cedula(self,cedula):
        actual=self.cabeza
        while actual:
            if actual.cedula==cedula:
                print("Cedula:", actual.cedula)
                print("Nombre:", actual.nombre)
                print("Habitacion:", actual.habitacion)
                print("Orden de llegada:", actual.orden)
                return
            actual=actual.siguiente
            print("No se encontró al huesped con la cedula ingresada :C .")
        
    def consultar_por_orden(self,orden):
        actual=self.cabeza
        while actual:
            if actual.orden==orden:
                print("Cedula:", actual.cedula)
                print("Nombre:", actual.nombre)
                print("Habitacion:", actual.habitacion)
                print("Orden de llegada:", actual.orden)
                return
            actual=actual.siguiente
            print("No se encontró al huesped con el orden de llegada ingresado :C .")