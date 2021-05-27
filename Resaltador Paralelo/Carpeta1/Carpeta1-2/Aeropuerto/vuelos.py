vuelos = {}
with open('aviones.txt', 'r') as f:
  aviones = f.readlines()
  for avion in aviones:
    if avion not in vuelos:
      vuelos[avion] = 0
      vuelos[avion] += 1
    elif avion in vuelos:
      vuelos[avion] += 1
  
  tot_vuelos = 0
  for pais in vuelos:
    tot_vuelos += vuelos[pais]
  
  for pais in vuelos:
    if vuelos[pais] > tot_vuelos * 0.20:
      print(pais)