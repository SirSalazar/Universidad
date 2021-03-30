class Nodo:
    # Constructor: (llave, valor, hijoIzquierdo, hijoDerecho, padre)
    def __init__(self, llave, valor, padre=None, hijoIzquierdo=None, hijoDerecho=None):
        self.llave = llave
        self.valor = valor
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho
        self.padre = padre

    # Retornar el nodo del hijo izquierdo [None cuando no tiene hijo]
    def ObtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    # Asignar el nodo del hijo izquierdo
    def PonerHijoIzquierdo(self, hijo):
        self.hijoIzquierdo = hijo

    # Retornar el nodo del hijo derecho [None cuando no tiene hijo]
    def ObtenerHijoDerecho(self):
        return self.hijoDerecho

    # Asignar el nodo del hijo derecho
    def PonerHijoDerecho(self, hijo):
        self.hijoDerecho = hijo

    # Validar sí el nodo es raíz
    def EsNodoRaiz(self):
        return not self.padre

    # Validar sí el nodo es hoja
    def EsNodoHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)

class ArbolBinario:
    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.raiz = None
        self.peso = 0

    def ObtenerPeso(self):
        return self.peso

    def AgregarNodo(self, llave, valor):
        if self.raiz != None:
            # agregar nodo nuevo al árbol
            self._AgregarNodo(llave, valor, self.raiz)
        else:
            # agregar el nuevo nodo como raíz
            self.raiz = Nodo(llave, valor)
            print("El nodo ", llave, " se ha agregado como raiz con un valor de:", valor)

    def _AgregarNodo(self, llave, valor, nodo):
        # verificar sí es menor o mayor para ir por la izq o derecha respectivamente
        if (valor < nodo.valor):
            if (nodo.ObtenerHijoIzquierdo()):  # verifica si tiene hijo izq
                # se llama recursivamente al hijo implicado
                self._AgregarNodo(llave, valor, nodo.ObtenerHijoIzquierdo())
            else:
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(llave, valor, nodo)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                print("Se ha agregado como hijo izquierdo de ", nodo.llave, " a ", nuevoNodo.llave, " con un valor de", valor, "y un padre :", nodo.valor)
        else:
            if (valor > nodo.valor):
                if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                    # se llama recursivamente al hijo implicado
                    self._AgregarNodo(llave, valor, nodo.ObtenerHijoDerecho())
                else:
                    # se crea un nuevo nodo y se asigna como hijo
                    nuevoNodo = Nodo(llave, valor, nodo)
                    nodo.PonerHijoDerecho(nuevoNodo)
                    print("Se ha agregado como hijo derecho de ", nodo.llave, " a ", nuevoNodo.llave, "con un valor de", valor, "y un padre:", nodo.valor)

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo):
        if (nodo):
            print(nodo.valor)
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho())

    # In-order (I-R-D)
    def imprimir_in_order(self, nodo):
        if (nodo):
            self.imprimir_in_order(nodo.ObtenerHijoIzquierdo())
            print(nodo.valor)
            self.imprimir_in_order(nodo.ObtenerHijoDerecho())

    # Post-order (I-D-R)
    def imprimir_post_order(self, nodo):
        if (nodo):
            self.imprimir_post_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_post_order(nodo.ObtenerHijoDerecho())
            print(nodo.valor)

    def buscarNodo(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodo(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodo(self, busqueda, nodo):
        if not nodo:
            return None
        if (busqueda == nodo.valor):
            return nodo
        else:
            if (busqueda < nodo.valor):
                return self._buscarNodo(busqueda, nodo.ObtenerHijoIzquierdo())
            else:
                return self._buscarNodo(busqueda, nodo.ObtenerHijoDerecho())

#4- Se debe implementar en código Python un método para buscar un nodo específico, y cuando se encuentre
#debe mostrar el recorrido desde la raíz hasta dicho nodo.

    def rutaBusqueda(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return (self._rutaBusqueda(busqueda, self.raiz, []))
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _rutaBusqueda(self, busqueda, nodo, ruta):
        if not nodo:
            return None
        if (busqueda == nodo.valor):
            ruta.append(nodo.valor)
            return ruta
        else:
            if (busqueda < nodo.valor):
                ruta.append(nodo.valor)
                return self._rutaBusqueda(busqueda, nodo.ObtenerHijoIzquierdo(), ruta)
            else:
                ruta.append(nodo.valor)
                return self._rutaBusqueda(busqueda, nodo.ObtenerHijoDerecho(), ruta)
#5- Un triada de primos, es aquel conjunto de números primos que se encuentran en 3 nodos diferentes
#estrechamente relacionados (un padre y sus dos hijos). Se necesita implementar un método que permita
#identificar todas las triadas de primos que se encuentran en un árbol dado.

    def es_primo(nodo):          #Metodo que verifica si un numero es primo
        for n in range(2, nodo.valor):
            if nodo.valor % n == 0:
                return False
        return True

    def buscarTriada(self, nodo):
        if (nodo):
            if (nodo.ObtenerHijoDerecho()):
                if (nodo.ObtenerHijoIzquierdo()):
                    print("El nodo con el valor", nodo.valor, "y sus dos hijos son primos")
            else:
                print("no tiene hijos")
            #print(nodo.valor)
            #self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            #self.imprimir_pre_order(nodo.ObtenerHijoDerecho())



abb = ArbolBinario()
abb.AgregarNodo("A", 57)
abb.AgregarNodo("B", 34)
abb.AgregarNodo("C", 23)
abb.AgregarNodo("D", 12)
abb.AgregarNodo("E", 7)
abb.AgregarNodo("F", 5)
abb.AgregarNodo("G", 10)
abb.AgregarNodo("H", 44)
abb.AgregarNodo("I", 37)
abb.AgregarNodo("J", 70)
"""
abb.AgregarNodo("K", 85)
abb.AgregarNodo("L", 100)
abb.AgregarNodo("M", 65)
abb.AgregarNodo("N", 81)
abb.AgregarNodo("O", 92)
abb.AgregarNodo("P", 245)
abb.AgregarNodo("Q", 77)
abb.AgregarNodo("R", 61)
abb.AgregarNodo("S", 59)
abb.AgregarNodo("T", 999)
abb.AgregarNodo("U", 1)
abb.AgregarNodo("V", 9)
abb.AgregarNodo("W", 3)
abb.AgregarNodo("X", 8)"""

print("------------ 4 -------------")
busqueda = 8
resultado = abb.rutaBusqueda(busqueda)
print("La ruta para llegar al nodo con valor", busqueda, "es:",  resultado)

print("------------ 5 -------------")
abb.buscarTriada(abb.raiz)