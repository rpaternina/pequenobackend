import funciones

while True:

    try:

        menu = int(input(''' 
        
        [1] Agregar nueva pelicula
        [2] Obtener peliculas
        [3] Eliminar pelicula
        [4] Salir del programa
        >>> '''))


        if menu == 1:
            funciones.agregar_pelicula()
        elif menu == 2:
            funciones.obtener_peliculas()
        elif menu == 3:
            funciones.eliminar_pelicula()    
        elif menu == 4:
            print('Saliendo...')
            exit()
            

    except ValueError as error:
        print(f'Debe ingresar una opción valida {error}')        