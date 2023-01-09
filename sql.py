import sqlite3
from constantes import *


def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor


def agregar_pelicula(pelicula):
    conexion , cursor = conectar_db()

    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )

    sql = f'INSERT INTO pelicula(nombre,duracion,generos) VALUES{pelicula};'
    cursor.execute(sql)
    conexion.commit()
    conexion.close()


def obtener_pelicula():
    conexion , cursor = conectar_db()
    sql = f'SELECT * FROM pelicula;'
    cursor.execute(sql)
    peliculas = cursor.fetchall()
    conexion.close()
    return peliculas   


def eliminar_pelicula(nombre):
    conexion , cursor = conectar_db()
    sql = f'DELETE FROM pelicula WHERE nombre = {nombre}'
    cursor.execute(sql)
    cursor.fetchone()
    conexion.commit()

