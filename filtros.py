import csv
import logging

def filtrar_por_columna(ruta, columna, valor, separador= ','):
    '''
    Docstring for leercsv
    Filtra las filas donde 'columna' == 'valor'
    
    Parametros:
        ruta: Ruta del archivo.
        columna: Nombre de la columna por la que se filtra.
        valor: Valor que debe coincidir.
        separador: Caracter separador valido.
    ''' 
    with open(ruta, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter= separador)
        encontrado = False
        for row in reader:
            if row.get(columna) == valor:
                logging.debug(f"EL valor se ha encontrado: {row}")
                encontrado = True
        if not encontrado:
            logging.error(f"No se encontraron coincidencias del valor: {valor}")
    
def buscar_coincidencia(ruta, columna, texto, separador= ","):
    '''
    Docstring for buscar_coincidencia
    Busca coincidencias parciales:
    Si texto= "an" puede coincidir con "Ana", "Andres", "Sanchez".
    
    ruta: Ruta del archivo.
    columna: Nombre de la columna.
    texto: valor de busqueda de coincidencia.
    separador: denotador de separacion en el archivo CSV.
    '''

    resultados = []
    texto = texto.lower()

    with open(ruta, newline= '', encoding= 'utf-8') as f:
        reader = csv.DictReader(f, delimiter= separador)

        if columna not in reader.fieldnames:
            raise ValueError(f"La columna '{columna}' no existe en el archivo.")
        
        for row in reader:
            if texto in row[columna].lower():
                resultados.append(row)

    return resultados


