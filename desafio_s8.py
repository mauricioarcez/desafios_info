from datetime import datetime
import textwrap

class Usuario:
	usuarios_registrados = []
	usuario_existente = False

	def __init__(self):
		self.estado = '--'  # Por defecto
		self.avatar = 'avatar.png'  # Por defecto
		self.id = 'Registrese para obtener un ID de usuario\n'

		self.nombre = None
		self.apellido = None
		self.telefono = None
		self.username = None
		self.email = None
		self.__contraseña = None
		self.fecha_registro = None
		self.online = False

	def __repr__(self):
		return f'{self.username}'

	def registrar(self, username, contraseña, nombre, apellido, telefono, email):
		self.username = username.lower()
		self.__contraseña = contraseña
		self.nombre = nombre
		self.apellido = apellido
		self.telefono = telefono
		self.email = email
		self.fecha_registro = datetime.now()  # Fecha actual de registro

		for user in Usuario.usuarios_registrados:
			if user.username == username.lower():
				self.usuario_existente = True
				break
		if self.usuario_existente == False:
			self.usuarios_registrados.append(self)
			self.id = len(self.usuarios_registrados)
			print(f'Usuario registrado con exito. ¡Bienvenido {username}! Ahora puedes leer articulos.\n')
		else:
			print('El nombre de usuario elegido ya se encuentra en uso.\n')

	def login(self, username, contraseña):
		for user in self.usuarios_registrados:
			if user.username == username and user.__contraseña == contraseña:
				print(f'              ...INICIANDO SESION...\nBienvenido {self.username}, estos son los articulos destacados de hoy.\n')
				self.online = True
				return
		print('Usuario o contraseña ingresada es incorrecta\n')
    
	def menu(self):
		def menu_principal():
			print(' _________________________________________________________ ')
			print('|                                                         |')
			print('|   INFOnews          [1.Registrarse] [2.Iniciar sesion]  |')
			print('|_________________________________________________________|')
			print('|   _____________________     _____________________       |')
			print('|  |                     |   |                     |      |')
			print('|  |   [Inicia sesion]   |   |   [Inicia sesion]   |      |')
			print('|  | para leer articulos |   | para leer articulos |      |')
			print('|  |  [ARTICULO OCULTO]  |   |  [ARTICULO OCULTO]  |      |')
			print('|  |_____________________|   |_____________________|      |')
			print('|  . Titulo oculto           . Titulo oculto              |')
			print('|                                                         |')
			print('|                                                         |')
			print('| PRESIONE 1 PARA REGISTRARSE                             |')
			print('| PRESIONES 2 PARA INICIAR SESION [Si esta registrado]    |')
			print('| PRESIONES 3 PARA PUBLICAR UN ARTICULO [Si es colab]     |')
			print('| PRESIONES 4 PARA COMENTAR UN ARTICULO [publico/colab]   |')
			print('|_________________________________________________________|\n')
		menu_principal()
  
		def mostrar_contenido():
			if self.online:
				print(f' ______________________________________________')
				print(f'|                                              ')
				print(f'|   INFOnews                 [5.Cerrar Sesion] ')
				print(f'|______________________________________________')
				print(f'|   _________________________________________  ')
				print(f'|  |ID-Articulo#{a1.id}                        ')
				print(f'|  |                                           ')
				print(f'|  |                {a1.imagen}.png            ')
				print(f'|  |                                           ')
				print(f'|  |_________________________________________  ')
				print(f'|  .{a1.titulo} [4]                            ')
				print(f'|  -{a1.fecha_publicada}                       ')
				print(f'|   _________________________________________  ')	
				print(f'|  |ID-Articulo#{a2.id}                        ')
				print(f'|  |                                           ')
				print(f'|  |               {a2.imagen}.png             ')
				print(f'|  |                                           ')
				print(f'|  |_________________________________________  ')
				print(f'|  .{a2.titulo} [4]                            ')
				print(f'|  -{a2.fecha_publicada}                       ')
				print(f'|                                              ')
				print(f'| PRESIONE 3 PARA AGREGAR UN ARTICULO          ')
				print(f'| PRESIONE 4 PARA COMENTAR UN ARTICULO.        ')
				print(f'| PRESIONE 5 PARA CERRAR SESION.               ')
				print(f'|______________________________________________\n')

		while True:
   
			decision = int(input('Ingrese su eleccion:\n-> '))
   
			if decision == 1:
				nombre_usuario = input('Ingrese su nombre de usuario:\n-> ')
				contraseña = input('Ingrese su contraseña:\n-> ')
				nombre = input('Ingrese su nombre:\n-> ')
				apellido = input('Ingrese su apellido:\n-> ')
				telefono = input('Ingrese su telefono:\n-> ')
				email = input('Ingrese su email:\n-> ')

				self.registrar(nombre_usuario,contraseña,nombre,apellido,telefono,email)
				username = nombre_usuario
				password = contraseña
				iniciar = int(input('Desea Inciar sesion? 1/2\n1->SI.\n2->NO.\n-> '))
				if iniciar == 1:
					self.login(nombre_usuario,contraseña)
					mostrar_contenido()
				else:
					print('Hasta luego!..\n')
					menu_principal()

			elif decision == 2:
				try:
					self.login(username,password)
					mostrar_contenido()
				except Exception:
					print('Debes registrarte para iniciar sesion en una cuenta.\n')
					menu_principal()
     
			elif decision == 3:
				pregunta = int(input('Desea registrarse como colaborador?\n1->SI.\n2->NO.\n-> '))
				if pregunta == 1 and self.online:
					c1 = Colaborador(self)
					c1.registrar()
					
					if self.es_colaborador:
						titulo = input('Ingrese un titulo llamativo para su articulo:\n-> ').upper()
						resumen = input('Ingrese un resumen del titulo:\n-> ').capitalize()
						contenido = input('Ingrese el contenido explicativo de su articulo:\n-> ')
						imagen = input('Ingrese la imagen que resaltara el articulo:\n-> ')
			
						c1.publicar(titulo,resumen,contenido,imagen)
						artic = Articulo.articulos_publicados[-1]
							
						print(f' __________________________________________________')
						print(f'|                                                  ')
						print(f'|   INFOnews                    [5.Cerrar Sesion ] ')
						print(f'|__________________________________________________')
						print(f'|   _____________________________________________  ')
						print(f'|  |ID-Articulo#{artic.id}                         ')
						print(f'|  |                                               ')
						print(f'|  |               {artic.imagen}.png              ')
						print(f'|  |                                               ')
						print(f'|  |_____________________________________________  ')
						print(f'|  .{artic.titulo}                                 ')
						print(f'|  AUTOR: {self.username}, ID#{self.id}            ')
						print(f'|       {artic.resumen}                            ')
						print(f'|                                                  ')
						print(f'|    \"{artic.contenido}\"                       \n')
				else:
					print('Inicie sesion para probar esta funcion.\nHasta luego..')
					menu_principal()
     
			elif decision == 4:

				def mostrar_comentario():
					ultimo = Comentario.lista_comentarios[-1]
					for articulo in Articulo.articulos_publicados:
						if articulo.id == id_art:
							titu = articulo.titulo
							titu_contenido = articulo.contenido
							break
					wrap = textwrap.wrap(titu_contenido,width=40)

					print(f' ___________________________________________ ')
					print(f'|                                            ')
					print(f'|          {titu}                            ')
					print(f'| \"{wrap[0]}                                ')
					print(f'| {wrap[1]}                                  ')
					print(f'| {wrap[2]}\"                                ')
					print(f'|___________________________________________ ')
					print(f'|   _______   _____________________________  ')
					print(f'|  |  _w   | |{self.username}:               ')
					print(f'|  | _(")_ | |  {ultimo.contenido}           ')
					print(f'|  |/|___|\| |_____________________________  ')
					print(f'|                         {ultimo.fecha_hora}')
					print(f'|   ___   _________________________________  ')
					print(f'|  | 0 | |Escribir comentario... [4]         ')
					print(f'|  |/_\| |_________________________________\n')

				pregunta2 = int(input('Desea comentar como publico[1] o como colaborador[2] ?\n1->PUBLICO.\n2->COLABORADOR.\n-> '))

				if pregunta2 == 1 and self.online:		
					p1 = Publico(self)
					p1.registrar()
					if self.es_publico:
						id_art = int(input('Ingrese el ID del articulo que desea comentar.\n-> '))
						contenido_coment = input('Escriba su comentario:\n-> ')
						p1.comentar(id_art,contenido_coment)
						mostrar_comentario()
							
				elif pregunta2 == 2 and self.online:		
					c1 = Colaborador(self)
					c1.registrar()
					if self.es_colaborador:
						id_art = int(input('Ingrese el ID del articulo que desea comentar.\n-> '))
						contenido_coment = input('Escriba su comentario:\n-> ')
						c1.comentar(id_art,contenido_coment)
						mostrar_comentario()
				else:
					print('Inicie sesion para probar esta funcion.\nHasta luego..')
					menu_principal()
      
			elif decision == 5:
				print('Has cerrado sesion.. Ingrese cualquier numero MAYOR a 5 para terminar el programa.\nNos vemos pronto..')
				menu_principal()
    
			else:
				print('Opciones no disponibles. Gracias por visitar INFOnews.')
				return False

