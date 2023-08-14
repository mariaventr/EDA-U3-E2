class Nodo:
    __valor=int
    __siguiente=None
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None

    def getValor(self):
        return self.__valor
    
    def setSiguiente(self, objeto):
        self.__siguiente=objeto

    def getSiguiente(self):
        return self.__siguiente

class PilaEnlazada:
    __tope= None
    def __init__(self):
        self.__tope = None

    def vacio(self):
        return self.__tope is None

    def insertar(self, valor):
        nueva_celda = Nodo(valor)
        nueva_celda.setSiguiente(self.__tope)
        self.__tope = nueva_celda

    def eliminar(self):
        if self.vacio():
            print("La pila está vacía. No se puede realizar pop.")
            return None
        valor = self.__tope.getValor()
        self.__tope = self.__tope.getSiguiente()
        return valor

    def mostrar(self):
        if self.vacio():
            print("La pila está vacía.")
        else:
            celda_actual = self.__tope
            while celda_actual:
                print(celda_actual.getValor())
                celda_actual = celda_actual.getSiguiente()

def decimal_a_binario(decimal):
    pila = PilaEnlazada()
    
    while decimal > 0:
        residuo = decimal % 2
        pila.insertar(residuo)
        decimal //= 2

    if pila.vacio():
        return "0"
    
    binario = ""
    while not pila.vacio():
        binario += str(pila.eliminar())
    
    return binario

# Ejemplo de uso
numero_decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero_decimal)
print("El número decimal", numero_decimal, "en binario es:", binario)


        
