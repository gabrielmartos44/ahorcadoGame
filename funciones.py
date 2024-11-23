import json
import random

def get_string(mensaje:str,mensaje_error:str, minimo:int, maximo:int) -> str:
    
	string = input(f"{mensaje}")

	while( not string.isalpha() or len(string) > maximo or len(string) < minimo):
		print(f"{mensaje_error}")  
		string = input(f"{mensaje} ")
		
	return string
#-----------------------------------------------------------------------------------------------------------
def elegiridioma():

    while True:
        idioma = input("Seleccionar idioma:  Español(ES) o ingles(EN)--> ").upper()
        if (idioma == "ES" or idioma == "EN"):
            print("Bienvenido al juego!!!")
            return idioma

        else:
            print("Opcion no valida!! Debes seleccionar ES(Español) o EN(Ingles)") 
#-----------------------------------------------------------------------------------------------------------
''''
funcion que Cargar el json como un diccionario  y lo retorna con la variable datos
'''
def cargar_diccionario(path):
    with open(path, "r") as archivo:
        datos = json.load(archivo)          
    return datos["ahorcado"]                

#-----------------------------------------------------------------------------------------------------------
''''
funcion que  selecciona una palara aleatorea mediante el ID y 
retorla el diccionario de la palabra aleatorea con la que se jugara
'''
def seleccionar_palabra_aleatorea(datos):
    ids_disponibles = []

    for item in datos:                                  #guardo los id en una lista
        ids_disponibles.append(item["id"])
    
    id_aleatorio = random.choice(ids_disponibles)       # Seleccionar un id aleatorio de la lista de ids
    
    for item in datos:                                    # Buscar en la lista el diccionario que tenga el id seleccionado
        if item["id"] == id_aleatorio:
            return item     
#-----------------------------------------------------------------------------------------------------------
''''
funcion que inicializa una lista con "-" respecto a lo largo de la palabra seleccionada para jugar
'''
def generar_palara_oculta(palabra_selecc,idioma):
    palabraOculta = ["-"] * len(palabra_selecc[idioma])
    return palabraOculta
#-----------------------------------------------------------------------------------------------------------
''''
funcion que covierte la palabra en una lista separandolas en letras
'''

def separador_de_palabra(palabra_seleccionada,idioma):
    lista = []
    for i in range(len(palabra_seleccionada[idioma])): 
        lista.append(palabra_seleccionada[idioma][i])  
    return lista
#-----------------------------------------------------------------------------------------------------------
''''
funcion que solicita al jugador que ingrese una letra, 
esta funcion compara si la letra ingresada ya ha sido usada o no,
si fue usada le solicita una letra nueva,
si no ha sido usada esta retora dicha letra
'''
def obtener_letra_unica(banderaLetrasIngresadas,letrasUsadas):
    banderaLetraIngresadas = False
    letraIngresada = get_string("\nIngrese una Letra: ","Error...Tiene que elegir una letra de la 'A' a la 'Z' ",1, 1).lower()
    #evalua si la letra ingresada esta en el la lista de letras ingresadas
    while banderaLetrasIngresadas:
        for i in range(len(letrasUsadas)):
            if letraIngresada == letrasUsadas[i]:
                letraIngresada = get_string("\nYa habias ingresado esa letra, ingresa una diferente: ","Error...Tiene que elegir una letra de la 'A' a la 'Z' ",1, 1).lower()
                banderaLetraIngresadas = True
        
        if  banderaLetraIngresadas:  
            banderaLetraIngresadas = False
        else:
            banderaLetrasIngresadas = False

    return letraIngresada
#-----------------------------------------------------------------------------------------------------------
''''
funcion que compara si la palabra ingresda concuerda con la alguna de las latras de la palabra aleatorea seleccionada
si encuentra alguna similitud esta la reemplaza en la posicion correspondiente y la retorna
'''
def modificar_palabra_oculta(palabra_separada,letraIngresada,palabraOculta,acierto):
    for i in  range(len(palabra_separada)):            
        if palabra_separada[i] == letraIngresada:
            palabraOculta[i] = letraIngresada
            acierto = True

    return acierto,palabraOculta
#-----------------------------------------------------------------------------------------------------------
''''
funcion que evalua si el jugador ha logrado adivinar la palabra oculta,
esta funcion compara la palabra ocilta con la palara aleatorea seleccionada la cual fue convertida en una lista
en dado caso de que estas concuerden este marca la bandera de salida para que deje de ejecutar el juego e imprima
el puntaje y la palabra, en dado caso de que consumiera los 6 fallos este maracara tambien marcara 
la bandera de salida para que deje de ejecutar eh imprima el game over y la cantidad de puntos
'''
def estado_del_juego(palabraOculta,palabra_separada,fallos,palabra_seleccionada,idioma,salida,puntos):
    if palabraOculta == palabra_separada:
        print(f"\nFELICIDADES GANASTE {len(palabraOculta)} PUNTOS")
        print(f"La palabra oculta era: {palabra_seleccionada[idioma]} \n")
        puntos = len(palabraOculta)
        salida = False
    elif fallos == 0:
        salida = False
        print("Game over, el juego ha terminado. alcanzasate los 6 intentos")
        print(f"La palabra oculta era: {palabra_seleccionada[idioma]} \n")
        print(f"Has optenido la cantidad de {puntos} puntos")

    return salida,puntos
