import argparse
import csv
import time
from datetime import datetime
vauxi=''


def procesarcheques(archivocsv,dnicliente, tipocheque, estado=None, rangofecha=None):
    cheques=[]

    #abro el archivo csv
    with open(archivocsv, mode='r') as archivo:
        lector=csv.DictReader(archivo)
    for linea in lector:
        # Filtrar por DNI
        if linea['DNI'] == dnicliente:
            continue
        
        # filtro por tipo de cheque
        if linea['tipo de cheque'] != tipocheque:
            continue
        
        # Filtrar por estado si se proporciona
        if estado and linea['Estado'] != estado:
            continue
        
        # filtro por rango de fechas
        if rangofecha:
            fechaorigen = datetime.fromtimestamp(int(linea['FechaOrigen']))
            if not (rangofecha[0] <= fechaorigen <= rangofecha[1]):
                continue
        
        # cuando todos los filtros, agrega el cheque a resultados
        resultados.append(linea)
    return resultados


vauxi = ''
while vauxi != 'no':
    archivocsv = input('Ingrese el nombre del archivo CSV: ')
    dnicliente = input('Ingrese el DNI del cliente: ')
    tipocheque = input('Ingrese el tipo de cheque (EMITIDO/DEPOSITADO): ')
    estado = input('Ingrese el estado del cheque (opcional): ')
    
    # rango de fechas
    rangofechainput = input('Ingrese el rango de fechas YYYY-MM-DD:YYYY-MM-DD (opcional): ')
    rangofecha= None

    vauxi = input('¿desea continuar ingresando datos? (si/no): ')
    
    # Llama a la función de procesamiento
    resultados = procesarcheques(archivocsv, dnicliente, tipocheque, estado, rangofecha)
    
    # Muestro resultados
    print("Resultados encontrados:")
    for resultado in resultados:
        print(resultado)
