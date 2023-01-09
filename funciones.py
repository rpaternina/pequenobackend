from modelos import Pelicula , Genero, Catalogo
import sql

def agregar_pelicula():

    nombre = input('Ingrese el nombre de la pelicula: ')
    duracion = int(input('Ingrese la duración en minutos: '))
    genero = int(input('Ingrese el genero de la pelicula: '))

    pelicula = Pelicula(nombre, duracion, genero)    
    sql.agregar_pelicula(pelicula)

catalogo = Catalogo('Peliculas de mafia')

def obtener_peliculas():
    peliculas = sql.obtener_pelicula()
    for pelicula in peliculas:
        guardar_pelicula = Pelicula(pelicula[1], pelicula[2], pelicula[3])
        catalogo.pelicula.append(guardar_pelicula)

    for pelicula in catalogo.pelicula:
        print(f'''
Nombre de la pelicula: {pelicula.nombre}
Duración de la pelicula: {pelicula.duracion} minutos
Genero de la pelicula : {pelicula.genero}            
        ''')  

def eliminar_pelicula():
   
    peliculas = input(f'Ingrese el nombre de la pelicula a eliminar: ')
    sql.eliminar_pelicula(peliculas)            
    
    