# Resaltador de Texto: Implementación secuencial
# Edna Jacqueline Zavala Ortega A01750480
# Erick Alberto Bustos Cruz A01378966

import resaltadorTexto as rt
import os
import time


def main(directory,sExpressions,fileExtension):
    """
    Función que recibe un string "directorio" con el path de un directorio determinado,
    un string "sExpressions" con el nombre de un archivo que contiene expresiones S que
    representan las categorías léxicas de un lenguaje de programación, y un string
    "fileExtension" que indica qué tipo de archivos se desean resaltar.
    La función genera un directorio de nombre "Resultados"(o con variantes de ese nombre),
    que contiene archivos html, donde se realiza un resaltado de texto para cada código
    con extensión "fileExtension" existente dentro de "directory".
    La implementación de este resaltador procesa los archivos de manera secuencial.
    """
    # Nombre tentativo del directorio donde se almacenarán los códigos resaltados. 
    directoryName = "Resultados"
    # Permite definir el nombre del directorio que se creará para almacenar los scripts resaltados.
    directoryName = rt.defineDirectory(directoryName, directory)
    
    # Lectura de las expresiones-s que permiten identificar las categorías léxicas del lenguaje.
    data = rt.expressionsFile(sExpressions) 
    # Se localizan todos los archivos .py que se permitan.
    files = rt.findFiles(directory,[], fileExtension)
    
    # Crea y se cambia al directorio en el que se almacenarán los scripts resaltados.
    os.mkdir(directoryName)
    os.chdir(directoryName) 
    
    # Ciclo que envía cada archivo encontrado con la extensión proporcionada al método principal del resaltados de Texto.
    for file in files:
        rt.textHighlighter(data[0],data[1], file, rt.nameHTML(file))



# Permite marcar el tiempo de inicio de la ejecución del programa.      
startTime = time.time()
# Llama al método main proporcionándole las expresiones-s y la extensión del archivo.
main('C:\\Users\\Jacqueline Zavala\\Documents\\GitHub\\textHighlighter\\Resaltador Paralelo\\Prueba', 'expresionesS.txt', '.py')
#main(os.getcwd(),'expresionesS.txt', '.py')
# Permite marcar el tiempo final de la ejecución del programa.     
finishTime = time.time() - startTime
# Imprime el tiempo de ejecución del programa.
print('Tiempo de Ejecución: '+ str(finishTime))
