# Resaltador de Texto
# Edna Jacqueline Zavala Ortega A01750480
# Erick Alberto Bustos Cruz A01378966

from itertools import chain
import re
import os

def nameHTML(file, htmlNames):
    """
    Función que recibe un string con terminación .py
    la cual cambia por la terminación .html
    En caso de que el nombre de uno de los archivos a resaltar esté repetido (ya
    exista en htmlNames), se le agrega al nombre un "-1".
    """
    # Separar el nombre del archivo de su ruta
    fileName = os.path.split(file) 
    
    # Agregar .html al nombre del archivo eliminando el .py
    name = fileName[1][:-3] + ".html"
    
    # Si el nombre no está repetido, regresar el nombre 
    if name not in htmlNames:
        return name
    # Si está repetido agrega -1 y valida el nuevo nombre
    else:
        return nameHTML(fileName[1][:-3] + '-1' +".py", htmlNames) 

def findFiles(directory,files, extension):
    """
    Función que recibe un string  "directory" el cual contiene la dirección de un directorio
    y una lista de strings denominada "files". La función agrega las direcciones de todos los
    archivos con extensión "extension" presentes en el directorio dado a la lista "files",
    incluyendo aquellos en directorios anidados. Al final del proceso, se regresa la lista
    "files".
    """
    # Instanciarse en el directorio actual
    os.chdir(directory)
    
    # Listar elementos del dorectorio actual
    currentDirectory = os.listdir(directory)
    
    # Iterar sobre elementos
    for element in currentDirectory:
        if extension in element:
            # Agregar path de archivo .py a files
            files.append(os.getcwd() + '\\'+ element)
        elif ('.' not in element) and ('__pycache__' not in element):
            # Llamada recursiva para explorar directorios interiores
            files  = findFiles(os.getcwd() + '\\'+ element, files, extension)
            # Regresa al directorio anterior
            os.chdir(os.path.dirname(os.getcwd()))
    return files
        
def defineDirectory(directoryName, currentDirectory):
    """
    Recibe un string "directoryName" con el nombre de un subdirectorio en el directorio actual,
    revisa si existe ya un directorio con dicho nombre y en caso de ser así regresa 
    "directoryName" concatenado con -1. En caso contrario, regresa únicamente "directoryName"
    """
    # Si no exite un directorio con el nombre "directoryName", regresar el nombre
    if directoryName not in os.listdir(currentDirectory):  
        return directoryName
    # Si ya exite un directorio con el nombre "directoryName", agregar -1 al nombre y validarlo de nuevo
    else:
        directoryName += "-1"
        return defineDirectory(directoryName, currentDirectory)
    
def createCSS(labels, identical = [[]]):
    """
    Función que permite crear un CSS dentro del directorio de los resultados ya que es indispensable
    para visualizar los scripts resaltados de distintos colores. Recibe las etiquetas de las categorías
    léxicas del lenguaje y opcionalmente una lista de listas con las etiquetas que se deben resaltar 
    con el mismo color (en dicha lista se deben agrupar dentro de una lista las etiquetas de las 
    expresiones que se desean observar del mismo color).
    """
    # Lista de algunas opciones de colores para las categorías léxicas.
    colors = ['orange', 'green', 'blue', 'red', 'deeppink', 'rgb(0, 137, 161)', 'gray', 'black', 
              'rgba(174, 54, 243, 0.938)', 'rgb(182, 194, 11)', 'rgb(49, 207, 255)', 'rgb(122, 4, 87)',
              'rgb(214, 30, 85)', 'rgb(1, 161, 86)','rgb(255, 102, 0)', 'rgb(61, 1, 11)']
    # Variable que contendrá todo el script generado para el CSS.
    css = ''
    # Índice que permite iterar sobre la lista de colores.
    i = 0
    
    # Ciclo que permite asignar el mismo color a las etiquetas que el usuario ha señalado que deben
    # observarse del mismo color.
    for iterable in identical:
        for element in iterable:
            categoryFormat = element + '{\n\tcolor: '+ colors[i] +';\n}\n'
            css += categoryFormat
        i+=1       
    
    # Ciclo que permite asignar un color distinto al resto de las etiquetas correspondientes a las
    # categorías léxicas.
    for label in labels:
        if label not in chain(*identical):
            categoryFormat = label + '{\n\tcolor: '+ colors[i] +';\n}\n'
            css += categoryFormat
            if (i+1) == len(colors):
                i=0
            else:
                i+=1
                
    # Agrega al CSS la etiqueta 'pre' que pre-formatea el texto y determina que el tamaño de la fuente 
    # sea extra-extra grande.
    css += 'pre{\n\tfont-size: xx-large;\n}\n'  
     
    # Escribe el contenido dentro de un archivo con la extensión CSS 
    with open ('estilos.css', 'w', encoding='utf-8') as f:
        f.write(css)
            
