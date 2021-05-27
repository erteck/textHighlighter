from guitarra import Guitarra
from violin import Violin


class Concierto:
    
    def __init__(self, name):
        self.name = name
        self.__lista_instrumentos = []
    
    def agregar_instrumento(self, instrumento):
        self.__lista_instrumentos.append(instrumento)
    
    def ejecutar(self, mood):
        for instrumento in self.__lista_instrumentos:
            instrumento.tocar(mood)


def main():
    zoom_party = Concierto('Zoom Party')

    #aqui agregue cualquier otro instrumento que quiera tocar
    guitarrita = Guitarra()
    #zoom_party.agregar_instrumento(guitarrita)
    violincito = Violin()
    zoom_party.agregar_instrumento(violincito)

    zoom_party.ejecutar('energetic')

if __name__ == '__main__':
    main()