# Resaltador de Texto: Implementación paralela
# Edna Jacqueline Zavala Ortega A01750480
# Erick Alberto Bustos Cruz A01378966

import resaltadorTexto as rt
import os
import functools
from concurrent.futures import ProcessPoolExecutor
import time

def main(directory,sExpressions,cores, fileExtension):
    """
    Función que recibe un string "directorio" con el path de un directorio determinado,
    un string "sExpressions" con el nombre de un archivo que contiene expresiones S que
    representan las categorías léxicas de un lenguaje de programación, un entero "cores"
    que indica el número de núcleos que posee la computadora del usuario y un string
    "fileExtension" que indica qué tipo de archivos se desean resaltar.
    La función genera un directorio de nombre "Resultados"(o con variantes de ese nombre),
    que contiene archivos html, donde se realiza un resaltado de texto para cada código
    con extensión "fileExtension" existente dentro de "directory".
    La implementación de este resaltador hace uso de procesos paralelos que hacen uso
    de todos los "cores" disponibles en el procesador para maximizar la eficiencia.
    """
    # Nombre tentativo del directorio donde se almacenarán los códigos resaltados 
    directoryName = "Resultados"
    # Permite definir el nombre del directorio que se creará para almacenar los scripts resaltados.
    directoryName = rt.defineDirectory(directoryName) 
    # Lectura de las expresiones-s que permiten identificar las categorías léxicas del lenguaje.
    data = rt.expressionsFile(sExpressions)
    # Permite almacenar los nombres que se les asignarán a los archivos html resaltados.
    htmlNames = []
    # Se localizan todos los archivos .py que se permitan.
    files = rt.findFiles(directory,[], fileExtension) 
    # Define de manera dinámica el tamaño del "chunk" que tomará cada proceso.
    size = len(files)//cores 
    
    # Evita que el tamaño del "chunk" sea inválido.
    if size < 1: 
        size = 1
    
    # Crea y se cambia al directorio en el que se almacenarán los scripts resaltados.
    os.mkdir(directoryName)
    os.chdir(directoryName)
    
    # Agrega a la lista htmlNames los nombres de los archivos html que se crearán como resultado del resaltado.
    for name in files:
        htmlNames.append(rt.nameHTML(name))
    
    # Se crean tantos procesos como cores se haya especificado que tiene el procesador y le envía a cada uno un "chunk"
    # de tamaño "size" para que lo procese con la función parcial derivada de la función principal del textHighlighter.
    # Nota: dicho cambio fue necesario dado que dos de los argumentos son estáticos y no iterables. 
    with ProcessPoolExecutor(max_workers = cores) as executor:        
        newFun = functools.partial(rt.textHighlighter, data[0], data[1])
        executor.map(newFun, files, htmlNames, chunksize = size)
     
if __name__ == '__main__':
    """
    Llama al método main y permite calcular el tiempo que le toma resaltar
    todos los scripts considerando la extensión y las expresiones proporcionadas.
    Imprime el tiempo de ejecución.
    """
    startTime = time.time()
    main(os.getcwd(),'expresionesS.txt', 6, '.py')
    finishTime = time.time() - startTime
    print('Tiempo de Ejecución: '+ str(finishTime))
