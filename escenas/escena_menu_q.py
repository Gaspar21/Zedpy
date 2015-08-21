__author__ = 'cristian'
__author__ = 'cristian'
import pilas
import  escenas

class EscenaMenuq(pilas.escena.Base):

    def __init__(self,instancia_jugador):
        pilas.escena.Base.__init__(self)
        self.jugador=instancia_jugador


    def iniciar(self):
        p=pilas.actores.Sonido()
        self.chapa=pilas.actores.Actor(imagen='imag/escmenu/Inicio-4.png',x=0,y=0 )
        self.chapa.escala=1
        self.fondo = pilas.fondos.Fondo("./imag/Interfaz/fondo.png")


        self.boton_reanudar=pilas.actores.boton.Boton(x=-740,y=200,ruta_normal='imag/escmenu/reanudar1.png', ruta_press='imag/escmenu/reanudar2.png', ruta_over='imag/escmenu/reanudar2.png')
        self.boton_reanudar.conectar_presionado(self.ir_a_escena_anterior1)
        self.boton_reanudar.conectar_sobre(self.boton_reanudar.pintar_presionado)
        self.boton_reanudar.conectar_normal(self.boton_reanudar.pintar_normal)

        self.boton_jugar=pilas.actores.boton.Boton(x=-740,y=-240,ruta_normal='imag/escmenu/reiniciar1.png', ruta_press='imag/escmenu/reiniciar2.png', ruta_over='imag/escmenu/reiniciar2.png')
        self.boton_jugar.conectar_presionado(self.reiniciar)
        self.boton_jugar.conectar_sobre(self.boton_jugar.pintar_presionado)
        self.boton_jugar.conectar_normal(self.boton_jugar.pintar_normal)

        self.boton_opc=pilas.actores.boton.Boton(x=-740,y=-100,ruta_normal='imag/escmenu/opciones1.png', ruta_press='imag/escmenu/opciones2.png', ruta_over='imag/escmenu/opciones2.png')
        self.boton_opc.conectar_presionado(self._opciones)
        self.boton_opc.conectar_sobre(self.boton_opc.pintar_presionado)
        self.boton_opc.conectar_normal(self.boton_opc.pintar_normal)




        self.boton_salir=pilas.actores.boton.Boton(x=-740,y=-370,ruta_normal='imag/escmenu/salir1.png', ruta_press='imag/escmenu/salir2.png', ruta_over='imag/escmenu/salir2.png')
        self.boton_salir.conectar_presionado(self.salir)
        self.boton_salir.conectar_sobre(self.boton_salir.pintar_presionado)
        self.boton_salir.conectar_normal(self.boton_salir.pintar_normal)

        self.pulsa_tecla_escape.conectar(self.ir_a_escena_anterior)

    def ir_a_escena_anterior(self, evento):
        pilas.recuperar_escena()

    def ir_a_escena_anterior1(self):
        pilas.recuperar_escena()

    def _opciones(self):
       pilas.almacenar_escena(escenas.Opciones())



    def reiniciar(self):
        pilas.almacenar_escena(escenas.Reiniciar(self.jugador))

    #def comenzar(self):
    #    self.jugador.nivel=0
    #    self.jugador.deletedatos()
    #    pilas.cambiar_escena(escenas.escena_juego.iniciar(self.jugador,'newlevel'))

    def salir(self):
        import sys
        sys.exit(0)

iniciar=EscenaMenuq