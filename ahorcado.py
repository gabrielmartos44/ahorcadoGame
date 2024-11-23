from funciones import *

"""
funcion que se encarga de mostrar el menu en pantalla ejecutando las funciones respectivas para la logica del juego 
"""
def menu(datos):
    

    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar")
        print("2. Puntajes")
        print("3. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":

            idioma = elegiridioma()
            palabra_seleccionada = seleccionar_palabra_aleatorea(datos)
            palabra_separada = separador_de_palabra(palabra_seleccionada,idioma)
            palabraOculta = generar_palara_oculta(palabra_seleccionada,idioma)
            
            puntaje = juego_del_ahorcado(palabra_seleccionada,palabra_separada,palabraOculta,idioma)

            nombre = get_string("Ingrese el nombre del jugador: ","Error...Nombre muy corto o muy largo (sin numeros ni caracteres especiales)",3,30)
            guardar_puntuacion(nombre,puntaje)
            mostrar_top_5()

        elif opcion == "2":
           mostrar_top_5()

        elif opcion == "3":
            print("Saliendo del juego")
            break

        else:
            print("Opcion de menu invalida")



path = "Datosjason.json" 
datos = cargar_diccionario(path) 
menu(datos)