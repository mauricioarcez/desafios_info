from datetime import datetime

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
				print(' _________________________________________________________ ')
				print('|                                                         |')
				print('|   INFOnews                          [5.Cerrar Sesion ]  |')
				print('|_________________________________________________________|')
				print('|   _____________________     _______________________     |')
				print('|  | ID#1                |   | ID#                   |    |')
				print('|  |                     |   |                       |    |')
				print('|  |   Boca.imagen.png   |   | + [PUBLICAR ARTICULO] |    |')
				print('|  |                     |   |                       |    |')
				print('|  |_____________________|   |_______________________|    |')
				print('|  .BOCA VOLVIO A PERDER     .PRESIONE 3 PARA AGREGAR     |')
				print('|   DE LOCAL. [4]             UN ARTICULO                 |')
				print('|                                                         |')
				print('| PRESIONE 4 PARA COMENTAR UN ARTICULO.                   |')
				print('| PRESIONE 5 PARA ABANDONAR INFOnews.                     |')
				print('|_________________________________________________________|\n')

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
				se_registro = True
				username = nombre_usuario
				password = contraseña
				iniciar = int(input('Desea Inciar sesion? 1/2\n1->SI.\n2->NO.\n-> '))
				if iniciar == 1:
					self.login(nombre_usuario,contraseña)
					mostrar_contenido()
				else:
					print('Hasta luego!..\n')
					menu_principal()
					continue

			elif decision == 2 and se_registro == True:
				self.login(username,password)
				mostrar_contenido()

			elif decision == 3:
				publicar = input('Para publicar articulos debes ser colaborador.\nDeseas registrarte como colaborador?\n1->SI\n2->NO.\n-> ')
				if publicar == 1:
					u1 = Usuario()
					u1.registrar(nombre_usuario,contraseña,nombre,apellido,telefono,email)
					c1 = Colaborador(u1)
					c1.registrar()
					titulo = input('Ingrese un titulo llamativo para su articulo:\n-> ').upper()
					resumen = input('Ingrese un resumen del titulo:\n-> ').capitalize()
					contenido = input('Ingrese el contenido explicativo de su articulo:\n-> ')
					imagen = input('Ingrese la imagen que resaltara el articulo:\n-> ')

					titulo = c1.publicar(titulo,resumen,contenido,imagen,self.id)
					print(f' ___________________________________________________ ')
					print(f'|                                                    ')
					print(f'|   INFOnews                     [5.Cerrar Sesion ]  ')
					print(f'|____________________________________________________')
					print(f'|   __________________________________')
					print(f'|  | ID#{titulo.id}')
					print(f'|  |                                          ')
					print(f'|  |               {titulo.imagen}.png')
					print(f'|  |                                          ')
					print(f'|  |___________________________________')
					print(f'|  .{titulo.titulo}')
					print(f'|    AUTOR: {self.username},ID#{self.id}')
					print(f'| \"{titulo.resumen}')
					print(f'|')
					print(f'|    {titulo.contenido}')
				else:
					print('Debes registrarte como usuario primero antes de ser Colaborador.')
					continue
					

class Articulo():

    articulos_publicados = []

    def __init__(self, titulo, resumen, contenido, imagen, id_usuario):
        self.titulo = titulo
        self.resumen = resumen
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
    
    def __init__(self,id_articulo,contenido,id_usuario):
        self.id_articulo = id_articulo
        self.contenido = contenido
        self.id_usuario = id_usuario
        
        Comentario.contador_id += 1
        self.id = Comentario.contador_id
        self.fecha_hora = datetime.now()
        self.estado = 'Activo'
    
    def __repr__(self):
        return f'{self.contenido}'
        

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
		if self.es_colaborador:
			titulo = Articulo(titulo, resumen, contenido, imagen, self.id)
			print(f'Artículo publicado con éxito.\n')
			
		else:
			print('Debes registrarte como colaborador para poder publicar artículos.\n')




#Creacion de usuario. con solo avatar y estado.
u1 = Usuario()

#Menu intuitivo a seguir los pasos para registrarse o inicar sesion.
u1.menu()



