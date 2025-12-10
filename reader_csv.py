import csv
from .utils import validar_ruta, rowcount, limpiar_valor
from .filtros import filtrar_por_columna, buscar_coincidencia
import logging

class leercsv: 
    '''
    Lee un archivo e imprime todas sus filas.
    Comportamiento:
        -Lee fila por fila sin cargar todo el archivo en memoria.
        -Filtrado por columna.
        -Valida la ruta.
    '''
    def __init__(self, ruta, separador = ","):
        self.ruta = ruta
        self.separador = separador
        self.filas = []
        self.encabezados = []
        logging.debug(f"Creado LectorCSV(ruta= '{ruta}', separador= '{separador}')")
    
    def validar(self):
        logging.debug(f"Validando ruta: {self.ruta}")
        return validar_ruta(self.ruta)
    def leer(self, max_filas = None):
        '''
        Lee el CSV completo o hasta 'max_filas'.
        Guarda resultados en self.filas.
        '''
        self.validar()
        logging.info(f"Leyendo archivo: {self.ruta}")

        with open(self.ruta, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter= self.separador)
            self.encabezados = reader.fieldnames

            logging.debug(f"Encabezados: {self.encabezados}")

            for i, row in enumerate(reader, start= 1):
                fila_limpio = {k: limpiar_valor(v) for k, v in row.items()}
                self.filas.append(fila_limpio)

                if max_filas and i >= max_filas:
                    break
        logging.info(f"Archivo leidol correctamente. Filas cargadas: {len(self.filas)}")
        return self.filas

    def filtrar(self, columna, valor):
        validar_ruta(self.ruta)
        logging.debug(f"Filtrando por columna '{columna}' == '{valor}'")
        return filtrar_por_columna(columna, valor)
    
    def buscar(self, columna, texto):
        validar_ruta(self.ruta)
        logging.debug(f"Buscando '{texto}' dentro de columna '{columna}'")
        return buscar_coincidencia(columna, texto)
    
    def leer_encabezados(self):
        return self.encabezados
    
    def contar(self):
        return rowcount(self.ruta)
    
        


