import logging
import os
import csv

logging.basicConfig(
        level= logging.INFO,
        format= "%(asctime)s [%(levelname)s] %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("lector_csv.log", encoding= "utf-8"),
            logging.StreamHandler()
        ]
    )
def validar_ruta(ruta): 
    '''
    Valida si la ruta es correcta y segura.
    '''
    logging.debug(f"Intentando abrir el archivo: {ruta}")
    if not os.path.isfile(ruta):
        logging.error(f"El archivo {ruta} no existe.")
        raise FileNotFoundError(f"El archivo '{ruta}' no existe.")
    if not ruta.lower().endswith(".csv"):
        logging.error(f"Archivo no es CSV: '{ruta}'")
        raise ValueError("El archivo no es un CSV valido.")
    logging.info(f"Ruta verificada correctamente: {ruta}")
    return True

def limpiar_valor(valor):
    '''
    Limpia el valor en la casilla.
    '''
    if valor is None:
        return ''
    valor = str(valor).strip()

    if valor in ["", "NULL", "None", "N/A", "na"]:
        return ''
    return valor


def rowcount(ruta, separador= ","):
    with open(ruta, encoding= 'utf-8') as f:
        reader = csv.DictReader(f, delimiter= separador)
        total = sum(1 for _ in reader)

    logging.info(f"El archivo '{ruta}' contiene {total} filas.")
    return total

def convert_to_int(valor):
    '''
    Convierte un valor str a int o float.
    '''
    valor = limpiar_valor(valor)
    if valor == "":
        return None
    try:
        if '.' in valor:
            return float(valor)
        return int(valor)
    except:
        logging.warning(f"No se pudoconvertir a numero: {valor}")
        return None
    
def res_CSV(ruta, separador = ","):
    '''
    Genera un resumen del archivo CSV.
    '''
    resumen = {}

    with open(ruta, encoding= 'utf-8') as f:
        reader = csv.DictReader(f, delimiter= separador)
        resumen["columnas"] = reader.fieldnames
        resumen["total_filas"] = sum(1 for _ in reader)

    with open(ruta, encoding= 'utf-8') as f:
        reader = csv.DictReader(f, delimiter= separador)
        resumen["primeras_5"] = [next(reader) for _ in range(5)]

    logging.info(f"Resumen generado para '{ruta}'")

    return resumen
