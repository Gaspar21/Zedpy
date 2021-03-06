__author__ = 'sym'
import pilas
import escenas
import data
import duinobot


class EscenaDeUsuarios(pilas.escena.Base):
    imag_consola_usuario = './imag/Interfaz/usuario/jugador.png'
    imag_ingrese_nombre = './imag/Interfaz/usuario/ingresanom.png'
    imag_fondo = './imag/Interfaz/fondo.png'
    imag_animacion = './imag/Interfaz/usuario/barra.png'
    imag_caja = './imag/Interfaz/usuario/caja.png'
    imag_ok_normal = './imag/Interfaz/usuario/jugadoragrega.png'
    imag_ok_press = './imag/Interfaz/usuario/jugadoragrega1.png'
    imag_ok_over = './imag/Interfaz/usuario/jugadoragrega1.png'
    imag_info = './imag/Interfaz/info.png'

    def __init__(self):
        pilas.escena.Base.__init__(self)
        self.datos = data.Manager()
        self.block_ok = False
        self.alternar_imag=False

    def iniciar(self):

        self.fondo = pilas.fondos.Fondo(self.imag_fondo)
        self.imagen_consola_usuarios = pilas.actores.Actor(self.imag_consola_usuario, x=-800, y=50)

        self.imag_barra = pilas.actores.Actor(self.imag_animacion, x=-800, y=360)

        imag_info = pilas.imagenes.cargar_grilla(self.imag_info, 18)
        self.imag_info = pilas.actores.Animacion(imag_info, x=1300, y=1000, ciclica=True, velocidad=10)
        self.imag_info.cuando_hace_click=self.informacion
        self.imag_info.y=pilas.interpolar(-600,duracion=2,demora=1,tipo='rebote_final')
        self.imag_info.escala=2
        self.imag_info.escala=[1],3



        # Imagen que pide que escribsa tu nombre si no lo has hecho
        self.ima_escribi_nombre = pilas.actores.Actor(self.imag_ingrese_nombre, x=0, y=0)
        self.ima_escribi_nombre.transparencia = 100
        self.ima_escribi_nombre.z=-5

        self.m = pilas.actores.Texto(texto='Nuevo Jugador', x=-1080, y=560, magnitud=70,
                                     fuente='./escenas/interfazusuario/AGENCYB.TTF')
        self.m = pilas.actores.Texto(texto='Jugadores:', x=-1145, y=300, magnitud=70,
                                     fuente='./escenas/interfazusuario/AGENCYB.TTF')

        self.box_name = pilas.interfaz.ingreso_de_texto.IngresoDeTexto(ancho=200, x=-900, y=440)
        self.box_name.solo_letras()
        self.box_name.imagen_caja = pilas.imagenes.cargar(self.imag_caja)
        self.box_name.escala = 3
        self.box_name.transparencia = 60

        self.boton_ok = pilas.actores.boton.Boton(x=-420, y=440, ruta_normal=self.imag_ok_normal,
                                                  ruta_press=self.imag_ok_press, ruta_over=self.imag_ok_over)
        self.boton_ok.conectar_presionado(self._ok)
        self.boton_ok.conectar_sobre(self.boton_ok.pintar_sobre)
        self.boton_ok.conectar_normal(self.boton_ok.pintar_normal)
        self.boton_ok.z = -1

        lista_judagores = self.datos.getJugadores()
        lista_judagores.sort()
        interfaz = escenas.interfaz(lista_judagores)
        interfaz.comenzar()




    def _borrar_texto_ingrese_nombre(self):
        self.ima_escribi_nombre.transparencia = [100], 1
        self.block_ok = False

    def _ok(self):
        # responde al boton OK

        name = self.box_name.texto
        if name <> '':
            lista_de_jugadores = self.datos.getJugadores()

            if self.datos.checkusuario(name) == False:
                # self.datos.guardar_jugador(jugador=str(name),datos={})
                pilas.cambiar_escena(escenas.escena_menu.iniciar(('noexiste', str(name))))
        elif name == '' and self.block_ok == False:
            self.ima_escribi_nombre.transparencia = [0], 1
            pilas.mundo.agregar_tarea(1.5, self._borrar_texto_ingrese_nombre)
            self.block_ok = True



    def informacion(self,evento):
        if self.alternar_imag==False:
            self.alternar_imag=True
            self.imag_informacion=pilas.actores.Actor(x=580,y=-490,imagen='./imag/informacion/burbuja.png')
            self.imag_informacion.transparencia=100

            self.imag_informacion_desarrollado=pilas.actores.Actor(x=300,y=-400,imagen='./imag/informacion/desarrollado.png')
            self.imag_informacion_desarrollado.transparencia=100

            self.imag_informacion_programador=pilas.actores.Actor(x=40,y=-490,imagen='./imag/informacion/programador.png')
            self.imag_informacion_programador.transparencia=100

            self.imag_informacion_cristian=pilas.actores.Actor(x=290,y=-460,imagen='./imag/informacion/cristian.png')
            self.imag_informacion_cristian.transparencia=100

            self.imag_informacion_cristian1=pilas.actores.Actor(x=295,y=-525,imagen='./imag/informacion/cristian1.png')
            self.imag_informacion_cristian1.transparencia=100

            self.imag_informacion_seba=pilas.actores.Actor(x=628,y=-460,imagen='./imag/informacion/seba.png')
            self.imag_informacion_seba.transparencia=100
            self.imag_informacion_seba1=pilas.actores.Actor(x=650,y=-525,imagen='./imag/informacion/seba1.png')
            self.imag_informacion_seba1.transparencia=100

            self.imag_informacion_gaspar=pilas.actores.Actor(x=1000,y=-460,imagen='./imag/informacion/gaspar.png')
            self.imag_informacion_gaspar.transparencia=100
            self.imag_informacion_gaspar1=pilas.actores.Actor(x=1026,y=-525,imagen='./imag/informacion/gaspar1.png')
            self.imag_informacion_gaspar1.transparencia=100



            self.animacion_info()

        else:
            self.imag_informacion.eliminar()
            self.imag_informacion.eliminar()
            self.imag_informacion_desarrollado.eliminar()
            self.imag_informacion_programador.eliminar()
            self.imag_informacion_cristian.eliminar()
            self.imag_informacion_cristian1.eliminar()
            self.imag_informacion_seba.eliminar()
            self.imag_informacion_seba1.eliminar()
            self.imag_informacion_gaspar.eliminar()
            self.imag_informacion_gaspar1.eliminar()
            self.alternar_imag=False



    def nada(self,event):
        pass
    def animacion_info(self):

        self.imag_informacion.transparencia=[0],2

        pilas.mundo.agregar_tarea(1,self.animacion_con_delay)
        pilas.mundo.agregar_tarea(2.2,self.animacion_con_delay2)
        pilas.mundo.agregar_tarea(2.5,self.animacion_con_delay3)
        pilas.mundo.agregar_tarea(2.8,self.animacion_con_delay4)



    def animacion_con_delay(self):
        self.imag_informacion_desarrollado.transparencia=[0],1.4
        self.imag_informacion_programador.transparencia=[0],1.4

    def animacion_con_delay2(self):
        self.imag_informacion_cristian.transparencia=[0],0.4
        pilas.mundo.agregar_tarea(0.3,self.a1)


    def animacion_con_delay3(self):
        self.imag_informacion_seba.transparencia=[0],0.4
        pilas.mundo.agregar_tarea(0.3,self.a2)

    def animacion_con_delay4(self):
        self.imag_informacion_gaspar.transparencia=[0],0.4
        pilas.mundo.agregar_tarea(0.3,self.a3)

    def a1(self):
        self.imag_informacion_cristian1.transparencia=[0],0.4
    def a2(self):
        self.imag_informacion_seba1.transparencia=[0],0.4

    def a3(self):
        self.imag_informacion_gaspar1.transparencia=[0],0.4



iniciar = EscenaDeUsuarios
