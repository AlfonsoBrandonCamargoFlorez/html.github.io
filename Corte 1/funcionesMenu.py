import json


def cargarEstudiantes():

    file = open("estudiantes.json")

    estudiantes = json.load(file)

    for estudiante in estudiantes:

        print("Nombre:", estudiante["nombre"], "Edad:", estudiante["edad"], "Celular:", estudiante["telefono Celular"], "Estado:", estudiante["estado"])

    return estudiantes

lista_estudiantes= cargarEstudiantes()

def guardar_json():
    try:
      with open("estudiantes.json", 'w') as archivo_json:
        json.dump(lista_estudiantes, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")


def crearNuevoEstudiante():

    nuevoEstudiante = {}

    nuevoEstudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    nuevoEstudiante["edad"] = int(input("Ingrese la edad del estudiante: "))
    nuevoEstudiante["telefono Celular"] = int(input("Ingrese el número de celular: "))
    nuevoEstudiante["estado"] = input("Ingrese el estado en el que se encuentra el estudiante: ")

    lista_estudiantes.append(nuevoEstudiante)
    guardar_json()
       

    


def registroPrueba():

    file ="estudiantes.json"

    with open(file, "r+") as file:

        estudiantes = json.load(file)

        for estudiante in estudiantes:

            if estudiante["estado"].lower() == "inscrito":

                print("{} Usted puede presentar la prueba ya que su estado es {}".format(estudiante["nombre"], estudiante["estado"]))

                notaTeorica = int(input("Cuál es el resultado de su nota teorica: "))
                notaPractica = int(input("Cuál es el resultado de su nota practica: "))

                promedio = (notaPractica + notaTeorica) / 2

                if promedio >= 60:

                    estudiante["estado"] = "Aprobado"

                    print("Usted logró superar el promedio de la prueba con un {}".format(promedio))

                else:

                    estudiante["estado"] = "Reprobado"

                    print("Usted no logró superar el promedio su nota fue {} ".format(promedio))


            else:
                print("{} no puedes presentar la prueba porque su estado es {}".format(estudiante["nombre"], estudiante["estado"]))

            file.seek(0)

            json.dump(estudiantes, file)

def rutaestudio():
    
            
        for estudiante in lista_estudiantes:

            if estudiante["estado"].lower() == "aprobado":

                print("{} Usted puede elegir la ruta de entrenamiento".format(estudiante["nombre"]))

                salir = False

                while  not salir:

                    n = int(input("\n1.Ruta NodeJS."
                                "\n2.Ruta Java."
                                "\n3.Ruta NetCore"
                                "\n4.Ya elegi mi ruta."))
                    match n:

                        case 1:
                            estudiante["Ruta"] = "Ruta NodeJS "

                        case 2:
                            estudiante["Ruta"] = "Ruta Java "

                        case 3:
                            estudiante["Ruta"] = "Ruta NetCore "

                        case 4:
                            print("\nYa elegiste tu ruta. ")
                            salir = True
            guardar_json()
                    
                
                
                
                            
                
                

    