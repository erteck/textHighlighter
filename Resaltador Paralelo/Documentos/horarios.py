class Reloj:
    """Clase simple para representar las horas del dia"""
    
    def __init__(self, horas, minutos, segundos):
        """Inicializa instancias de Reloj. Si los datos proprcionados no son validos
        asigna horas = 0, minutos = 0, segundos = 0"""
        self._segundos = 0
        self._minutos = 0
        self._horas = 0
        self.establecer_reloj(horas, minutos, segundos)
    
    def establecer_reloj(self, horas, minutos, segundos):
        """Cambia la hora con los nuevos valores provistos
        Si alguno de los valores no es valido, no actualiza al atributo"""
        if type(segundos) == int and 0 <= segundos <= 59:
            self._segundos = segundos
        if type(minutos) == int and 0 <= minutos <= 59:
            self._minutos = minutos
        if type(horas) == int and 0 <= horas <= 23:
            self._horas = horas
    
    def __str__(self):
        return f'{self._horas:02d}:{self._minutos:02d}:{self._segundos:02d}'
    
    def avanzar_reloj(self):
        """Avanza la hora un segundo"""
        if self._segundos == 59:
            self._segundos = 0
            if self._minutos == 59:
                self._minutos = 0
                if self._horas == 23:
                    self._horas = 0
                else:
                    self._horas += 1
            else:
                self._minutos += 1
        else:
            self._segundos += 1

def main():
    r = Reloj(23, 59, 0)
    for i in range(60*60*2):
        print(r)
        r.avanzar_reloj()

if __name__ == '__main__':
    main()