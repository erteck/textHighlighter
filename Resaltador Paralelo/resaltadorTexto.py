# Resaltador de Texto
# Edna Jacqueline Zavala Ortega A01750480
# Erick Alberto Bustos Cruz A01378966

import re
import os

def nameHTML(file):
    """
    Función que recibe un string con terminación .py
    la cual cambia por la terminación .html
    """
    fileName = os.path.split(file) 
    return fileName[1][:-2] + "html"

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
    if directoryName not in os.listdir(currentDirectory):  
        return directoryName
    else:
        directoryName += "-1"
        return defineDirectory(directoryName, currentDirectory)
    
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
                result = result + '.*'
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
        <link rel="stylesheet" href="../estilos.css">
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
        #print(listSegmentation)
       
        # Variable auxiliar para la detección de strings
        string = False
        
        # Procesar caracter por caracter
        for character in range(0,len(line)):
            #print('LA COMILLA ACTUAL ES: ' + actualQuotationMark)
            #print('PROCESANDO: ' + line[character])
            #print(line[character])
            # Al detectar el final de un string sencillo
            if ((line[character] == '"') or (line[character] == "'")) and string and (line[character] == actualQuotationMark):
                #print('AGREGADO CON UNO: ' + line[character])
                listSegmentation[-1] += line[character]
                string = False
                actualQuotationMark = ""
                
            # Al detectar una comilla por primera vez determinar si es un string normal o multi-línea
            elif ((line[character] == '"') or (line[character] == "'")) and (not comment) and (matchwithprevious is None or delimiter) and not string and not lineComment:
                #print('AGREGADO CON DOS: ' + line[character])
                delimiter = False
                quotationMCounter = 1
                actualQuotationMark = line[character]
                listSegmentation.append(line[character]) 
                 
                consecutiveQuotMarks = 0
                seenCharaters = 0
                #print(line[character:])
                # Checar si hay tres comillas seguidas
                for m in range(character,len(line)):
                    if  line[m] == actualQuotationMark and seenCharaters <= 2:
                        consecutiveQuotMarks += 1
                    seenCharaters += 1
                    if seenCharaters == 3:
                        break
    
                if consecutiveQuotMarks == 3:
                    #print("ES DE BLOQUEEEEE " + str(consecutiveQuotMarks))
                    comment = True
                else:
                   # print("ES DE STRINGGGGGGGG"+ str(consecutiveQuotMarks))
                    string = True
            
            # Si detecté un string/comentario multi-línea, manejo de comillas
            elif comment and ((line[character] == '"') or (line[character] == "'")) and (line[character] == actualQuotationMark):
                #print('AGREGADO CON TRES: ' + line[character])
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
                #print('AGREGADO CON CUATRO: ' + line[character])
                listSegmentation[-1] += line[character]
                
            # Identificar cualquier otro elemento perteneciente a categorías léxicas diferentes a los strings
            # verificándolo con las expresiones regulares
            elif line[character] != '\n': 
                
                for k in range(0, len(regexps)):
                    #print(regexps[k])
                    pattern = re.compile(regexps[k])
                    matchwithprevious = re.fullmatch(pattern, listSegmentation[-1]+line[character])
                    if matchwithprevious is not None:
                        if labels[k] in ['delimiter','operator']:
                            delimiter = True
                        elif labels[k] in ['commentary']:
                            lineComment = True
                        listSegmentation[-1] += line[character]
                        #print('AGREGADO CON CINCO: ' + line[character])
                        break
            
            # Agregar saltos de línea        
            elif line[character] == '\n': 
                #print('AGREGADO CON SEIS: ' + line[character])
                listSegmentation.append(line[character])

            # Agregar caracteres que no entran en ninguna categoría léxica por si solos
            if (matchwithprevious is None) and line[character] not in ["'",'"','\n'] and (not comment and not string): 
                #print('AGREGADO CON SIETE: ' + line[character])
                listSegmentation.append(line[character])
            #else:
                #print('NO AGREGADO: ' + line[character])
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
    


