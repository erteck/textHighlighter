import numpy as np


def maxpooling2(img):
  fr = len(img)//2
  cr = len(img[0]) // 2

  resr = 0

  resultado = np.zeros((fr,cr),np.uint8)

  for i in range(0, len(img),2):
    print(i)
    resc = 0
    for j in range(0, len(img[0]), 2):
      print(j)
      matrizlocal = img[i:(i+2),j:(j+2)]
      resultado[resr][resc] = np.amax(matrizlocal)
      resc += 1
    resr += 1
  return resultado

print(maxpooling2(img))