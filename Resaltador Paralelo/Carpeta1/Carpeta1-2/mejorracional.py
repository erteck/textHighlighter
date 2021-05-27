# ----------------------------------------------------------
#Erick Alberto Bustos Cruz A01378966
# 
#
# ----------------------------------------------------------

from functools import total_ordering
import math as m

@total_ordering
class Racional:
    """Instancias de esta clase representan números 
    racionales con un numerador y un denominador.
    """
    def __reducir(self):
        GCD = m.gcd(int(self.__numerador),int(self.__denominador))
        numdor = self.__numerador / GCD
        denom = self.__denominador / GCD
        self.__numerador = int(numdor)
        self.__denominador = int(denom)
        
    def __init__(self,numerador,denominador):
      self.__numerador = int(numerador)
      self.__denominador = int(denominador)
      if self.__denominador < 0 and self.__numerador < 0:
        self.__numerador = -numerador
        self.__denominador = -denominador
      elif self.__denominador < 0 and self.__numerador > 0:
        self.__numerador = -numerador
        self.__denominador = -denominador
      Racional.__reducir(self)
      
    @property
    def numerador(self):
      return self.__numerador
      
    @property
    def denominador(self):
      return self.__denominador
      
    @numerador.setter
    def numerador(self,numerador):
      self.__numerador = numerador
      if self.__denominador < 0 and self.__numerador < 0:
        self.__numerador = -numerador
        #self.__denominador = -denominador
      elif self.__denominador < 0 and self.__numerador > 0:
        self.__numerador = - numerador
        #self.__denominador = -denominador
      Racional.__reducir(self)
      
    @denominador.setter
    def denominador(self,denominador):
      self.__denominador = denominador
      if self.__denominador < 0 and self.__numerador < 0:
        #self.__numerador = -numerador
        self.__denominador = -denominador
      elif self.__denominador < 0 and self.__numerador > 0:
        #self.__numerador = -numerador
        self.__denominador = -denominador
      Racional.__reducir(self)
    
    def __str__(self):
      return f'{self.__numerador}/{self.__denominador}'
        
    def __repr__(self):
      return f'Racional({self.__numerador}, {self.__denominador})'
      
    def __eq__(self, otro):
      return self.__numerador/self.__denominador == otro.__numerador/otro.__denominador
    
    def __lt__(self, otro):
      if self.__numerador/self.__denominador < otro.__numerador/otro.__denominador:
        return True
      if self.__numerador/self.__denominador < otro.__numerador/otro.__denominador:
        return False
        
    def __neg__(self):
      numerador = - self.__numerador
      denominador = self.__denominador
      ans = Racional(numerador,denominador)
      return ans
      
    def inverso(self):
      ans = Racional(self.__denominador,self.__numerador)
      Racional.__reducir(ans)
      return ans
      
    def __add__(self, otro):
      if self.__denominador == otro.__denominador:
        return Racional(self.__numerador + otro.__numerador, self.__denominador)
      else:
        lcm = int(abs(self.__denominador*otro.__denominador) // m.gcd(self.__denominador, otro.__denominador))
        numerador_nuevo = int((lcm/self.__denominador) * self.__numerador + (lcm/otro.__denominador) * otro.__numerador )
        return Racional(numerador_nuevo, lcm)
    
    def __sub__(self, otro):
      if self.__denominador == otro.__denominador:
        return Racional(self.__numerador - otro.__numerador, self.__denominador)
      else:
        lcm = int(abs(self.__denominador*otro.__denominador) // m.gcd(self.__denominador, otro.__denominador))
        numerador_nuevo = int((lcm/self.__denominador) * self.__numerador - (lcm/otro.__denominador) * otro.__numerador )
        return Racional(numerador_nuevo, lcm)
        
    def __mul__(self,otro):
      numerador = self.__numerador * otro.__numerador
      denominador = self.__denominador * otro.__denominador
      ans = Racional(numerador,denominador)
      Racional.__reducir(ans)
      return ans
    
    def __truediv__(self,otro):
      numerador = self.__numerador * otro.__denominador
      denominador = self.__denominador * otro.__numerador
      ans = Racional(numerador,denominador)
      Racional.__reducir(ans)
      return ans