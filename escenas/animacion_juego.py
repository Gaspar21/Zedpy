__author__ = 'cristian'
import botones
import pilas
import robotlib
import data


class Animacion(object):
    imagen_actor_robot_1 = 'imag/Interfaz/Actor/robot2.png'
    imagen_actor_robot_2 = 'imag/Interfaz/Actor/robot3.png'
    imag_fuera_de_mapa = 'imag/Interfaz/fueradelmapa.png'

    def __init__(self):
        self.config = data.Configuracion()

        self.robot_animacion = False
        self.robot = robotlib.Mover_Robot()


        # actor que es el led de abajo!
        self.placalcd = pilas.actores.Actor(imagen='imag/Interfaz/placalcd.png', x=-100, y=-2000)
        self.placalcd.escala = 1


        # actor que es la imageen de engranajes de la izquierda
        self.imag_engr_izq = pilas.actores.Actor(imagen='imag/Interfaz/Engraizq_1.png', x=-1820, y=1)
        self.imag_engr_izq.escala = 1
        self.fin_x_chapa = -1078



        # actor que es la imageen de engranajes de la derecha
        self.imag_engr_der = pilas.actores.Actor(imagen='imag/Interfaz/Engrader.png', x=1820, y=1)
        self.imag_engr_der.escala = 1
        self.fin_x_chapa_dercha = 955


        # ENGRANAJE 1 Que SE MUEVE

        imag_engranaje = pilas.imagenes.cargar('imag/Interfaz/engra1.png')
        self.engranaje_1 = pilas.actores.Mono()
        self.engranaje_1.set_imagen(imag_engranaje)
        self.engranaje_1.x = 1670
        self.engranaje_1.y = -468

        imag_tele = pilas.imagenes.cargar_grilla('imag/Interfaz/tvmenor.png', 2)
        imag_tele.escala = 0.2
        self.tele = pilas.actores.Animacion(imag_tele, x=1820, y=180, ciclica=True, velocidad=50)


        # Joystick
        self.joystick = pilas.actores.Actor(imagen='imag/comando/Controles/jostick.png', x=949, y=-1085)


        # BOTON RUN
        self.boton_run = pilas.actores.boton.Boton(x=820, y=-1085, ruta_normal='imag/comando/Controles/runoff.png',
                                                   ruta_press='imag/comando/Controles/runon.png',
                                                   ruta_over='imag/comando/Controles/runover.png')
        self.boton_run.conectar_presionado(self.__run)
        self.boton_run.conectar_sobre(self.boton_run.pintar_sobre)
        self.boton_run.conectar_normal(self.boton_run.pintar_normal)



        # BOTON ROBOT
        self.boton_robot = pilas.actores.boton.Boton(x=1100, y=-1085, ruta_normal='imag/comando/Controles/robotnul.png',
                                                     ruta_press='imag/comando/Controles/roboton.png',
                                                     ruta_over='imag/comando/Controles/robotover.png')
        self.boton_robot.conectar_presionado(self.__run)
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_sobre)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_normal)


        # actor que es la grilla
        self.imag_grilla = pilas.actores.Actor(imagen='imag/Interfaz/grilla.png', x=-140, y=1200)


        self.imag_fueradelmapa()  # se crea la imagen con transparencia 100% para que quede por debajo del robot



        # TAREA Y VARIABLES QUE SE ENCARGA DE GIRAR EL ENGRANAJE
        self.giro = 0
        self.engranaje_estado = True
        self.factor = 0
        self.velocidad = 1
        self.tarea_engranaje = pilas.mundo.agregar_tarea(0.01, self.girar_engranaje)
        self.tarea_stop_engranaje = pilas.mundo.agregar_tarea(1.6, self.stop_engranaje)

        self.botones = botones.botones()


        if self.config.graficos == True and self.config.lvlup==False:
            self.placalcd.y = pilas.interpolar(-390, tipo='lineal', demora=1, duracion=4)
            self.imag_engr_izq.x = pilas.interpolar(self.fin_x_chapa, tipo='lineal', demora=1, duracion=2)
            self.imag_engr_der.x = pilas.interpolar(self.fin_x_chapa_dercha, tipo='lineal', demora=1, duracion=2)
            self.engranaje_1.x = pilas.interpolar(775, tipo='lineal', demora=1, duracion=2)
            self.tele.x = pilas.interpolar(1100, tipo='lineal', demora=4, duracion=2)
            self.joystick.y = pilas.interpolar(-485, tipo='lineal', demora=4, duracion=2)
            self.boton_run.y = pilas.interpolar(-485, tipo='lineal', demora=4, duracion=2)
            self.boton_robot.y = pilas.interpolar(-485, tipo='lineal', demora=4, duracion=2)
            self.imag_grilla.y = pilas.interpolar(110, tipo='elastico_final', demora=3, duracion=4)
            # TAREA QUE HABILITA LOS BOTONES DE LOS NUMEROS Y COMANDOS
            self.tarea_habilitar_botones = pilas.mundo.agregar_tarea(7, self.habilitar_botones)




        else:
            self.placalcd.y = -390
            self.imag_engr_izq.x = self.fin_x_chapa
            self.imag_engr_der.x = self.fin_x_chapa_dercha
            self.engranaje_1.x = 775
            self.tele.x = 1100
            self.joystick.y = -485
            self.boton_run.y = -485
            self.boton_robot.y = -485
            self.imag_grilla.y = 110
            self.imag_grilla.y = 110
            # TAREA QUE HABILITA LOS BOTONES DE LOS NUMEROS Y COMANDOS
            self.tarea_habilitar_botones = pilas.mundo.agregar_tarea(2, self.habilitar_botones)

    def __move_robot(self):
        # ACA ES DONDE SE MANDA LA LISTA CON LOS MOVIMIENTOS
        print ('intentado mover')
        self.robot.mover(self.lista_movimientos)
        print self.lista_movimientos

    def habilitar_boton_robot(self, instancia_botones):
        self.lista_movimientos = instancia_botones.get_movimientos()
        self.boton_robot.conectar_presionado(self.__move_robot)
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_sobre)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_presionado)

    def deshabilitar_boton_robot(self):
        self.boton_robot.conectar_presionado(self.__run)  # no gace nada run tiene un pass
        self.boton_robot.conectar_sobre(self.boton_robot.pintar_normal)
        self.boton_robot.conectar_normal(self.boton_robot.pintar_normal)

    def _fueradelmapatransparencia(self):
        self.trans = self.trans - 1
        self._fuera_del_mapa.transparencia = self.trans
        if self.trans < 0:
            return False
        else:
            return True

    def imag_fueradelmapa(self):
        # primero creo la imagen ., por una cuestion de superposicion de las cosas
        self._fuera_del_mapa = pilas.actores.Actor(self.imag_fuera_de_mapa, x=-140, y=80)
        self._fuera_del_mapa.z = -5
        self.trans = 100
        self._fuera_del_mapa.transparencia = 100

    def fueradelmapa(self):
        tarea_transparencia = pilas.mundo.agregar_tarea(0.01, self._fueradelmapatransparencia)

    def __run(self):
        pass

    def alternar_animacion_robot(self, r):
        if self.robot_animacion == False:
            r.actor.set_imagen(self.imagen_actor_robot_1)
            self.robot_animacion = True
            return True

        else:
            self.robot_animacion = False
            r.actor.set_imagen(self.imagen_actor_robot_2)
            return True

    def getInstanciaBotones(self):
        return self.botones

    def stop_engranaje(self):
        self.factor = 0.001
        return False

    def girar_engranaje(self):

        if self.velocidad >= 0:
            self.velocidad = self.velocidad - self.factor
            self.giro = self.giro + self.velocidad
            self.engranaje_1.rotacion = self.giro

            if self.giro == 360:
                self.giro = 0
            return True
        else:
            return False

    def habilitar_botones(self):
        self.botones.habilitar_botones(True)
        return False
