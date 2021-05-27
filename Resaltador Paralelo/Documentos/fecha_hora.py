from fechas import Calendario
from horarios import Reloj

class CalendarioReloj(Reloj, Calendario):
    
    def __init__(self, dia, mes, año, horas, minutos, segundos):
        Calendario.__init__(self, dia, mes, año)
        Reloj.__init__(self, horas, minutos, segundos)
    
    def __str__(self):
        return f'{Calendario.__str__(self)}, {Reloj.__str__(self)}'
    
    def avanzar_reloj(self):
        hora_vieja = self._horas
        super().avanzar_reloj()
        if self._horas < hora_vieja:
            self.avanzar_fecha()