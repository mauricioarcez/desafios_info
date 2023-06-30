import datetime
año_actual = datetime.datetime.now().year

#Lista de inmuebles para agregar/modificar/eliminar
inmuebles = [
    {'id':1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'id':2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'id':3, 'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'id':4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'id':5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

# Funcion para validar datos
def validar_datos(mensaje,tipo,min_valor=None,max_valor=None,condiciones=None):
    
    '''Valida los datos ingresados para que los enteros sean enteros, los strings sean str, y los booleanos bool. Recibe un input como mensaje. Luego debes definir el tipo(str,int,bool), el valor minimo en caso de elegir int y su valor maximo. O las condiciones para que sea aceptado en caso de elegir str'''
    
    while True:
        entrada = input(mensaje)
        if tipo == 'int':
            try:
                valor = int(entrada)
                if min_valor is not None and valor < min_valor:
                    print(f'Error: El valor debe ser igual o mayor que {min_valor}')
                    continue
                if max_valor is not None and valor > max_valor:
                    print(f'Error: El valor debe ser igual o menor que {max_valor}')
                    continue
                if condiciones and entrada not in condiciones:
                    print(f'Error: El valor debe estar en {condiciones}')
                    continue
                return valor
            except ValueError:
                print('Error: Debe ingresar un valor entero')
        elif tipo == 'bool':
            if entrada.lower() == 'true':
                valor = True
            elif entrada.lower() == 'false':
                valor = False
            else:
                print('Error: Debe ingresar "true" o "false"')
                continue
            return valor
        elif tipo == 'str':
            if condiciones and entrada not in condiciones:
                print(f'Error: El valor debe estar en {condiciones}')
                continue
            return entrada
        else:
            print(f'Error: Tipo de entrada no valido.')
        
# Funcion para agregar un inmueble nuevo a la lista
def agregar_inmueble():
    
    ''' Crea un dict(nuevo_inmueble) y lo agrega a list(inmuebles). no necesita parametros, se va creando mediante preguntas al usuario.'''
    
    inmueble = {'id':None, 'año': None, 'metros': None, 'habitaciones':None, 'garaje': None, 'zona': None, 'estado': None }

    inmueble['año'] = validar_datos('Ingrese año de creacion del inmueble: ','int',2000,año_actual)
    
    inmueble['metros'] = validar_datos('Ingrese los metros cuadrados del inmueble: ','int',60)
    
    inmueble['habitaciones'] = validar_datos('Ingrese cuantas habitaciones posee el inmueble: ','int',2)
    
    inmueble['garaje'] = validar_datos('Ingrese si el inmueble posee garaje. Escriba true/false: ','bool',condiciones={True,False})
    
    inmueble['zona'] = validar_datos('Ingrese la zona del Inmueble.\nLas zonas aceptadas son A, B, C. en Mayusculas: ','str',condiciones={'A','B','C'})
    
    inmueble['estado'] = validar_datos('Ingrese el estado del inmueble.\nEste debe ser Disponible, Reservado o Vendido. Con su primer letra en Mayuscula: ','str',condiciones={'Disponible','Reservado','Vendido'})
     
    # Asigna un ID unico.
    ids_existentes = set()
    for inmueble_actual in inmuebles:
        ids_existentes.add(inmueble_actual['id'])
       
    id_faltante = 1
    while id_faltante in ids_existentes:
        id_faltante += 1
    inmueble['id'] = id_faltante
                
    inmuebles.append(inmueble)
    print(f'\nInmueble agregado con exito!\n{inmueble}')
       
#Funcion para editar un inmueble 
def editar_inmueble(id_inmueble,atributo):
    
    '''Cambia el valor de la clave de un inmueble.
    Recibe 2 parametros en este orden: 1.El id del inmueble. 2.La caracteristica del inmueble. El nuevo valor sera preguntado en la funcion.
    permite caracteristicas en mayusculas y minusculas pero debe ser siempre agregada entre comillas.'''
    
    atributo_minus = atributo.lower()
    print(f'En el inmueble seleccionado:\n{inmuebles[id_inmueble-1]}\n')
    valor_antiguo = inmuebles[id_inmueble-1][atributo_minus]
        
    if atributo_minus == 'año':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para {atributo}: ", 'int',2000,año_actual)
    elif atributo_minus == 'metros':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para {atributo}: ", 'int', 60)
    elif atributo_minus == 'habitaciones':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para {atributo}: ", 'int', 2)
    elif atributo_minus == 'garaje':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para {atributo}: ", 'bool', condiciones={True,False})
    elif atributo_minus == 'zona':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para{atributo}: ", 'str', condiciones={'A','B','C'})
    elif atributo_minus == 'estado':
        nuevo_valor = validar_datos(f"Ingrese el nuevo valor para {atributo}: ", 'str', condiciones={'Disponible','Reservado','Vendido'})
    else:
        print(f'{atributo.upper()} No es una caracteristica editable\n')
    
    inmuebles[id_inmueble-1][atributo_minus] = nuevo_valor
    print(f'has cambiado {atributo_minus}: {valor_antiguo} a {atributo_minus}: {nuevo_valor}')
    
    
# Funcion para eliminar un inmueble de la lista     
def eliminar_inmueble(id_inm):
    
    '''Elimina un inmueble de la lista segun el ID que se le pase como argumento. Imprime la lista eliminada'''
    
    if id_inm > len(inmuebles):
        print('El ID seleccionado no se encuentra en la lista de inmuebles.')
    else:
        print(f"\nHas eliminado este inmueble de la lista:\n{inmuebles[id_inm-1]}")
        inmuebles.remove(inmuebles[id_inm-1])

# Funcion para buscar inmuebles segun un presupuesto    
def busqueda(lista,presupuesto):
    
    '''Busca los inmuebles Disponibles o Reservados que sean menor o igual a un presupuesto dado por el usuario e imprime en pantalla una lista de inmuebles filtrados que cumplan los requisitos'''
    
    def calcular_precio_inmueble(diccionario):
        
        '''calcula el precio de un inmueble particular. funciona solo localmente. recibe como parametro un diccionario de la lista de inmuebles'''
        
        precio_base = diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500
        antiguedad = año_actual - diccionario['año']
        
        if diccionario['zona'] == 'A':
            precio = precio_base * (1 - antiguedad / 100)
        elif diccionario['zona'] == 'B':
            precio = precio_base * (1 - antiguedad / 100)* 1.5
        else:
            precio = precio_base * (1 - antiguedad / 100) * 2
        return precio
	
    # Crea una lista de inmuebles vacia y agrega las que cumplan el presupuesto
    inmuebles_accesibles = []
    for inmueble in lista:
        if presupuesto >= calcular_precio_inmueble(inmueble):
            if inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado':
                # Agrega el precio al diccionario y luego el diccionario a la lista.
                inmueble['precio'] = calcular_precio_inmueble(inmueble)
                inmuebles_accesibles.append(inmueble)
    if len(inmuebles_accesibles) >= 1:
        print(f'Aqui tienes una lista de inmuebles que sean menor o igual a tu presupuesto y su estado sea Disponible o Reservado:')
        for inmueble in inmuebles_accesibles:
            print(inmueble)
    else:
        print('Lo siento. No hay inmuebles Disponibles o Reservados por ese precio.')
        
'''
Participantes: 
Ivan
Alexis
Mauricio
Valentino

'''
