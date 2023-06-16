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
			print(f'Usuario registrado con exito, ¡Bienvenido {username}!\n')
		else:
			print('El nombre de usuario elegido ya se encuentra en uso.\n')

	def login(self, username, contraseña):
		for user in self.usuarios_registrados:
			if user.username == username and user.__contraseña == contraseña:
				print(f'...INICIANDO SESION...\nBienvenido {self.username}\n')
				self.online = True
				return
		print('Usuario o contraseña ingresada es incorrecta\n')


x1 = Usuario()
x2 = Usuario()
x3 = Usuario()

print(Usuario.usuarios_registrados)
x1.registrar('mauricioarcez', '123mauri', 'mauricio','arce', 3624822158, 'mauricioarcez23@gmail.com')
x2.registrar('mauricioarcez', 'mauuu', 'mauricio', 'arce', 1176849284, 'mauricio_arce@gmail.com.ar')
print(Usuario.usuarios_registrados)
print(x1.id)
print(x2.id)
x1.login('mauricioarcez', '123mauri')
