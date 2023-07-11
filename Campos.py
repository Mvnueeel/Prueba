import os

def ComprarDepartamento():
     print("Ingrese el rut del comprador sin guion ni puntos: ", )
     for i in range(4):
	     for j in range(5):
			    if(j<4):
				     if(j==0):
					     print("Rut:",matriz[j,i])
Precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
departamentos = []
for piso in range(1, 11):
    for tipo, precio in precios.items():
        departamentos.append(Departamento(tipo, piso, precio))
    
def MostrarDepartamentosDisponibles():
    print("Mostrando departamentos disponibles para su compra")
    for d in self.departamentos:
            estado = 'disponible' if d.disponible else f'vendido a {d.comprador}'
            print(f'Departamento {d.tipo}{d.piso} - {estado}')

def lista_compradores(self):
        for comprador in sorted(self.compradores):
            print(comprador)

def ventas_totales(self):
        total = sum(d.precio for d in self.departamentos if not d.disponible)
        print(f'Las ganancias totales son {total} UF')
