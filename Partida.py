
class Partida(object):

    def __init__(self, partidaFinalizada,  jugador1,  jugador2, ganador):
        self.partidaFinalizada = False
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turnoJugador1 = True
        self.ganador = ganador
        self.partidaGuardada = False



    def turno_jugador_1(self):
        if self.turnoJugador1==True:
            print("Turno de "+ self.jugador1.nombre+'.'+" Ingrese el ataque que desea utilizar: ")
            ataque = input('1 -Ataque Simple \n2 -Ataque Especial \n3 -Guardar Partida ')
            print("")
            if ataque == '1':
                print("")
                self.jugador1.ataqueSimple(self.jugador2.monstruo)
                self.turnoJugador1 = False
                if self.jugador2.monstruo.vida <= 0:
                    self.partidaFinalizada = True
                    self.ganador = self.jugador1.nombre

            if ataque =='2' and self.jugador1.cantidadAtaqueEspecial>0:
                print("")
                self.jugador1.ataqueEspecial(self.jugador2.monstruo)
                self.turnoJugador1 = False
                if self.jugador2.monstruo.vida <= 0:
                    self.partidaFinalizada = True
                    self.ganador = self.jugador1.nombre
            if ataque == '2' and self.jugador1.cantidadAtaqueEspecial<=0:
                print("Solo puede utilizar el ataque especial en 4 oportunidades. Perdio su turno! \nPreste atención para la próxima.")
                self.turnoJugador1 = False
                print("")
            if ataque == '2' or ataque == '1':
                print("Resultados del ataque: ")
                print("Vida de "+self.jugador1.nombre, self.jugador1.monstruo.vida)
                print("Vida de "+self.jugador2.nombre, self.jugador2.monstruo.vida)
                print("")
            if ataque == '3':
                self.partidaGuardada = True

        else:
            self.turno_jugador_2()


    def turno_jugador_2(self):
        print("Turno de "+ self.jugador2.nombre+'.'+" Ingrese el ataque que desea utilizar: ")
        ataque = input('1 -Ataque Simple \n2 -Ataque Especial \n3 -Guardar Partida ')
        print("")
        if ataque == '1':
            self.jugador2.ataqueSimple(self.jugador1.monstruo)
            self.turnoJugador1 = True
            if self.jugador1.monstruo.vida <= 0:
                self.partidaFinalizada = True
                self.ganador = self.jugador2.nombre

        if ataque == '2' and self.jugador2.cantidadAtaqueEspecial<=4 :
            print("")
            self.jugador2.ataqueEspecial(self.jugador1.monstruo)
            self.turnoJugador1 = True
            if self.jugador1.monstruo.vida <= 0:
                self.partidaFinalizada = True
                self.ganador = self.jugador2.nombre

        if ataque =='2' and self.jugador2.cantidadAtaqueEspecial<=0:
            print("Solo puede utilizar el ataque especial en 4 oportunidades. Perdio su turno! \nPreste atención para la próxima.")
            self.turnoJugador1 = True
            print("")
        if ataque == '1' or ataque == '2':
            print("")
            print("Resultados del ataque: ")
            print("Vida de "+self.jugador1.nombre, self.jugador1.monstruo.vida)
            print("Vida de "+self.jugador2.nombre, self.jugador2.monstruo.vida)
            print("")
        if ataque == '3':
            print("")
            self.partidaGuardada = True





