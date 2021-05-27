from playsound import playsound
from instrumento import Instrumento

class Guitarra(Instrumento):
    
    def tocar(self, mood):
        if mood == 'sad':
            print("Tocando una triste balada de guitarra :'(")
            playsound('guitar-sad.mp3')
        elif mood == 'energetic':
            print('Tocando una alegre melodia de guitarra')
            playsound('guitar-happy.mp3')