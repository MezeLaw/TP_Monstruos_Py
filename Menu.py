from Monstruo import Monstruo
from Partida import Partida
from Jugador import Jugador
from TipoFuego import TipoFuego
from TipoAire import TipoAire
from TipoAgua import TipoAgua
from TipoTierra import TipoTierra
from ErrorAlIntentarCargar import ErrorAlIntentarCargar
from ErrorAlIntentarGuardar import ErrorAlIntentarGuardar
import pickle

class Menu():

    def __init__(self):
        print('#################################################################')
        print("")
        print("Bienvenido a 'Lucha de Monstruos'. Para jugar inicie una nueva partida.\n"
              "Lucha de Monstruos es un juego donde dos participantes combaten a muerte\n"
              "con sus monstruos y sus ataques. Cada monstruo tiene un tipo principal y \n"
              "uno secundario, así como también dos ataques: el simple y el especial.")
    def crear_nueva_partida(self):
        print("")
        print("#################################################################")
        #Creacion monstruos

        nombre1 = input('Ingrese el nombre del jugador numero 1: ')
        print("")
        print("##################################################################")
        print("")
        print('Pasaremos a la opcion de creacion de Monstruos. \nDebe elegir dos tipos de Monstruo para su monstruo. \nPuede elegir entre: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego')
        print("")
        tipo1 = input('#Seleccione el tipo principal para su monstruo:  ')
        while tipo1 != '1' and tipo1!='2' and tipo1!='3' and tipo1 !='4':
            tipo1 = input('#Utilice los numeros para seleccionar el tipo. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida:   ')
        print("")
        tipo2 = input('#Ahora seleccione el tipo secundario para su monstruo. \nDebe ser diferente al elegido anteriormente. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida: ')
        print('')
        while tipo2 !='1' and tipo2!='2' and tipo2!='3' and tipo2 !='4':
            tipo2 = input(
                '#Utilice los numeros para elegir el tipo secundario. \nDebe ser diferente al elegido anteriormente. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida: ')
        while tipo1 == tipo2:
            tipo2 = input(
                '#El tipo secundario de su monstruo debe ser diferente al elegido anteriormente. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida: ')
        print("#################################################################")
        print("")
        monstruoJugador1 = Monstruo(self.crear_tipo_correspondiente(self.validar_tipo(tipo1)), self.crear_tipo_correspondiente(self.validar_tipo(tipo2)), 100)
        print(monstruoJugador1.tipo_1.tipo, monstruoJugador1.tipo_2.tipo)
        print("#################################################################")
        nombre2 = input('Ingrese el nombre del jugador numero 2: ')
        print("#################################################################")
        print('Elija el primer tipo para su monstruo. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego')
        print("")
        tipo1J2 = input('#Seleccione el tipo principal para su monstruo:  ')
        while tipo1J2 != '1' and tipo1J2 != '2' and tipo1J2 != '3' and tipo1J2 != '4':
            tipo1J2 = input('#Utilice los numeros para indicar su selección. \nOpciones:  \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego')
        print("")
        tipo2J2 = input('#Seleccione el tipo secundario para su monstruo. \nDebe ser diferente al elegido anteriormente. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida: ')
        while tipo2J2 != '1' and tipo2J2 != '2' and tipo2J2 != '3' and tipo2J2 != '4':
            tipo2J2 = input('#Utilice los numeros para indicar su selección. \nOpciones:  \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego')
        print('')
        while tipo1J2 == tipo2J2:
            tipo2J2 = input(
                '#El tipo secundario de su monstruo debe ser diferente al elegido anteriormente. \nOpciones: \n1-Agua \n2-Aire \n3-Tierra \n4-Fuego \nOpcion elegida: ')
        print("#################################################################")

        monstruoJugador2 = Monstruo(self.crear_tipo_correspondiente(self.validar_tipo(tipo1J2)), self.crear_tipo_correspondiente(self.validar_tipo(tipo2J2)), 100)
        print(monstruoJugador2.tipo_1.tipo, monstruoJugador2.tipo_2.tipo)

        #Creacion jugadores

        jugador1 = Jugador(nombre1, monstruoJugador1)
        jugador2 = Jugador(nombre2, monstruoJugador2)

        #Creacion Partida

        partida = Partida(False, jugador1, jugador2, '')
        print("")
        print("Partida creada")
        print("###########################")
        print("Comienza el juego. Inicia el jugador numero 1. ")
        while partida.partidaFinalizada == False and partida.partidaGuardada == False:
            if partida.partidaFinalizada == False and partida.partidaGuardada == False:
                if partida.turnoJugador1 == True:
                    partida.turno_jugador_1()
                else:
                    partida.turno_jugador_2()
            if partida.partidaFinalizada == True:
                print("")
                print("¡¡Partida finalizada!!")
                print("Jugador ganador: ", partida.ganador)
                print(" ")
                print("Puede iniciar una nueva partida si así lo desea, o salir.")
                print("")
                print(" ---------------------------------------------------------- ")
                self.menu()

            if partida.partidaGuardada == True:
                nombrePartida = input("Ingrese el nombre de la partida a guardar: ")
                while nombrePartida == None:
                    nombrePartida = input("Ingrese el nombre de la partida a guardar: ")
                nombrePartida+='.pickle'
                self.guardar_partida(partida, nombrePartida)
                print("Partida guardada Exitosamente. Puede iniciar una nueva partida o salir si lo desea. Gracias")
                self.menu()

    def guardar_partida(self, partida, saveData):
        try:
            with open(saveData, 'wb') as archivoSave:
                pickle.dump(partida, archivoSave)
        except ErrorAlIntentarGuardar():
            print("Hubo un error al intentar guardar la partida. Lo sentimos.")
        #raise ErrorAlIntentarGuardar('Actualmente esta opción está en construcción. Lamentamos las molestias ocasionadas.')

    def cargar_partida(self):

        saveData = input("Ingrese el nombre de su partida a cargar : ")
        while saveData =="" or saveData == None:
            saveData = input("Ingrese el nombre de la partida a cargar: \n")
        saveData = saveData+'.pickle'
        try:
            with open(saveData, 'rb') as archivoSave:
               partida = pickle.load(archivoSave)
               partida.partidaGuardada = False
               print("")
               print("Partida cargada con éxito. ")
               print("")

               print("Resultados Parciales: ")
               print("Vida del J1 ", partida.jugador1.monstruo.vida)
               print("Vida del J2 ", partida.jugador2.monstruo.vida)
               print("")
               while partida.partidaFinalizada == False and partida.partidaGuardada == False:
                   #if partida.partidaFinalizada == False and partida.partidaGuardada == False:
                    if partida.turnoJugador1 == True:
                        partida.turno_jugador_1()
                    else:
                       partida.turno_jugador_2()

                    if partida.partidaFinalizada == True:
                       print("")
                       print("¡¡Partida finalizada!!")
                       print("Jugador ganador: ", partida.ganador)
                       print(" ")
                       print("Puede iniciar una nueva partida si así lo desea, o salir.")
                       print("")
                       print(" ---------------------------------------------------------- ")
                       self.menu()

        except ErrorAlIntentarCargar(Exception):
           print('Ocurrió un error al intentar cargar la partida. Lo sentimos mucho')
        ##raise ErrorAlIntentarCargar('Actualmente esta opción también está en construcción. Sentimos las molestias ocasionadas.')

    def salir(self):
        print('######################################')
        print('Deseamos haya disfrutado del juego.\n Que tenga un buen día!')

    def validar_tipo(self, tipo):
        tipos = {'1': 'Agua', '2': 'Aire', '3': 'Tierra', '4': 'Fuego'}
        tipoAux = tipos.get(tipo)
        return tipoAux


    def crear_tipo_correspondiente(self, tipo):
        if tipo == 'Aire':
            tipoRta = TipoAire()
        if tipo == 'Agua':
            tipoRta = TipoAgua()
        if tipo == 'Fuego':
            tipoRta = TipoFuego()
        if tipo == 'Tierra':
            tipoRta = TipoTierra()

        return tipoRta

    def menu(self):
        print("")
        print("Menu: ")
        op = 0
        while op != 3:
            try:
                print('1. Crear nueva partida')
                print('2. Cargar partida')
                print('3. Salir')
                op = (input('Seleccione una opcion: '))
                print("")
                if op == '1':
                    self.crear_nueva_partida()
                #if op == '2':
                   # self.guardar_partida()
                if op == '2':
                    self.cargar_partida()
                if op == '3':
                    self.salir()
                print("######################################")
                break
            except(ErrorAlIntentarGuardar):
                print("Upss! Algo salió mal :( ! Lamentamos las molestias!")
                print("")
            except(ErrorAlIntentarCargar):
                print("Upss! Lo sentimos, pero actualmente esta opción también está en construcción. Lamentamos las molestias!")
                print("")

if __name__ == '__main__':
    menu = Menu ()
    menu.menu()
    print("")