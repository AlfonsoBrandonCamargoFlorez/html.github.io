
import json
from funcionesMenu import cargarEstudiantes, gestordeinformes, gestordepeliculas, admformatos, admactores, admgeneros

def menuPrograma():
    print("¡Bienvenido al Programa de Gestión de Blockbuster!")

    salir = False
    lista_peliculas = cargarEstudiantes()  # Puedes cargar los estudiantes una vez al inicio del programa

    while not salir:
        try:
            pregunta = int(input("\n-------Sistema gestor de peliculas Blockbuster-------"
                                "\n1.Gestor de generos. "
                                "\n2.Gestor de Actores. "
                                "\n3.Administrador de formatos. "
                                "\n4.Gestor de Informes. "
                                "\n5.Gestor de peliculas. "
                                "\n6.Salir. "
                                "\n¿Qué opción desea ingresar?: "))

            match pregunta:
                case 1:
                    admgeneros(lista_peliculas)
                case 2:
                    admactores(lista_peliculas)
                case 3:
                    admformatos(lista_peliculas)
                case 4:
                    gestordeinformes(lista_peliculas)
                case 5:
                    gestordepeliculas(lista_peliculas)
                case 6:
                    print("Hasta luego, que tenga un buen día")
                    salir = True    
                case _:
                    print("Opción no válida. Inténtelo de nuevo.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

menuPrograma()



