
import json

#me permite abrir el archivo peliculas.json
def cargarEstudiantes():
    peliculas = []

    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []


#funsion que me permite llamar otras funciones y ver listas de peliculas, listas de peliculas por actores y buscar pelicula para mostrar sinopsis y actores

def gestordeinformes(peliculas):
    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Listas de peliculas de genero especifico. "
                                "\n2.Listas de peliculas por actores. "
                                "\n3.Buscar Pelicula y mostrar la sinopsis y los actores. "
                                "\n4.Ir al menu principal. "))
                match ask:
                    case 1:
                        generop(peliculas)

                    case 2:
                        actor1(peliculas)
                    
                    case 3:
                        nombrep(peliculas)
                    
                    case 4:                    
                        print("Regresando al menú anterior. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 3.")
            return peliculas
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []
                                
#funsion que me permite consultar en el .json las peliculas que tiene cierto actor.
def actor1(peliculas):
    actv=input("Ingrese el nombre del actor para consultar sus peliculas.")
    actor1 = [estudiante for estudiante in peliculas if estudiante["act1"].lower() == actv ]

    if actor1:
        print("\nPeliculas del actor" , actv)
        for estudiante in actor1:
            print("Nombre:", estudiante["nombre"])
    else:
        print("\nNo tenemos peliculas de este actor.")

    actor2 = [estudiante for estudiante in peliculas if estudiante["act2"].lower() == actv ]

    if actor2:
        print("\nPeliculas del actor" , actv)
        for estudiante in actor2:
            print("Nombre:", estudiante["nombre"])
   

    actor3 = [estudiante for estudiante in peliculas if estudiante["act3"].lower() == actv ]

    if actor3:
        print("\nPeliculas del actor" , actv)
        for estudiante in actor3:
            print("Nombre:", estudiante["nombre"])

#funcion que me permite ver todas las peliculas de determinado genero, accion, comedia, terror etc.
def generop(peliculas):
    gener=input("Ingrese el genero de la pelicula")
    generop = [estudiante for estudiante in peliculas if estudiante["genero"].lower() == gener ]

    if generop:
        print("\nPeliculas del genero " , gener)
        for estudiante in generop:
            print("Nombre:", estudiante["nombre"])
    else:
        print("\nNo tenemos peliculas de este genero.")


#funcion que me permite traer informacion de una pelicula
def nombrep(peliculas):
    actv=input("Ingrese el nombre de la pelicula.")
    nombrep = [estudiante for estudiante in peliculas if estudiante["nombre"].lower() == actv ]

    if nombrep:
        print("\nLa sinopsis de la pelicula" , actv, " es: ")
        for estudiante in nombrep:
            print("Sinopsis :", estudiante["sinopsis"])
            print("Y sus actores principales son ",estudiante["act1"], ", ",estudiante["act2"]," y ",estudiante["act3"])
    else:
        print("\nNo tenemos esta pelicula aun.")
    





    

lista_peliculas = cargarEstudiantes()

#funcion que me permite guardar en mi .json
def guardar_json(lista_peliculas):
    try:
        with open("peliculas.json", 'w') as archivo_json:
            json.dump(lista_peliculas, archivo_json, indent=2)
            print("La lista de peliculas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya peliculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:", e)


#funcion que me permite hacer modificaciones en .json como agregar nuevas peliculas, buscar una pelicula etc.
def gestordepeliculas(peliculas):
    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Agregar pelicula.  "
                                "\n2.Editar pelicula. "
                                "\n3.Eliminar Pelicula. "
                                "\n4.Eliminar actor. "
                                "\n5.Buscar pelicula. "
                                "\n6.Listar todas las peliculas."
                                "\n7.Menu principal. "))
                match ask:
                    case 1:
                        crearpelicula()
                    case 2:
                        print("Estamos trabajando en ello.")
                    
                    case 3:
                        print("Estamos trabajando en ello.")

                    case 4:                    
                        print("Estamos trabajando en ello.")

                    case 5:                    
                        buscarp(peliculas)

                    case 6:                    
                        todasp(peliculas)

                    case 7:                    
                        print("Saliendo del menu actual. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 7.")
            return peliculas
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []


