import pandas as pd
import random as rd


#Oxigenación 95-100 NORMAL, menor a 95 WARNING
#Temperatura 36.5°C to 37°C NORMAL, diferente WARNING
#Ritmo cardiaco 60 a 100 NORMAL


codigos_postales=["53120", "54750", "52926", "53126", "54743", "54800", "54919", "54713", "53125", "53122","53120", "54750", "52926", "53126", "54743", "54800", "54919", "54713", "53125", "53122","53120"] #21

fechas = ["2020-11-08","2020-11-09","2020-11-10","2020-11-11", "2020-11-12", "2020-11-13", "2020-11-14" ,"2020-11-15", "2020-11-16", "2020-11-17", "2020-11-18", "2020-11-19", "2020-11-20", "2020-11-21"] #14

columnas = ["ID_U","Fecha","CP", "Oxigenacion", "RitmoCardiaco", "Temperatura", "Congestion", "DolorCabeza", "Tos", "Cansancio"]



arreglo = []

for filas in range(500): #500 muestras
    clave = rd.randint(1,21)
    if(clave == 7 or clave == 13 or clave == 18): 
        oxigenacion = round(rd.uniform(91.0,95.0),2)
        temperatura = round(rd.uniform(34.0, 36.0),2) #VALORES INFERIORES
        rpm = round(rd.uniform(97.0, 105.0),2)
        codigo_postal = codigos_postales[1] #54750
        congestion_nasal, dolor_cabeza, tos_seca , cansancio = "si", "si", "si", "si"
    elif(clave == 5 or clave == 6): #VALORES SUPERIORES
        oxigenacion = round(rd.uniform(91.0,95.0),2)
        temperatura = round(rd.uniform(37.0, 39.0),2)
        rpm = round(rd.uniform(97.0, 105.0),2)
        codigo_postal = codigos_postales[3] #53126
        congestion_nasal, dolor_cabeza, tos_seca , cansancio = "si", "si", "si", "si"
    elif (clave == 8 or clave == 16 or clave == 3): #Hermanos Diosdado Caballero y amigo Carlos Pazos
        oxigenacion = round(rd.uniform(91.0,95.0),2)
        temperatura = round(rd.uniform(37.0, 39.0),2)
        rpm = round(rd.uniform(97.0, 105.0),2)
        codigo_postal = codigos_postales[2] #52926
        congestion_nasal, dolor_cabeza, tos_seca , cansancio = "si", "si", "si", "si"
    elif(clave == 4 or clave == 19 or clave == 20):
        oxigenacion = round(rd.uniform(91.0,95.0),2)
        temperatura = round(rd.uniform(37.0, 39.0),2)
        rpm = round(rd.uniform(97.0, 105.0),2)
        codigo_postal = codigos_postales[clave] #54743, 53122","53120
        congestion_nasal, dolor_cabeza, tos_seca , cansancio = "si", "si", "si", "si"
    else:
        oxigenacion = round(rd.uniform(95.0,100.0),2)
        temperatura = round(rd.uniform(36.0, 37.0),2)
        rpm = round(rd.uniform(60.0, 100.0),2)
        codigo_postal = codigos_postales[clave-1]
        congestion_nasal, dolor_cabeza, tos_seca , cansancio = "no", "no", "no", "no"
    fecha = fechas[rd.randint(0,13)]
    arreglo.append([clave, fecha, codigo_postal, oxigenacion, rpm, temperatura, congestion_nasal, dolor_cabeza, tos_seca, cansancio])
    
df = pd.DataFrame(arreglo, columns = columnas)
df.to_csv("Datos_Dummy.csv", sep=",", index=False)
print(df.head(10))