def createPatterns(line):
    """
    Función que, dada una línea de un archivo de texto con expresiones s, regresa un string
    de la forma  ->   [identificador]: [expresión regular de la librería re de python]
    Las expresiones s recibidas deben estar estructuradas con la notación especificada
    en el reporte anexo.
    """
    # Resultado
    result = ""
    
    # Pila LIFO con caracteres de concatenación de las intrucciones empleadas en las expresiones s.
    # Ejemplo: la instrucción de unión (+) en las expresiones s requiere utilizar el caracter | para
    # concatenar sus argumentos al realizar la traducción a expresiones regulares de python. (+ 1 2 3) -> (1|2|3)
    concat = [""]
    
    # Pila LIFO con caracteres que deben ser agregados al final de una intrucción dentro de una
    # expresión regular de python.
    # Ejemplo: la instrucción de cerradura (*) en las expresiones s requiere colocar el caracter *
    # al final de los argumentos al realizar la traducción a expresiones regulares de python. 
    # (* [abc]) -> [abc]*
    lastSymbol = [""]
    
    for i in range(0, len(line)):
        # Detección del final de una instrucción
        if line[i] == ')' and line[i - 1] != "\\":
            concat.pop()
            result += lastSymbol[-1]
            lastSymbol.pop()
        # Detección del inicio de una instrucción de concatenación
        elif line[i:i + 2] == "(.":
            concat.append('')
            lastSymbol.append('')
        # Detección del inicio de una instrucción de cerradura
        elif line[i:i + 2] == "(*":
            concat.append('')
            lastSymbol.append('*')
        # Detección del inicio de una instrucción de unión
        elif line[i:i + 2] == "(+":
            concat.append('|')
            lastSymbol.append(')')
            result+= '('
        # Detección del inicio de una instrucción de cerradura donde debe aparecer al menos una vez el argumento
        elif line[i:i + 2] == "(#":
            concat.append('')
            lastSymbol.append('+')
        # Detección de espacios en blanco entre instrucciones anidadas
        elif line[i] == " " and line[i - 2:i] in ["(*", '(.', '(#', '(+']:
            result += ""
        # Detección de cualquier otro espacio en blanco (entre agrumentos)
        elif line[i] == " ":
            if line[i+1] !="8":
                result += concat[-1]
        # Agregar los argumentos
        elif line[i - 1:i + 1] not in ["(*", '(.', '(#', '(+']:
            if(line[i] == '$'):
                result = result + '.'
            elif (line[i] == '8'):
                lastSymbol.pop()
                lastSymbol.append(')?')
            else:
                result = result + line[i]

    return result


def expressionsFile(sExpressions):
    #global labels
    #global regexps
    # Documento donde se guardan los equivalentes de las expresiones s a expresiones regulares de python
    exprRegDoc = open('expresionesresultantes.txt','w')

    # Diccionario donde las llaves son los identificadores de cada expresión regular y los valores
    # la expresión regular como tal
    regexpsDic = {}

    # Lectura del documento con las expresiones s
    text = open(sExpressions, 'r')

    # Iterar línea por línea
    for line in text:
        firstime = True
        key = ""
        
        # Quitar saltos de línea y dobles espacios
        line = line.replace("\n", "")
        line = line.replace("  "," ")
        
        # Iterar caracter por caracter
        for i in range(0, len(line)):
            
            # Identidicar el fin de la etiqueta
            if line[i] == ":" and firstime:
                
                # Volver la eqtiqueta una llave
                key = line[0:i]
                
                # Usar createPatterns para extraer la expresión regular y guardarla en el diccionario
                regexpsDic[key] = createPatterns(line[i + 2:])
                exprRegDoc.write(key + ': '+ regexpsDic[key] + '\n')
                break

    text.close()
    
    # Crear lista con etiquetas
    labels = list(regexpsDic.keys())
    
    # Crear lista con expresiones regulares
    regexps = list(regexpsDic.values())
    
    return [labels,regexps]
     
    

