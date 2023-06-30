import random as rnd # Por convencion, llamamos a random como 'rnd'.

# Pedir un nombre al usuario
nombre = input('\nJuguemos a \'Adivina el numero\'. Pero primero...\n >>Ingrese su nombre: ').capitalize()

# Imprimir un mensaje con las reglas 
print(f'\nBienvenido {nombre}, debes adivinar el numero oculto.\nEste se encuentra entre el 1 y el 100.\nTienes 8 intentos.\n¿Podras lograrlo?\n')

#Una frase que cambie en cada intento realizado, para no repetir siempre lo mismo. (extra para hacerlo mas divertido.)
frases_intentos = ['¡Estas Cerca!', '¡Aplausos por el esfuerzo! Pero sigue intentando', 'A ver si la pegas en el próximo intento.','¿En serio crees que estás cerca?', 'Estás en la búsqueda, che.', 'No te rindas.', 'Estás calentando.', 'Esperaba algo mejor','¿Eso es lo mejor que puedes hacer?']

numero_ganador = rnd.randint(1, 100)  # Numero ganador aleatorio
intentos_disponibles = 8  # Cantidad de intentos restantes
cumple_condicion = True # Bandera del bucle while

# Requerimientos
while cumple_condicion:
   
    # Solicitar un numero al usuario. informando sus intentos restantes.
    numero_ingresado = input(f'Ingrese un numero entre 1 y 100. Tus intentos disponibles son {intentos_disponibles}.\n>>Numero elegido:  ')
    
    # Conversion de el numero_ingresado de str a int en una nueva variable para condicionar las pistas y requerimientos.
    numero_ingresado_entero = int()
    if numero_ingresado.isdigit():
        numero_ingresado_entero = int(numero_ingresado)
    # Si NO es un numero entero: imprimir mensaje de error.
    if not numero_ingresado.isdigit():
        print(f'\n¡RECUERDA!\nDebes ingresar un numero entero, entre 1 y 100.\n\'{numero_ingresado}\' no cumple las condiciones, vamos de nuevo..')
        continue
    
    #eleccion de una frase aleatoria
    eleccion_frase = rnd.choice(frases_intentos)
    
    # Pista: es mayor. en caso de negativo, no resta intentos vuelve a intentar.
    if numero_ingresado_entero < numero_ganador and numero_ingresado_entero > 0:
        print(f'\n{eleccion_frase}\nEl numero ganador es mayor a \'{numero_ingresado}\'')
        intentos_disponibles -= 1
    # Pista: es menor. en caso de >100 no resta intentos, vuelve a intentar.
    if numero_ingresado_entero > numero_ganador and numero_ingresado_entero <= 100:
        print(f'\n{eleccion_frase}\nEl numero ganador es menor a \'{numero_ingresado}\'.')
        intentos_disponibles -= 1
    
    # Limites numericos incumplidos. no resta intentos, vuelve a intentar.
    if numero_ingresado_entero <= 0 or numero_ingresado_entero > 100:
        print(f'\n¡RECUERDA!\nEl numero ingresado debe estar entre 1 y 100.\n\'{numero_ingresado}\' no cumple las condiciones, vamos de nuevo..')
        continue
    
    # Ganador del juego.
    if numero_ingresado_entero == numero_ganador:
        cumple_condicion = False
        ganador = f'\n¡Que suerte!\nLo has adivinado en el intento {9 - intentos_disponibles} {nombre}! y te han sobrado {intentos_disponibles - 1} intentos. \n¡Gracias por jugar!'
        # Reemplazar los plurales por singulares en caso de quedar 1 intento y ganar
        if intentos_disponibles == 1:
            singular = ganador.replace('intentos', 'intento').replace('han', 'ha')
            print(singular)
        else:
            print(ganador)
    # Perdedor del juego.
    if intentos_disponibles == 0:
        cumple_condicion = False
        print(f'\n¡JA, PERDISTE {nombre.upper()}!\nSe te han acabado los intentos.\n El numero oculto era: \'{numero_ganador}\'.\nNo te desanimes, la proxima sera.\n¡Gracias por jugar!\n')
       





