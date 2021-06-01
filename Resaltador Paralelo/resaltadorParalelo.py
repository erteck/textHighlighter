import resaltadorTexto as rt
import os
import functools
from concurrent.futures import ProcessPoolExecutor
import time



def main(directory,sExpressions,cores):
    directoryName = "Resultados"
    directoryName = rt.defineDirectory(directoryName)
    #print(type(newDirectory))
   
    data = rt.expressionsFile(sExpressions)
    htmlNames = []
    files = rt.findFiles(directory,[])
    chunks = len(files)//cores
    if chunks < 1:
        chunks = 1
    os.mkdir(directoryName)
    os.chdir(directoryName)
    for name in files:
        htmlNames.append(rt.nameHTML(name))
    #with ProcessPoolExecutor(max_workers=6) as executor:
    #    fileNames = executor.map(nameHTML, files, chunksize = chunks)
    #for name in fileNames:
    #    htmlNames.append(name)
    with ProcessPoolExecutor(max_workers=6) as executor:        
        newFun = functools.partial(rt.textHighlighter, data[0], data[1])
        executor.map(newFun, files, htmlNames, chunksize = chunks)
    
        
if __name__ == '__main__': 
    startTime = time.time()
    main(os.getcwd(),'expresionesS.txt',6)
    finishTime = time.time() - startTime
    print('Tiempo de Ejecución: '+ str(finishTime))
