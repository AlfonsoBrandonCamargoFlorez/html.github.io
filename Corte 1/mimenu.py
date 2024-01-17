import json
from funcionesMenu import cargarEstudiantes, crearNuevoEstudiante, registroPrueba, rutaestudio

def menuPrograma():

    salir = False

    while  not salir:

        pregunta = int(input("\n1.Si desea cargar la información de los estudiantes."
                            "\n2.Si desea ingresar un nuevo estudiante."
                            "\n3.Para registrar la prueba. "
                            "\n4.Elegir ruta de estudio. "
                            "\n5.Para Salir" 
                            "\n¿Qué opción desea ingresar?: "))

        match pregunta:

            case 1:

                cargarEstudiantes()

            case 2:

                crearNuevoEstudiante()

            case 3:


                registroPrueba()

            case 4:
                rutaestudio()

            case 5:
                print("Hasta luego, que tenga un buen día")
                salir = True


menuPrograma()