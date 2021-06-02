# ESTE ES EL BUENO
import re


def main(archivo):
    patrones = {}
    fpatters = open(archivo,'r')
    for linea in fpatters:
        print(linea)
       
    
def createPatterns(line):
    result = ""
    concat = [""]
    lastSymbol = [""]
    for i in range(0, len(line)):
        if line[i] == ')' and line[i - 1] != "\\":
            concat.pop()
            result += lastSymbol[-1]
            lastSymbol.pop()
        elif line[i:i + 2] == "(.":
            concat.append('')
            lastSymbol.append('')
        elif line[i:i + 2] == "(*":
            concat.append('')
            lastSymbol.append('*')
        elif line[i:i + 2] == "(+":
            concat.append('|')
            lastSymbol.append(')')
            result+= '('
        elif line[i:i + 2] == "(#":
            concat.append('')
            lastSymbol.append('+')
        elif line[i] == " " and line[i - 2:i] in ["(*", '(.', '(#', '(+']:
            result += "" + ''
        elif line[i] == " ":
            if line[i+1] !="8":
                result += concat[-1] + ""
        elif line[i - 1:i + 1] not in ["(*", '(.', '(#', '(+']:
            #print(concat[-1])
            if(line[i] == '$'):
                result = result + '.*'
            elif (line[i] == '8'):
                lastSymbol.pop()
                lastSymbol.append(')?')
            else:
                result = result + line[i]

    return result


exprRegDoc = open('expresionesresultantes.txt','w')


regexpsDic = {}
text = open('expresionesmod.txt', 'r')
for line in text:
    firstime = True
    key = ""

    line = line.replace("\n", "")
    line = line.replace("  "," ")
    for i in range(0, len(line)):
        if line[i] == ":" and firstime:
            key = line[0:i]
            linea = line[i + 2:]
            #print(type(linea))
            regexpsDic[key] = createPatterns(line[i + 2:])
            exprRegDoc.write(key + ': '+ regexpsDic[key] + '\n')
            break

text.close()



etiquetas = list(regexpsDic.keys())


regexps = list(regexpsDic.values())


print(regexps)
superregex = '|'.join(regexps)
print(superregex)

# Crear archivo html
f = open('Resultado.html', 'w')
# texto


var = 0

code = open('bestcodigo.py','r')


contadorComillas = 0
comment = False
comentario = [""]
for line in code:
    for i in range(len(line)):
        if line[i] != " ":
            var = i
            html_template += len(line[0:i])*'&nbsp'
            break
    
    # Lista donde voy a guardar las expresiones separadas
    lista = [""]
    
    comillaActual = ""
    string = False

    matchwithprevious = None

    # Itero caracter por caracter en la parte de la línea donde empiezan los caracteres
    for character in line[i:]:
        
        # DEBO CHECAR LOS STRINGS porque terminan después
        if ((character == '"') or (character == "'")) and string and (character == comillaActual):
            lista[-1] += character
            contadorComillas += 1
            print('Agregado con primer if: '+ character)
            string = False
            comillaActual = ""
        elif ((character == '"') or (character == "'")) and (comillaActual == "") and matchwithprevious is None and (contadorComillas == 0):
            # Si hay comillas dentro de comentario multilínea.
            if comment: 
                contadorComillas = 0
                comentario[-1] += character
            else:    
                comillaActual = character
                lista.append(character)
                print('Agregado con el primer elif: ' + character)
                contadorComillas+=1
                string = True

                
        elif string or comment:
            if comment:
                contadorComillas = 0
                comentario[-1] += character
            else:
                lista[-1] += character
            print('Agregado con elif string: ' + character)
        elif (contadorComillas == 2) and ((character == '"') or (character == "'")):
            lista[-1] += character
            contadorComillas += 1
            if comment == True:
                comment = False
                lista.append(comentario)
                comentario = [""]
            else:
                comment = True
                comentario = lista
            
            #lista[-1] = '<commentary>'+lista[-1]
        
        else: 
            for k in range(0, len(regexps)):
                matchwithprevious = re.fullmatch(regexps[k], lista[-1]+character)
                if matchwithprevious is not None:
                    lista[-1] += character
                    print('Agregado con else: ' + character)
                    break
        if (matchwithprevious is None) and (not string) and character not in ["'",'"']:
        #if ((character != "'") and (character != '"')) and matchwithprevious is None and (not string):
            lista.append(character)
            print("Agregado con ult if: " + character)
        
    print(lista)
    #Nota al poner tres comillas sale un vacío debe ser porque ninguna exp regular acepta comillas solas
       
    for element in lista:
        receivedmatch = False
        for j in range(0, len(regexps)):
            match = re.fullmatch(regexps[j], element)
            if match is not None:
                #print('Hice match con: ' + element)
                etiquetaAbre = "<"+ etiquetas[j]+">"
                etiquetaCierra = "</"+ etiquetas[j]+">"
                html_template = html_template + etiquetaAbre + element + etiquetaCierra 
                receivedmatch = True
                break
           
                
        if receivedmatch == False or element == " ":
            html_template += element 
            #print('Agregué: '+ element )
                
    """
    split = re.split(regexpsDic['delimiter'] +'|(\s)' +'|'+regexpsDic['operator'],line)
    while None in split:
        split.remove(None)
    print(split)
    receivedmatch = False

    for element in split:
        #print(element)

        for j in range(0,len(regexps)):
            #print(regexps[j])
            reg = re.compile(regexps[j])
            match = re.fullmatch(reg,element)
            if match is not None:
                print('IN')
                
                html_template = html_template + etiquetaAbre + element + etiquetaCierra
                receivedmatch = True
                break
        if receivedmatch == False or element == " ":
            html_template += element    
    """
code.close()

""" ndjenjdn """

'''
Este es un comentario
"""
'''


  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()

e=3
