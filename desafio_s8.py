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
		print(' _________________________________________________________________ ')
		print('|                                                                 |')
		print('|   INFOnews                  [1.Registrarse] [2.Iniciar sesion]  |')
		print('|_________________________________________________________________|')
		print('|   _____________________      _____________________              |')
		print('|  |                     |    |                     |             |')
		print('|  |   [Inicia sesion]   |    |   [Inicia sesion]   |             |')
		print('|  | para leer articulos |    | para leer articulos |             |')
		print('|  |  [ARTICULO OCULTO]  |    |  [ARTICULO OCULTO]  |             |')
		print('|  |_____________________|    |_____________________|             |')
		print('|  . Titulo oculto            . Titulo oculto                     |')
		print('|                                                                 |')
		print('|                                                                 |')
		print('|   PRESIONE 1 PARA REGISTRARSE                                   |')
		print('|   PRESIONES 2 PARA INICIAR SESION [Si esta registrado]          |')
		print('|_________________________________________________________________|\n')

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
				return False

			elif decision == 2:
				nombre_usuario = input('Ingrese su nombre de usuario:\n-> ')
				contraseña = input('Ingrese su contraseña:\n-> ')
				self.login(nombre_usuario,contraseña)
				return False
			else:
				print('Opciones no disponibles\n')
				return False

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




