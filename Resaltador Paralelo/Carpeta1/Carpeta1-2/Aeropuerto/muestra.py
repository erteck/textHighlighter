# creaciion de un diccionario
d = {}

# guardar valor 10 con llave 'j'
d['j'] = 10

# revisar si existe elemento con llave k
# si existe, sumarle uno a su valor
# de lo contrario, agregarlo al diccionario con valor de 0
if 'k' in d:
  d['k'] += 1
else:
  d['k'] = 0

# obtener las llaves del diccionario
print('Llaves:')
for k in d.keys():
  print(k)

# obtener los valores del diccionario
print('Valores:')
for v in d.values():
  print(v)

# obtener los valores del diccionario
print('Llaves y Valores:')
for i in d.items():
  print(i)