def textHighlighter(labels, regexps, codeFile, htmlName):# sExpressions = "../expresionesS.txt"):
    """
    Recibe un documento txt "sExpressions" con expresiones s que describen las categorías léxicas de un lenguaje
    de programación y un documento "codeFile" con el código a analizar.
    Como resultado, la función crea un documento "Resultado.html" donde escribe el código de "codeFile"
    coloreando cada elemento perteneciente a una categoría léxica de un color diferente.
    """

    # Crear archivo html donde se va a guardar el resultado
    f = open(htmlName, 'w', encoding = 'utf8')
    
    # Establecer un template
    html_template = """
    <html>
    <head>
        <link rel="stylesheet" href="estilos.css">
    </head>
    <body>
    <p><pre>"""
    
    # Abrir archivo con código a analizar
    code = open(codeFile,'r', encoding = 'utf8')
    
    # Lista donde se guardarán strings procedentes de la segmentación del archivo con código de python
    listSegmentation = [""]
    
    # Variable auxiliar para la detección de strings, cuenta las comillas vistas
    quotationMCounter = 0
    
    # Variable auxiliar para la detección de comentarios
    comment = False
    
    # 
    lineComment = False
    
    # Variable que permite detectar si un string o comentario empieza y termina con
    # el mismo tipo de comilla
    actualQuotationMark = ""
    
    # Variable que me permite determinar si el último elemento de la lista
    # concatenado con el caracter actual satisface alguna expresión regular establecida
    matchwithprevious = None
    
    # Variable que permite deterctar strings sin separación de delimitadores u operadores
    delimiter = False
    
    # Iterar línea por línea
    for line in code:
        matchwithprevious = None
        lineComment = False
       
        # Variable auxiliar para la detección de strings
        string = False
        
        # Procesar caracter por caracter
        for character in range(0,len(line)):
            # Al detectar el final de un string sencillo
            if ((line[character] == '"') or (line[character] == "'")) and string and (line[character] == actualQuotationMark):
                listSegmentation[-1] += line[character]
                string = False
                actualQuotationMark = ""
                
            # Al detectar una comilla por primera vez determinar si es un string normal o multi-línea
            elif ((line[character] == '"') or (line[character] == "'")) and (not comment) and (matchwithprevious is None or delimiter) and not string and not lineComment:
                delimiter = False
                quotationMCounter = 1
                actualQuotationMark = line[character]
                listSegmentation.append(line[character]) 
                 
                consecutiveQuotMarks = 0
                seenCharaters = 0
                
                # Checar si hay tres comillas seguidas
                for m in range(character,len(line)):
                    if  line[m] == actualQuotationMark and seenCharaters <= 2:
                        consecutiveQuotMarks += 1
                    seenCharaters += 1
                    if seenCharaters == 3:
                        break
                # Es un comentario/string de bloque
                if consecutiveQuotMarks == 3:
                    comment = True
                # Es un string común
                else:
                    string = True
            
            # Si detecté un string/comentario multi-línea, manejo de comillas
            elif comment and ((line[character] == '"') or (line[character] == "'")) and (line[character] == actualQuotationMark):
                listSegmentation[-1] += line[character]
                
                # Verificar si hay tres comillas seguidas (para finalizar el comentario)
                consecutiveQuotMarks = 0
                seenCharaters = 0
                for m in range(character,len(line)):
                    if  line[m] == actualQuotationMark and seenCharaters <= 2:
                        consecutiveQuotMarks += 1
                    seenCharaters += 1
                    if seenCharaters == 3:
                        break
                
                # Agregar las primeras tres comillas
                if quotationMCounter < 3:
                    quotationMCounter += 1
                # Agregar las últimas tres comillas 
                elif consecutiveQuotMarks == 3 or quotationMCounter > 3:
                    quotationMCounter += 1
                    if quotationMCounter == 6:
                        quotationMCounter = 0
                        actualQuotationMark = ""
                        comment = False
            
            # Agregar el contenido de un string o comentario siempre que no sean las comillas que lo delimitan
            elif string or comment:
                listSegmentation[-1] += line[character]
                
            # Identificar cualquier otro elemento perteneciente a categorías léxicas diferentes a los strings
            # verificándolo con las expresiones regulares
            elif line[character] != '\n': 
                
                for k in range(0, len(regexps)):
                    pattern = re.compile(regexps[k])
                    matchwithprevious = re.fullmatch(pattern, listSegmentation[-1]+line[character])
                    if matchwithprevious is not None:
                        if labels[k] in ['delimiter','operator']:
                            delimiter = True
                        elif labels[k] in ['commentary']:
                            lineComment = True
                        listSegmentation[-1] += line[character]
                        break
            
            # Agregar saltos de línea        
            elif line[character] == '\n': 
                listSegmentation.append(line[character])

            # Agregar caracteres que no entran en ninguna categoría léxica por si solos
            if (matchwithprevious is None) and line[character] not in ["'",'"','\n'] and (not comment and not string): 
                listSegmentation.append(line[character])

    code.close()
    
    # Iterar sobre la lista, identificar expresiones regulares y  agregarlas al template
    # con sus debidas labels
    for element in listSegmentation:
        receivedmatch = False
        for j in range(0, len(regexps)):
            match = re.fullmatch(regexps[j], element)
            if match is not None:
                openLabel = "<"+ labels[j]+">"
                closeLabel = "</"+ labels[j]+">"
                html_template = html_template + openLabel + element + closeLabel 
                receivedmatch = True
                break        
        if receivedmatch == False or element == " ":
            html_template += element
    
    # Agregar labels finales      
    html_template += "</pre><p></body></html>"
  
    # Escribir template en archivo html
    f.write(html_template)
    
    # Cerrar archivo html
    f.close()
    