#-----------------------------------------------------------------------------------------------------------
''''
funcion que ejecuta la el juego  del ahorcado  solictando la letra para jugar y guardandolas en una lista
esta luego ejecuta la funcion modificar_palabra_oculta para luego evaluar si  la letra se encuentra o no en
la palabra oculta y remplaza la letra acentada en la posicion correspondiente, 
si hubo un fallo  no lo hace, luego se evalua si se acerto o no en la palabra para imprimir en pantalla el monigote
final ejecuta estado_del_juego el cual evalua si adivinamos o no el total de la palabra
para luego retorna el puntaje obtenido
'''
def juego_del_ahorcado(palabra_seleccionada,palabra_separada,palabraOculta,idioma):
    salida = True
    acierto = False
    fallos = 6
    letrasUsadas = []
    banderaLetrasIngresadas = False
    puntos = 0
    while salida:

        letraIngresada = obtener_letra_unica(banderaLetrasIngresadas,letrasUsadas)
        letrasUsadas.append(letraIngresada)
        banderaLetrasIngresadas = True

        print("\n")

        acierto,palabraOculta = modificar_palabra_oculta(palabra_separada,letraIngresada,palabraOculta,acierto)
        
        if acierto == True:
            acierto = False
            puntos +=1
            mostrar_monigote(fallos)
            print("\n¡Bien hecho! Adivinaste una letra.")
        else:
            fallos -= 1
            mostrar_monigote(fallos)
            print(f"\nLetra incorrecta. Te quedan {fallos} intentos.")
        
        for i in  range(len(palabraOculta)): 
            print(palabraOculta[i],end="")
        
        print("\nLetras usadas: " + ", ".join(letrasUsadas))
        print(f"Intentos restantes: {fallos}")
        
        salida,puntos = estado_del_juego(palabraOculta,palabra_separada,fallos,palabra_seleccionada,idioma,salida,puntos)
        
    return puntos

#-----------------------------------------------------------------------------------------------------------

''''
funcion que dependiendo  del numero de intentos retorna el monigote dependendiendo en el intento en el que este 
'''
def mostrar_monigote(nro_intentos):
    match nro_intentos:
        case 0:
            print("""
         .----.
         |    |       .----------------------------.
         |    |       | ¡GAME OVER! Eduardo murió. |                                   
         |    O       '----------------------------'
         |   /|\\  
         |   / \\   
         |
    ============                                                  
            """)
        case 1:
            print("""
         .----.
         |    |       .-----------------------------.
         |    |       | ¡Solo queda un intento más! |                                   
         |    O       '-----------------------------'
         |   /|\\  
         |   /    
         |
    ============                                                  
            """)
        case 2:
            print("""
         .----.
         |    |       .--------------------------------.
         |    |       | ¿Enserio me vas a dejar morir? |                                   
         |    O       '--------------------------------'
         |   /|\\  
         |       
         |
    ============                                                  
            """)
        case 3:
            print("""
         .----.
         |    |       .-----------------------------------.
         |    |       | Empiezo a dudar de tu capacidad...|                                   
         |    O       '-----------------------------------'
         |   /|  
         |       
         |
    ============                                                  
            """)
        case 4:
            print("""
         .----.
         |    |       .---------------------------.
         |    |       | ¡Uy! Esto empieza a doler.|                                   
         |    O       '---------------------------'
         |    |  
         |       
         |
    ============                                                  
            """)
        case 5:
            print("""
         .----.
         |    |       .------------------------------------------------------------.
         |    |       | Me llamo Eduardo, confio en que no volveras a fallar...no? |                                   
         |    O       '------------------------------------------------------------'
         |     
         |       
         |
    ============                                                  
            """)
        case 6:
            print("""
         .----.
         |    |       .-----------------------------------------.
         |    |       | ¡Muy bien! Por aqui no pasa nada todavia|                                   
         |            '-----------------------------------------'
         |     
         |       
         |
    ============                                                  
            """)
#-----------------------------------------------------------------------------------------------------------
"""
funcion que guarda los datos en una variable y veriica si el json esta vacio o si no existe, 
el puntaje nuevo ingresado se agrega al la lista de diccionarios de puntajes o lista de diccionarios vacia y
 esta se agrega o se crea en el sconres.json
"""
def guardar_puntuacion(nombre, puntaje):
    lista_puntajes = []

    try:
        with open("scores.json", "r") as file:
            lista_puntajes = json.load(file)
    except FileNotFoundError:
        lista_puntajes = []
    except json.JSONDecodeError:
        lista_puntajes = []

    nuevo_puntaje = {"nombre": nombre, "puntaje": puntaje}
    lista_puntajes.append(nuevo_puntaje)

    with open("scores.json", "w") as file:
        json.dump(lista_puntajes, file, indent=4)

#-----------------------------------------------------------------------------------------------------------
"""
funcion que ordena por seleccion los datos entregados en la funcion mostrar_top_5() la cual ordena los datos pasados
de mayor a menor y retornandolos ordenados
"""
def ordenar_por_selecion(datos):

    for i in range(len(datos)):       
        maximo = i                

        for j in range(i+1,len(datos)):   
            if datos[j]['puntaje'] > datos[maximo]['puntaje']:    
                maximo = j                   

        temp = datos[i]                   
        datos[i] = datos[maximo]             
        datos[maximo] = temp
    return datos
#-----------------------------------------------------------------------------------------------------------
"""
funcion que se encarga de mostrar en pantallael top 5 mejores puntuaciones
recorriendo los primeros datos ya ordenados por la funcion ordenar_por_seleccion()
"""
def mostrar_top_5():
    try:
        with open("scores.json", "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        return print("\nLista de puntajes vacia")
    except json.JSONDecodeError:
        return print("\nLista de puntajes vacia")
        
    datos_ordenados = ordenar_por_selecion(datos)
    
    print("\n--- TOP 5 MEJORES:")
    for i, jugador in enumerate(datos_ordenados[:5], start=1):  
        print(f"{i}- {jugador['nombre']}: {jugador['puntaje']}")