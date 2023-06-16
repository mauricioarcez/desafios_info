from datetime import datetime

class Usuario:
    contador_id = 0
    usuarios_registrados = []
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
        self._telefono = None
        self.username = None
        self.email = None
        self.__contraseña = None 
        self.fecha_registro = None
        self.avatar = None
        self.estado = None
        self.online = None
        self.id = None
               
    def registrar(self, username, contraseña, email, telefono):
        self.username = username.lower()
        self.__contraseña = contraseña
        self.email = email
        self._telefono = telefono
        
        self.fecha_registro = datetime.now()
        self.avatar = 'avatar.png' 
        self.estado = '--'
        self.online = False
        self.id = self.generador_id()
        
    def __repr__(self):
        return f'{self.username}'   
    
    def generador_id(self): 
        if self.username is not None:
            Usuario.contador_id += 1
            Usuario.usuarios_registrados.append(self)
            return Usuario.contador_id
    
    def login(self, username, contraseña):
        if self.username == username.lower() and self.__contraseña == contraseña:
            self.online = True
            print(f'\n.... INICIANDO SESION ....\n Bienvenido ¡{username}!\n')
        else:
            print('Usuario o contraseña ingresada no es correcta')
            

x1 = Usuario('mauricio','arce')
x2 = Usuario('juan','perez')

x1.registrar('mauricioarcez','123456','mauricioarcez23@gmail.com',3624822158)
x2.registrar('juanperez14','14juan','juancito01@gmail.com',232234294)

print(x2.id)
print(Usuario.usuarios_registrados)

x1.login('mauricioarcez','fake')
x2.login('juanperez14','14juan')

