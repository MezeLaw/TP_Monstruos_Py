import Tipo

class TipoAgua():

    def __init__(self, tipo='Agua', soy_fuerte_frente='Fuego', soy_debil_frente='Tierra'):
        self.tipo = tipo
        self.soy_fuerte_frente = soy_fuerte_frente
        self.soy_debil_frente = soy_debil_frente

    def __str__(self):
        return " %s: %s, %s" %(self.tipo, self.soy_fuerte_frente, self.soy_debil_frente)