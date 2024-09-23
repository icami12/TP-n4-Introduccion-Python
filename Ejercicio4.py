# lista de sucursales, cada una con su nombre y una lista de instrumentos a la venta. 
# Instrumento (ID alfanumérico, precio y tipo (Percusión, Viento o Cuerda)
tipoInstrumento = ["percusion", "viento", "cuerda"]

class Instrumento:
    def __init__(self, id, precio, tipo) -> None:
        self.id = id
        self.validacionPrecio(precio)
        self.validacionTipo(tipo)
        
    def validacionPrecio(self, precio):
        if precio > 0:
            self.precio = precio
        else:
            print("El precio no corresponde como válido.\n")
            self.precio = None
    
    def validacionTipo(self,tipo):
        if tipo.lower() in tipoInstrumento:
            self.tipo = tipo
        else:
            print(f'El tipo {tipo} de instrumento no es válido')
            self.tipo = None
    #Método: Mostrar datos de cada instrumento en la consola.
    def mostrarInfo(self):
        print(f'ID: {self.id}\nPRECIO: {self.precio}\nTIPO: {self.tipo}')              

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre.lower()
        self.instrumentos = []
        
    def add_instrumentos(self, instrumento):
        if isinstance(instrumento,Instrumento):
            self.instrumentos.append(instrumento)
        else:
            print(f'Solo se puede agregar instrumentos a la lista de la sucursal {self.nombre}')
            
    #Método listarInstrumentos(): Mostrar todos los datos de cada instrumento en la consola.  
    def listarInstrumentos(self):
        print(f'----Sucursal {self.nombre}----')
        for instrum in self.instrumentos:
            instrum.mostrarInfo()
            print("------------------------")
            
    #Método instrumentosPorTipo(tipo): Devolver una lista de instrumentos cuyo tipo coincida con el parámetro tipo.
    def devolverListaDeinstrumentosPorTipo(self, tipo):
        instrumReturn = []
        tipo = tipo.lower()  # Convierte el tipo a minúsculas una vez para consistencia
        
        if tipo in tipoInstrumento:
            for instrum in self.instrumentos:
                if instrum.tipo.lower() == tipo:
                    instrumReturn.append(instrum)
            if instrumReturn:
                return instrumReturn
            else:
                print(f'No hay instrumentos de ese tipo en la sucursal {self.nombre}.\n')
                return instrumReturn
        else:
            print(f'Ese tipo de instrumento no esta permitido.\n')
            return instrumReturn
        
    #Método borrarInstrumento(id): Recibir un ID y eliminar el instrumento asociado de la sucursal correspondiente.
    def borrarInstrumento(self, id):
        encontrado = False
        for instrum in self.instrumentos:
            if instrum.id == id:
                self.instrumentos.remove(instrum)
                encontrado = True
                break
        if encontrado:
            print(f'\nInstrumento con ID {id} borrado.\n')
        else:
            print(f'\nInstrumento con ID {id} no encontrado.\n')

class Sucursales:
    def __init__(self):
        self.sucursales = []
        
    def add_sucursal(self, sucursal):
        if isinstance(sucursal,Sucursal):
            self.sucursales.append(sucursal)
        else:
            print('No es una instancia Sucursal.\n')
              
    #Método porcInstrumentosPorTipo(sucursal): Recibir el nombre de una sucursal y retornar los porcentajes de instrumentos por tipo.
    def porcInstrumentosPorTipo(self, nameSucursal):
        dicPorcentajesInstrumentos = {"percusion":0, "viento":0, "cuerda":0}
        total_instrumentos = 0
        sucursal_encontrada = False
        
        for sucursal in self.sucursales:
            if sucursal.nombre.lower() == nameSucursal.lower():
                sucursal_encontrada = True
                for instrumento in sucursal.instrumentos:
                    if instrumento.tipo == "percusion":
                        dicPorcentajesInstrumentos["percusion"] += 1
                    elif instrumento.tipo == "viento":
                        dicPorcentajesInstrumentos["viento"] += 1
                    elif instrumento.tipo == "cuerda":
                        dicPorcentajesInstrumentos["cuerda"] += 1
                    total_instrumentos +=1
                
                if total_instrumentos > 0:
                    for tipo, cantidad in dicPorcentajesInstrumentos.items():
                        porcentaje = (cantidad / total_instrumentos) * 100
                        print(f'{tipo.capitalize()}: {porcentaje:.2f}%')
                else:
                    print(f'No hay instrumentos en la sucursal {sucursal}.\n')
                break
        if not sucursal_encontrada:
            print(f'La sucursal {nameSucursal} no existe.\n')

#sucursal, instrumento y lista de sucursales creada   
sucursalesCatamarca = Sucursales()            
sucursal1 = Sucursal("Centro")
instrum1 = Instrumento("65GH",23544,"viento")
instrum2 = Instrumento("10GF",13544,"percusion")

sucursal1.add_instrumentos(instrum1)
sucursal1.add_instrumentos(instrum2)
sucursal1.listarInstrumentos() #METODO 1: mostrando datos de los instrumentos de la sucursal

#METODO 4: agregando sucursal a lista de sucursales y mostrando %
sucursalesCatamarca.add_sucursal(sucursal1)
print(f'\n--- Porcentajes de instrumentos en la sucursal {sucursal1.nombre} ---')
sucursalesCatamarca.porcInstrumentosPorTipo(sucursal1.nombre)

#METODO 2: devolviendo lista de instrumentos de viento y mostrando sus datos(solo un elemento)
instrumsDeUnTipo = []
instrumsDeUnTipo = sucursal1.devolverListaDeinstrumentosPorTipo("viento") 
print("\nLista de instrumentos del tipo buscado en la sucursal: ")
for instrum in instrumsDeUnTipo:
    instrum.mostrarInfo()

#METODO 3: borrando instrumento de viento y mostrando que se eliminó
sucursal1.borrarInstrumento("65GH")
sucursal1.listarInstrumentos()