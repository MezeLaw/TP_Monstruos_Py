import Tipo


class Monstruo():

    def __init__(self, tipo1, tipo2, vida):
        self.tipo_1 = tipo1
        self.tipo_2 = tipo2
        self.vida = vida

    def ataqueSimple(self):
        print('Realicé un ataque simple')

    def ataqueEspecial(self):
        print('Realicé un ataque especial')