class Articulo():

    articulos_publicados = []

    def __init__(self, titulo, resumen, contenido, imagen, id_usuario):
        self.titulo = titulo.upper()
        self.resumen = resumen.capitalize()
        self.contenido = contenido
        self.imagen = imagen
        self.id_usuario = id_usuario

        self.estado = 'Activo'
        self.fecha_publicada = datetime.now()
        Articulo.articulos_publicados.append(self)
        self.id = len(Articulo.articulos_publicados)

    def __repr__(self):
        return f'{self.titulo}'

class Comentario():
    
    contador_id = 0
    lista_comentarios = []
    
    def __init__(self,id_articulo,contenido,id_usuario):
        self.id_articulo = id_articulo
        self.contenido = contenido
        self.id_usuario = id_usuario
        
        Comentario.contador_id += 1
        self.id = Comentario.contador_id
        self.fecha_hora = datetime.now()
        self.estado = 'Activo'
        self.lista_comentarios.append(self)
        
        
class Publico(Usuario):

	publico_existente = False

	def __init__(self, usuario):
		super().__init__()
		self.__dict__ = usuario.__dict__  # Copia todos los atributos del usuario
		self.es_publico = False

	def registrar(self):
		for user in Usuario.usuarios_registrados:
			if user.username == self.username:
				self.es_publico = True
				self.publico_existente = True
				print(f'{self.username}, ¡Te has registrado como publico, ahora puedes comentar articulos!\n')
				break
		if self.publico_existente == False:
			print('Debes registrarte como usuario, para luego registrarte como publico\n')

	def comentar(self,id_articulo,contenido):
		if self.es_publico:
			contenido = Comentario(id_articulo,contenido,self.id)
			print('Comentario publicado.\n')
		else:
			print('Debes registrarte como publico o colaborador para comentar articulos.\n')

