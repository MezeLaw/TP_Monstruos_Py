from Monstruo import  Monstruo

class Jugador(object):

    def __init__(self, nombre, monstruo):
        self.nombre = nombre
        self.monstruo = monstruo
        self.cantidadAtaqueEspecial = 4

    def ataqueSimple(self, monstruoOponente):
        #Aca habria que meter la logica de los tipos para los ataques
        #if monstruoOponente.tipo_1 or monstruoOponente.tipo_2
        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 1:
            monstruoOponente.vida = monstruoOponente.vida - 12
        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 2:
            monstruoOponente.vida = monstruoOponente.vida - 10
        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 0:
            monstruoOponente.vida = monstruoOponente.vida - 8

    def ataqueEspecial(self, monstruoOponente):
        # Idem verificacion de tipos

        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 1:
            monstruoOponente.vida = monstruoOponente.vida - 18
            self.cantidadAtaqueEspecial = self.cantidadAtaqueEspecial - 1
        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 2:
            monstruoOponente.vida = monstruoOponente.vida - 15
            self.cantidadAtaqueEspecial = self.cantidadAtaqueEspecial - 1
        if self.definirSiEsFuerte(self.monstruo, monstruoOponente) == 0:
            monstruoOponente.vida = monstruoOponente.vida - 12
            self.cantidadAtaqueEspecial = self.cantidadAtaqueEspecial - 1

    def definirSiEsFuerte(self, monstruo, monstruoOponente):
        cantidad_fuertes = 0
        cantidad_debiles = 0
        lista_oponente = [monstruoOponente.tipo_1, monstruoOponente.tipo_2]
        mi_lista = [monstruo.tipo_1, monstruo.tipo_2]

        for tipo in mi_lista:
            if tipo.soy_fuerte_frente == lista_oponente[0] or tipo.soy_fuerte_frente == lista_oponente[1]:
                cantidad_fuertes = cantidad_fuertes + 1
            if tipo.tipo == lista_oponente[0].soy_fuerte_frente or tipo.tipo == lista_oponente[1].soy_fuerte_frente:
                cantidad_debiles = cantidad_debiles + 1

            if cantidad_fuertes > cantidad_debiles:
                return 1

            if cantidad_fuertes == cantidad_debiles:
                return 2

            else:
                return 0