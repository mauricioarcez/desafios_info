from datetime import datetime

class Usuario:
    
    lista_usuarios = [] # Usuarios totales
    contador_id = 0 # Id auto-incremental
    
    def __init__(self,nombre,apellido,telefono,username,email,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self._telefono = telefono
        self.username = username.lower()
        self.email = email
        self.__contraseña = contraseña 
        
        self.fecha_registro = datetime.now() # Fecha actual
        self.avatar = 'avatar.png' # Por defecto
        self.estado = None
        self.online = False
        self.id = self.generador_id()
        self.lista_usuarios.append(self)
        
    def generador_id(self):
        Usuario.contador_id += 1
        return Usuario.contador_id
    
    def __repr__(self):
        return f'{self.username}'
    
    def login(self,username,contraseña):
        if self.username == username.lower() and self.__contraseña == contraseña:
            self.online = True
            print(f'\nBienvenido ¡{username}!')
        else:
            print('Usuario o contraseña ingresada no es correcta')
            
    def registrar():
        while True:
            usuario_disponible = True
            r_username = input('Ingrese un nombre de usuario para registrarse:\n-> ')
            
            for x in Usuario.lista_usuarios:
                if x.username == r_username:
                    print('El nombre de usuario ingresado se encuentra en uso')
                    usuario_disponible = False
                    break
            if usuario_disponible:
                r_contraseña = input('Ingrese una contraseña para iniciar sesion:\n-> ')
                r_email = input('Ingrese un email para verificar su cuenta:\n-> ')
                r_nombre = input('Ingrese su nombre real:\n-> ')
                r_apellido = input('Ingrese su apellido:\n-> ')
                r_telefono = input('Por ultimo ingrese su numero de telefono:\n-> ')
                print(f'¡Usuario creado con exito!, {r_username}\nAhora puedes iniciar sesion con tu username y tu contraseña.\n')
                r_username = Usuario(r_nombre,r_apellido,r_telefono,r_username,r_email,r_contraseña)
                break
            

x1 = Usuario('mauricio', 'arce', '3624822158', 'mauricioarcez', 'mauricioarcez23@gmail.com', '123mauri')
x2 = Usuario('juan','perez','3624678953','juancito01','juancito01@gmail.com','123juan')
x3 = Usuario('lionel','messi','3624638503','liomessi22','liomessi@gmail.com','messi35')

print(Usuario.lista_usuarios)
x1.login('mauricioarcez','123mauri')
print(x1.online)
print(x3.online)

Usuario.registrar()
print(Usuario.lista_usuarios)