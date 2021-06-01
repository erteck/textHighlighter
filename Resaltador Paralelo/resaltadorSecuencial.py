import resaltador as rt
import os
import time




#textHighlighter('expresionesS.txt','ejemplo.py', 'nombre del html') 
#findFiles(os.getcwd())
# regresar a dir anterior os.chdir(os.path.dirname(os.getcwd()))
#>>> os.mkdir('Christmas Photos')

def main(directory,sExpressions):
    directoryName = "Resultados"
    directoryName = rt.defineDirectory(directoryName)
    data = rt.expressionsFile(sExpressions)
    files = rt.findFiles(directory,[])
    os.mkdir(directoryName)
    os.chdir(directoryName) 
    for file in files:
        rt.textHighlighter(data[0],data[1], file, rt.nameHTML(file))


      
startTime = time.time()
main(os.getcwd(),'expresionesS.txt')
finishTime = time.time() - startTime
print('Tiempo de Ejecución: '+ str(finishTime))