#funcion que me permite buscar una pelicula por su nombre y saber el valor de alquiler de la misma
def buscarp(peliculas):
    busc=input("Ingrese el nombre de la pelicula")
    buscarp = [estudiante for estudiante in peliculas if estudiante["nombre"].lower() == busc ]

    if buscarp:
        print("\nSi tenemos la pelicula" , busc)
        for estudiante in buscarp:
            print("Costo de alquiler es $", estudiante["valor"]," pesos el dia.")
    else:
        print("\nNo tenemos peliculas de este genero.")

#funcion que me permite ver todas las peliculas almacenadas y su genero
def todasp():
    
    print("Generos de peliculas con las que actualmente contamos.")
    for peliculas in peliculas:        
        print(peliculas["nombre"])

#funcion que me permite crear una nueva pelicula.
def crearpelicula():
    global lista_peliculas

    nuevapelicula = {}

    nuevapelicula["nombre"] = input("Ingrese el nombre de la pelicula. ")
    nuevapelicula["duracion"] = int(input("Ingrese la duracion de la pelicula. "))
    nuevapelicula["copias"] = int(input("Numero de copias. "))
    nuevapelicula["genero"] = (input("Genero de la pelicula. "))
    nuevapelicula["codigo"] = int(input("Ingrese codigo de la pelicula. "))
    nuevapelicula["act1"] = (input("Actor 1. "))
    nuevapelicula["act2"] = (input("Actor 2. "))
    nuevapelicula["act3"] = (input("Actor 3. "))
    nuevapelicula["formatop"] = (input("Formato de la pelicula. "))
    nuevapelicula["sinopsis"] = (input(".Ingrese sinopsis de la pelicula. "))
    nuevapelicula["valor"] = int(input("Valor alquiler pelicula. "))
    

    lista_peliculas.append(nuevapelicula)

    guardar_json(lista_peliculas)





def admgeneros(peliculas):
    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Crear Genero. "
                                "\n2.Listar Generos. "
                                "\n3.Ir al menu principal. "))
                match ask:
                    case 1:
                        print("Estamos trabajando en ello.")

                    case 2:
                        todosg(peliculas)                 
                 
                    case 3:                    
                        print("Regresando al menú principal. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 3.")
            return peliculas
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []

def todosg(peliculas):
    
    print("Generos de peliculas con las que actualmente contamos.")
    for peliculas in peliculas:        
        print(peliculas["genero"])




def admactores(peliculas):
    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Crear Actor. "
                                "\n2.Listar Actores. "
                                "\n3.Ir al menu principal. "))
                match ask:
                    case 1:
                        print("Estamos trabajando en ello.")

                    case 2:
                        print("Estamos trabajando en ello.")                   
                 
                    case 3:                    
                        print("Regresando al menú principal. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 3.")
            return peliculas
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []
    

def todosf(peliculas):
    
    print("Formatos de peliculas con las que actualmente contamos.")
    for peliculas in peliculas:        
        print(peliculas["formatop"])

def admformatos(peliculas):
    try:
        with open("peliculas.json") as file:
            peliculas = json.load(file)

        if peliculas is not None:
            salir = False
            while not salir:
                ask = int(input("\n1.Crear Formato. "
                                "\n2.Listar Formatos. "
                                "\n3.Ir al menu principal. "))
                match ask:
                    case 1:
                        print("Estamos trabajando en ello.")

                    case 2:
                        todosf(peliculas)                   
                 
                    case 3:                    
                        print("Regresando al menú principal. ")
                        salir = True
                    case _:
                        print("Opción no válida. Por favor, elija una opción del 1 al 3.")
            return peliculas
        else:
            print("El archivo 'peliculas.json' está vacío o tiene un formato incorrecto.")
            return []

    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Puede que aún no haya peliculas guardados.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
        return []
    except Exception as e:
        print("Error desconocido:", e)
        return []
