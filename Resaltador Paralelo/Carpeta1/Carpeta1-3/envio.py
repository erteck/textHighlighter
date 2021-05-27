class Envio:
    def __init__(self,nombreR,direccionR,cpR,nombreD,direccionD,cpD,largo,ancho,costo_estandar):
        self._nombreR = nombreR
        self._direccionR = direccionR
        self._cpR = cpR
        self._nombreD = nombreD
        self._direccionD = direccionD
        self._cpD = cpD
        self._largo = largo
        self._ancho = ancho
        self._costo_estandar = costo_estandar
        
    
    def calcula_costo(self):
        return self._costo_estandar
    
    def __str__(self):
        return f'De: {self._nombreR}, {self._direccionR}, CP: {self._cpR}. Para: {self._nombreD}, {self._direccionD}, {self._cpD}. Dimensiones: {self._largo} x {self._ancho}. Costo: ${self.calcula_costo()}'
        

class Sobre(Envio):
    def __init__(self,nombreR,direccionR,cpR,nombreD,direccionD,cpD,largo,ancho,costo_estandar,cargo_adicional):
        super().__init__(nombreR,direccionR,cpR,nombreD,direccionD,cpD,largo,ancho,costo_estandar)
        self._cargo_adicional = cargo_adicional
    
    def calcula_costo(self):
        if self._largo > 25 or self._ancho > 30:
            return self._costo_estandar + self._cargo_adicional
        else:
            return self._costo_estandar
    
    def __str__(self):
        return 'Sobre. ' + super().__str__()
        
class Paquete(Envio):
    def __init__(self,nombreR,direccionR,cpR,nombreD,direccionD,cpD,largo,ancho,costo_estandar,profundidad,peso,costoperkg):
        super().__init__(nombreR,direccionR,cpR,nombreD,direccionD,cpD,largo,ancho,costo_estandar)
        self._profundidad = profundidad
        self._peso = peso
        self._costoperkg = costoperkg
    
    def calcula_costo(self):
        return super().calcula_costo() + self._peso * self._costoperkg
        
    def __str__(self):
        return 'Paquete. ' + super().__str__()

e1 = Envio('Luke', 'Owen Farm', 1408, 'Anakin', 'Lava Fortress', 1518, 10, 20, 200)
print(e1)
p1 = Paquete('Leia', 'DS Jail', 3125, 'Han', 'Carbonite Slab', 2100, 20, 30, 200, 15, 3, 150)
print(p1)
s1 = Sobre('Yoda', 'Swamp', 2879, 'Ben', 'High Ground', 8879, 30, 20, 200, 50)
print(s1)