class Colaborador(Usuario):
    
	colaborador_existente = False

	def __init__(self, usuario):
		self.__dict__ = usuario.__dict__  # Copia todos los atributos del usuario
		self.es_colaborador = False

	def	registrar(self):
		for user in Usuario.usuarios_registrados:
			if user.username == self.username:
				self.es_colaborador = True
				self.colaborador_existente = True
				print(f'{self.username}, ¡Te has registrado como colaborador, ahora puedes publicar y comentar articulos!\n')
				break
		if self.colaborador_existente == False:
			print('Debes registrarte como usuario, para luego registrarte como colaborador\n')

	def comentar(self, id_articulo, contenido):
		if self.es_colaborador:
			contenido = Comentario(id_articulo, contenido, self.id)
			print('Comentario publicado.\n')
		else:
			print('Debes registrarte como publico o colaborador para comentar articulos.\n')

	def publicar(self,titulo,resumen,contenido,imagen):
		if self.es_colaborador == True:
			Articulo(titulo, resumen, contenido, imagen, self.id)
			print(f'Artículo publicado con éxito.\n')
			
		else:
			print('Debes registrarte como colaborador para poder publicar artículos.\n')




#Creacion de 2 usuarios. con solo avatar y estado predefinidos y sus otros atributos en None hasta que se registren.
u1 = Usuario()
u2 = Usuario()

#Creacion de 2 Articulos definidos para comentar
a1 = Articulo('BOCA VOLVIO A PERDER DE LOCAL','La derrota fue contra Arsenal por 3 a 0 en la Bombonera.','contenido extenso de prueba porque no se que escribir aqui, pero se supone debe ser un poco largo','imagen.boca',1)
a2 = Articulo('Chaco for ever tiene nuevos refuerzos', 'se trata de Lionel Messi jugador que viene desde el PSG de Francia.','Contenido extenso de prueba porque no se que escribir aqui, pero se supone debe ser un poco largo','imagen.chaco',2)

#Menu intuitivo a seguir los pasos para registrarse, inicar sesion, comentar, publicar.
Usuario.menu(u1)



