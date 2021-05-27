from abc import ABC,abstractmethod

class Ente(ABC):
    def __init__(self,nombre,hp,sp,deff,atck):
        self._nombre = nombre
        self._hp = hp
        self._sp = sp
        self._deff = deff
        self._atck = atck
        
    def atacar(self,e):
        e.tomar_daño(self._atck)
    
    def tomar_daño(self,puntos):
        if self._deff < puntos:
            self._hp -= puntos - self._deff
    
    def recuperar_hp(self,puntos):
        self._hp += puntos
        
    def usar_sp(self,puntos):
        if self._sp >= puntos:
            print('Exito!')
            self._sp -= puntos
            return True
        else:
            print('La habilidad ha fallado!')
            return False
    
    def recuperar_sp(self,puntos):
        self._sp += puntos
        
    def knockeado(self):
        if self._hp <= 0:
            return True
        else:
            return False
    
    def __str__(self):
        if self.knockeado():
            return f'{self._nombre} KO!'
        else:
            return f'{self._nombre}(HP={self._hp}, SP={self._sp}, DEF={self._deff}, ATK={self._atck})'
            
    @abstractmethod        
    def descansar(self):
        pass
            
class Hechizero(ABC):
  
    @abstractmethod
    def hechizar(self,e):
        pass
    
    def revivir(self,e):
        if isinstance(e,Heroe) and e.knockeado() and self.usar_sp(10):
            e.despertar()
        
        
class Orco(Ente):
    def __init__(self,nombre):
        super().__init__(nombre,hp=7,sp=0,deff=2,atck=6)
    
    def descansar(self):
        self.recuperar_hp(4)
        
class Heroe(Ente):
    def despertar(self):
        if self.knockeado():
            self._hp = 5
    
    def descansar(self):
        self.recuperar_hp(2)
        self.recuperar_sp(1)
        
class Mago(Heroe,Hechizero):
    def __init__(self,nombre):
        Heroe.__init__(self,nombre,hp=10, sp=15, deff=1, atck=5)
        
    def hechizar(self,e):
        if self.usar_sp(5):
            e.tomar_daño(self._atck * 2)
    
class Paladin(Heroe,Hechizero):
    def __init__(self,nombre):
        Heroe.__init__(self,nombre,hp=15, sp=10, deff=3, atck=8)
    
    def hechizar(self,e):
        if self.usar_sp(7) and isinstance(e,Heroe):
            e.recuperar_hp(2)
        else:
            e.tomar_daño(self._atck * 2)
            
            
        
            
        
        