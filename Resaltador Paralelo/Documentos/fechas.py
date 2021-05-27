class Calendario:
    """Clase simple para representar fechas"""
    
    # Duraciones de cada mes
    _duraciones = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    @classmethod
    def es_bisiesto(cls, a):
        """Determina si un año es bisiesto o no de acuerdo al agloritmo
        if (year is not divisible by 4) then (it is a common year)
        else if (year is not divisible by 100) then (it is a leap year)
        else if (year is not divisible by 400) then (it is a common year)
        else (it is a leap year)"""
        if a % 4 != 0:
            return False
        elif a % 100 != 0:
            return True
        elif a % 400 != 0:
            return False
        else:
            return True
        
    def __init__(self, dia, mes, año):
        """Inicializa instancias de Calendario. Si los datos proprcionados no son validos
        asigna dia = 1, mes = 1, año = 1970"""
        self._dia = 1
        self._mes = 1
        self._año = 1970
        self.establecer_fecha(dia, mes, año)
    
    def establecer_fecha(self, dia, mes, año):
        """Cambia la fecha con los nuevos valores provistos
        Si alguno de los valores no es valido, no actualiza al atributo"""
        if type(año) == int and año > 0:
            self._año = año
        if type(mes) == int and 1 <= mes <= 12:
            self._mes = mes
        if self._mes == 2 and Calendario.es_bisiesto(self._año):
            num_dias = 1
        else:
            num_dias = 0
        if type(dia) == int and 1 <= dia <= Calendario._duraciones[self._mes - 1] + num_dias:
            self._dia = dia
    
    def __str__(self):
        return f'{self._dia:02d}/{self._mes:02d}/{self._año}'
    
    def avanzar_fecha(self):
        """Avanza la fecha un dia"""
        if self._mes == 2 and Calendario.es_bisiesto(self._año):
            num_dias = 1
        else:
            num_dias = 0
        if self._dia == Calendario._duraciones[self._mes-1] + num_dias:
            self._dia = 1
            if self._mes == 12:
                self._mes = 1
                self._año += 1    
            else:
                self._mes += 1
        else:
            self._dia += 1

def main():
    c = Calendario(1, 1, 1990)
    for i in range(3653):
        print(c)
        c.avanzar_fecha()
        
if __name__ == '__main__':
    main()