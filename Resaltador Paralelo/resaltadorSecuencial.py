import ResaltadorTexto
import os


files = [] # directorios de los códigos

def nameHTML(file):
    fileName = os.path.split(file) 
    return fileName[1][:-2] + "html"

def findFiles(directory):
    os.chdir(directory)
    currentDirectory = os.listdir(directory) #['Codigos', 'Imagenes', 'code.py', 'imagen.jpg']
    print(currentDirectory)
    for element in currentDirectory:
        if '.py' in element:
            # Agregar path de archivo .py a files
            files.append(os.getcwd() + '\\'+ element)
        elif ('.' not in element) and ('__pycache__' not in element):
            # Llamada recursiva para explorar directorios interiores
            findFiles(os.getcwd() + '\\'+ element)
            # Regresa al directorio anterior
            os.chdir(os.path.dirname(os.getcwd()))
        
#textHighlighter('expresionesS.txt','ejemplo.py', 'nombre del html') 
findFiles(os.getcwd())
print(files)
# regresar a dir anterior os.chdir(os.path.dirname(os.getcwd()))
#>>> os.mkdir('Christmas Photos')

def main(directory):
    findFiles(directory)
    os.mkdir('Resultados')
    os.chdir('Resultados')    
    for file in files:
        ResaltadorTexto.textHighlighter('../expresionesS.txt',file, nameHTML(file))
        
main(os.getcwd())