from playsound import playsound
from instrumento import Instrumento

class Violin(Instrumento):
    
    def tocar(self, mood):
        if mood == 'sad':
            print('El violin mas pequeño del mundo, tocando la cancion mas triste del mundo')
            playsound('violin-sad.mp3')
        elif mood == 'energetic':
            print('Tocando feliz con mi violin')
            playsound('violin-happy.mp3')