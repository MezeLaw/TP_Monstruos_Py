import Tipo

class TipoAire():

    def __init__(self, tipo = 'Aire', soy_fuerte_frente = 'Agua', soy_debil_frente = 'Tierra'):
        self.tipo = tipo
        self.soy_fuerte_frente = soy_fuerte_frente
        self.soy_debil_frente = soy_debil_frente

    def __str__(self):
        return " %s: %s, %s" %(self.tipo, self.soy_fuerte_frente, self.soy_debil_frente)