import numpy as np 
import os
import Campos as va 
def ingresar_datos():
    for c in range(8):
        run=va.validacion_nombre()
        matriz[0,c]=run
class CasaFeliz:
    def __init__(self):
        self.departamentos = []
        self.compradores = []
        self.pisos = 10
        self.departamentos_por_piso = 4
        self.matriz_departamentos = [[None] * self.departamentos_por_piso for _ in range(self.pisos)]

    def comprar_departamento(self, comprador):
        self.mostrar_departamentos_disponibles()
        piso = int(input("Ingrese el piso del departamento: "))
        numero = int(input("Ingrese el número del departamento: "))

       
        if self.matriz_departamentos[piso - 1][numero - 1] is None:
            self.matriz_departamentos[piso - 1][numero - 1] = comprador
            self.compradores.append(comprador)
            print("Departamento comprado con éxito.")
        else:
            print("El departamento seleccionado ya ha sido comprado.")

    def mostrar_departamentos_disponibles(self):
        print("Departamentos disponibles:")
        for piso in range(self.pisos):
            for numero in range(self.departamentos_por_piso):
                if self.matriz_departamentos[piso][numero] is None:
                    print(f"Piso {piso+1}, Número {numero+1}")

    def ver_lista_de_compradores(self):
        print("Lista de compradores:")
        for comprador in self.compradores:
            print(comprador)

    def mostrar_ganancias_totales(self):
        ganancias = len(self.compradores)
        print(f"Ganancias totales: ${ganancias}")

    def salir():
       print("¡Gracias por su compra! ")
       print(" Manuel Campos, 11/07/2023  ")

    while(True):
            print("---- Menú ----")
            print("1. Comprar departamento")
            print("2. Mostrar departamentos disponibles")
            print("3. Ver lista de compradores")
            print("4. Mostrar ganancias totales")
            print("5. Salir")

            opcion = int(input("Ingrese una opción: "))

            if opcion=="1":
               comprar_departamento()
            elif opcion=="2":
               mostrar_departamentos_disponibles()
            elif opcion=="3":
               ver_lista_de_compradores()
            elif opcion=="4":
               mostrar_ganancias_totales()
            elif opcion=="5":
               salir()
            else:
                print("Opción inválida. Intente nuevamente.")


