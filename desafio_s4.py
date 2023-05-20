#Lista de inmuebles para agregar/modificar/eliminar
inmuebles = [
    {'id':1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'id':2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'id':3, 'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'id':4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'id':5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

# Funcion para agregar un inmueble nuevo a la lista
def agregar_inmueble():
    
    ''' Crea un dict(nuevo_inmueble) y lo agrega a list(inmuebles). no necesita parametros, se va creando mediante preguntas al usuario.'''
    
    inmueble = {'id':None, 'año': None, 'metros': None, 'habitaciones':None, 'garaje': None, 'zona': None, 'estado': None }

    while True:
        año_ingresado = input('Ingrese numericamente el año de creacion del inmueble:\n-> ')
        if año_ingresado.isdigit() and int(año_ingresado) >= 2000:
            año_ingresado = int(año_ingresado)
            inmueble['año'] = año_ingresado
            print(f'Datos Guardados. AÑO = {año_ingresado}\n')
        else:
            print('No operamos con inmuebles anteriores al año 2000 o forma no numerica')
            continue

        metro_ingresado = input('Ingrese los metros cuadrados del inmueble:\n-> ')
        if metro_ingresado.isdigit() and int(metro_ingresado) >= 60:
            metro_ingresado = int(metro_ingresado)
            inmueble['metros'] = metro_ingresado
            print(f'Datos guardados. METROS = {metro_ingresado}\n')
        else:
            while True:
                print('No operamos con inmuebles menores a 60 metros cuadrados')
                x = input('Ingrese un valor en metros cuadrados valido:\n-> ')
                if x.isdigit() and int(x) >= 60:
                    x = int(x)
                    inmueble['metros'] = x
                    print(f'Datos guardados. METROS = {x}\n')
                    break
                else:
                    continue
    
        habitacion_ingresado = input('Ingrese la cantidad numerica de habitaciones del inmueble:\n-> ')
        if habitacion_ingresado.isdigit() and int(habitacion_ingresado) >= 2:
            habitacion_ingresado = int(habitacion_ingresado)
            inmueble['habitaciones'] = habitacion_ingresado
            print(f'Datos guardados. HABITACIONES = {habitacion_ingresado}\n')
        else:
            while True:
                print('No operamos con inmuebles de menos de 2 habitaciones.')
                x = input('Ingrese una cantidad numerica de habitaciones valida:\n-> ')
                if x.isdigit() and int(x) >= 2:
                    x = int(x)
                    inmueble['habitaciones'] = x
                    print(f'Datos guardados. HABITACIONES = {x}\n')
                    break
                else:
                    continue
            
        garaje_ingresado = input('Ingrese SI/NO. ¿el inmueble posee garaje?:\n-> ').lower()
        if garaje_ingresado == 'si':
            inmueble['garaje'] = True
            print('Datos guardados. GARAJE = True\n')
        elif garaje_ingresado == 'no':
            inmueble['garaje'] = False
            print('Datos guardados. GARAJE = False\n')
        else: 
            while True:
                print('Las opciones disponibles son SI/NO')
                x = input('¿El inmueble posee garaje?:\n ->').lower()
                if x == 'si':
                    inmueble['garaje'] = True
                    print('Datos guardados. GARAJE = True\n')
                    break
                elif x == 'no':
                    inmueble['garaje'] == False
                    print('Datos guardados. GARAJE = False\n')
                    break
                else:
                    continue
                    
        zona_ingresado = input('Las zonas ingresadas solo pueden ser \'A\',\'B\',\'C\'.\nIngrese la zona del inmueble:\n-> ').upper()
        if zona_ingresado == 'A' or zona_ingresado == 'B' or zona_ingresado == 'C':
            inmueble['zona'] = zona_ingresado
            print(f'Datos guardados. ZONA = {zona_ingresado}\n')
        else:
            while True:
                print('Las opciones disponibles son A,B,C')
                x = input('¿En cual de estas zonas se encuentra el inmueble?:\n ->').upper()
                if x == 'A' or x == 'B' or x == 'C':
                    inmueble['zona'] = x
                    print(f'Datos guardados. ZONA = {x}\n')
                    break
                else:
                    continue
            
        estado_ingresado = input('Ingrese el estado del inmueble.\nLas opciones son: \'Disponible\',\'Reservado\',\'Vendido\'\n-> ').capitalize()
        if estado_ingresado == 'Disponible' or estado_ingresado == 'Reservado' or estado_ingresado == 'Vendido':
            inmueble['estado'] = estado_ingresado
            print(f'Datos guardados. ESTADO = {estado_ingresado}\n')
        else:
            while True:
                print('Las opciones disponibles son Disponible, Reservado, Vendido.')
                x = input('¿En que estado se encuentra el inmueble?:\n ->').capitalize()
                if x == 'Disponible' or x == 'Reservado' or x == 'Vendido':
                    inmueble['estado'] = x
                    print(f'Datos guardados. ESTADO = {x}\n')
                    break
                else:
                    continue
        
        id_ingresado = len(inmuebles) + 1
        inmueble['id'] = id_ingresado
                
        inmuebles.append(inmueble)
        print(f'\nInmueble agregado con exito!\n{inmueble}')
        break

# Lista de las caracteristicas que pueden ser editables
caracteristicas = ['año','metros','habitaciones','garaje','zona','estado']
# Convertir la lista a string y entre comillas para una mejor experiencia visual al usuario.
espaciado = ''
for x in caracteristicas:
    espaciado+= '\'' + x +'\'' + ', '
    
#Funcion para editar un inmueble 
def editar_inmueble(id_inmueble,atributo,valor_nuevo):
    
    '''Edita y cambia el valor de la caracteristica de un inmueble.
    Recibe 3 parametros en este orden: 1.El id del inmueble a modificar. 2.La caracteristica del inmueble a modificar. 3.El valor que quiere reemplazar en la caracteristica seleccionada.
    permite caracteristicas en mayusculas y minusculas pero debe ser siempre agregada entre comillas.'''
    
    atributo_minus = atributo.lower()
    print(f'En el inmueble seleccionado:\n{inmuebles[id_inmueble-1]}\n')
    if atributo_minus in caracteristicas:
        valor_antiguo = inmuebles[id_inmueble-1][atributo_minus]
        nuevo_valor = inmuebles[id_inmueble-1][atributo_minus] = valor_nuevo
        print(f'has cambiado {atributo_minus}: {valor_antiguo} a {atributo_minus}: {nuevo_valor}')
    else:
        print(f'{atributo.upper()} No es una caracteristica editable\nLas caracteristicas son:\n{espaciado}\nIngresadas SIEMPRE entre comillas \'\'.')


# Funcion para eliminar un inmueble de la lista     
def eliminar_inmueble(id_inm):
    
    '''Elimina un inmueble de la lista segun el ID que se le pase como argumento. Imprime la lista eliminada'''
    
    print(f"\nHas eliminado este inmueble de la lista:\n{inmuebles[id_inm-1]}")
    inmuebles.remove(inmuebles[id_inm-1])
    
def busqueda(lista,presupuesto):
    
    '''Busca los inmuebles Disponibles o Reservados que sean menor o igual a un presupuesto dado por el usuario e imprime en pantalla una lista de inmuebles filtrados que cumplan los requisitos'''
    
    def calcular_precio_inmueble(diccionario):
        
        '''calcula el precio de un inmueble particular. funciona solo localmente. recibe como parametro un diccionario de la lista de inmuebles'''
        
        precio_base = diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500
        antiguedad = 2023 - diccionario['año']
        
        if diccionario['zona'] == 'A':
            precio = precio_base * (1 - antiguedad / 100)
        elif diccionario['zona'] == 'B':
            precio = precio_base * (1 - antiguedad / 100)* 1.5
        else:
            precio = precio_base * (1 - antiguedad / 100) * 2
        return precio
	
    inmuebles_accesibles = []
    for inmueble in lista:
        if presupuesto < calcular_precio_inmueble(inmueble) and inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado':
            inmuebles_accesibles.append(inmueble)
        
        print(f'Aqui tienes una lista de inmuebles que sean menor o igual a tu presupuesto y su estado sea Disponible o Reservado:')
        for inmueble in inmuebles_accesibles:
            print(inmueble)
    