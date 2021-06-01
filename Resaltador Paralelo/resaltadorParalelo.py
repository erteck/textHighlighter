import resaltadorTexto as rt
import os
import functools
from concurrent.futures import ProcessPoolExecutor
import time

def main(directory,sExpressions,cores, extension):
    directoryName = "Resultados"
    directoryName = rt.defineDirectory(directoryName)
   
    data = rt.expressionsFile(sExpressions)
    htmlNames = []
    files = rt.findFiles(directory,[], extension)
    size = len(files)//cores
    if size < 1:
        size = 1
    os.mkdir(directoryName)
    os.chdir(directoryName)
    for name in files:
        htmlNames.append(rt.nameHTML(name))
    with ProcessPoolExecutor(max_workers=6) as executor:        
        newFun = functools.partial(rt.textHighlighter, data[0], data[1])
        executor.map(newFun, files, htmlNames, chunksize = size)
    
        
if __name__ == '__main__': 
    startTime = time.time()
    main(os.getcwd(),'expresionesS.txt', 6, '.py')
    finishTime = time.time() - startTime
    print('Tiempo de Ejecución: '+ str(finishTime))
