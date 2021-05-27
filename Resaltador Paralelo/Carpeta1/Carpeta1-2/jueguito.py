import random
from personajes import Ente, Orco, Heroe, Hechizero, Mago, Paladin

class Juego:
    
    @classmethod
    def demo(cls):
        l = Paladin('Paladin')
        g = Mago('Mago')
        o = Orco('Orco1')
        o2 = Orco('Orco2')
        lotr = [l, g, o, o2]
        for lotr1 in lotr:
            Juego.probando_tipos(lotr1)
        print(f'{g} hechiza a {l}')
        g.hechizar(l)
        print(f'Resultado = {l}')
        print()

        print(f'{o} ataca a {g}')
        o.atacar(g)
        print(f'Resultado = {g}')
        print()

        print(f'{o} descansa')
        o.descansar()
        print(f'Resultado = {o}')
        print()

        print(f'Recuperando directamente 10 hp a {o}')
        o.recuperar_hp(10)
        print(f'Resultado = {o}')
        print()

        print(f'{l} descansa')
        l.descansar()
        print(f'Resultado = {l}')
        print()

        l.recuperar_sp(20)

        print(f'{l} hechiza a {o2}')
        l.hechizar(o2)
        print(f'Resultado = {o2}')
        print()

        print(f'{l} hechiza a {g}')
        l.hechizar(g)
        print(f'Resultado = {g}')
        print()

        print(f'Asignando 20 daños directos a {g}')
        g.tomar_daño(20)
        print(f'Resultado = {g}')
        print()

        print(f'{l} revive a {g}')
        l.revivir(g)
        print(f'Resultado = {g}')
        print()

        print(f'Asignando 10 sp directos a {l}')
        l.recuperar_sp(10)
        print(f'Resultado = {l}')
        print()

        print(f'{l} revive a {g}')
        l.revivir(g)
        print(f'Resultado = {g}')
        print()

    @classmethod
    def probando_tipos(cls, e):
        print(f'Probando {e}')
        if isinstance(e, Ente):
            print('Es un ente')
        if isinstance(e, Heroe):
            print('Es un heroe')
        if isinstance(e, Orco):
            print('Es un orco')
        if isinstance(e, Paladin):
            print('Es un paladin')
        if isinstance(e, Mago):
            print('Es un mago')
        if isinstance(e, Hechizero):
            print('Es un hechizero')

    def __init__(self):
        self.personajes = []

    def añadir_personaje(self, e):
        self.personajes.append(e)

    def iniciar_juego(self):
        print('++++++++++++++++++++++++++')
        print('+++THE LORD OF THE QUIZ+++')
        print('++++++++++++++++++++++++++')
        print('')
        print('Comienza la batalla!')
        print('')
        turno = 0
        while (not self.heroes_ko() and not self.orcos_ko()):
            if (not self.personajes[turno].knockeado()):
                if (isinstance(self.personajes[turno], Heroe)):
                    self.turno_jugador(self.personajes[turno])
                else:
                    print('El amo del calabozo está pensando su jugada...')
                    self.turno_dm(self.personajes[turno])
                print('')
                print('Siguiente turno...')
            
            turno = (turno + 1) % len(self.personajes)
        if (self.heroes_ko()):
            print('El mal ha triunfado!')
        else:
            print('El bien ha triunfad!')
        
    

    def heroes_ko(self):
        for e in self.personajes:
            if isinstance(e, Heroe) and not e.knockeado():
                return False
        return True
    

    def orcos_ko(self):
        for e in self.personajes:
            if isinstance(e, Orco) and not e.knockeado():
                return False
        return True
    

    def turno_jugador(self, h):
        print(f'Turno de {h}')
        print('Escoge una acción:')
        print('a. Atacar')
        print('d. Descansar')
        if isinstance(h, Hechizero):
            print('h. Lanzar Hechizo')
            print('r. Revivir')
        option = input()
        if option in ['a', 'h', 'r']:
            i = 0
            print('Escoge un objetivo:')
            for e in self.personajes:
                print(f'{i}. {e}')
                i += 1
            target = self.personajes[int(input())]
            if option == 'a':
                print(f'{h} ha atacado a {target}')
                h.atacar(target)
            elif option == 'h':
                print(f'{h} intenta hechizar a {target}')
                h.hechizar(target)
            elif option == 'r':
                print(f'{h} intenta revivir a {target}')
                h.revivir(target)
            print(target)
        elif option == 'd':
            h.descansar()
            print(f'{h} toma un descanso...')        
    

    def turno_dm(self, o):
        target = random.choice(self.personajes)
        if isinstance(target, Heroe):
            print(f'{o} ha atacado a {target}')
            o.atacar(target)
            print(target)
        else:
            o.descansar()
            print(f'{o} ha tomado un descanso...')
        
def main():
    print('Bienvenido! Escoge una opción')
    print('1. Demo')
    print('2. Partida')
    opcion = int(input())
    if opcion == 1:
        Juego.demo()
    else:
        j = Juego()
        p = Paladin('Aragorn')
        m = Mago('Gandalf')
        o1 = Orco('Sgrimma')
        o2 = Orco('Wyzk')
        o3 = Orco('Krackett')
        j.añadir_personaje(p)
        j.añadir_personaje(m)
        j.añadir_personaje(o1)
        j.añadir_personaje(o2)
        j.añadir_personaje(o3)
        j.iniciar_juego()
        
main()