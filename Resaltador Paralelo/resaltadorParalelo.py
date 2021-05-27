import ResaltadorTexto
import os
import functools
from concurrent.futures import ProcessPoolExecutor
import time

files = [] # directorios de los códigos


def nameHTML(file):
    fileName = os.path.split(file) 
    return fileName[1][:-2] + "html"

def findFiles(directory):
    os.chdir(directory)
    currentDirectory = os.listdir(directory) #['Codigos', 'Imagenes', 'code.py', 'imagen.jpg']
    for element in currentDirectory:
        if '.py' in element:
            # Agregar path de archivo .py a files
            files.append(os.getcwd() + '\\'+ element)
        elif ('.' not in element) and ('__pycache__' not in element):
            # Llamada recursiva para explorar directorios interiores
            findFiles(os.getcwd() + '\\'+ element)
            # Regresa al directorio anterior
            os.chdir(os.path.dirname(os.getcwd()))
        
def defineDirectory(directoryName):
    if directoryName not in os.listdir(os.getcwd()):  
        print(directoryName)
        return str(directoryName)
    else:
        directoryName += "-1"
        defineDirectory(directoryName)

def main(directory,sExpressions,cores):
    directoryName = "Resultados"
    directoryName1 = str(defineDirectory(directoryName))
    #print(type(newDirectory))
    chunks = len(files)//cores
    if chunks < 1:
        chunks = 1
    data = ResaltadorTexto.expressionsFile(sExpressions)
    htmlNames = []
    findFiles(directory)
    os.mkdir(directoryName1)
    os.chdir(directoryName1)
    with ProcessPoolExecutor(max_workers=6) as executor:
        fileNames = executor.map(nameHTML, files)
    for name in fileNames:
        htmlNames.append(name)
    with ProcessPoolExecutor(max_workers=6) as executor:        
        newFun = functools.partial(ResaltadorTexto.textHighlighter, data[0], data[1])
        future = executor.map(newFun, files, htmlNames, chunksize = chunks)
    
        
if __name__ == '__main__': 
    startTime = time.time()
    main(os.getcwd(),'expresionesS.txt',6)
    finishTime = time.time() - startTime
    print('Tiempo de Ejecución: '+ str(finishTime))
