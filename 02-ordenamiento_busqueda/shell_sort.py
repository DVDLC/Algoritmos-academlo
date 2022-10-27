
def shell_sort( arr ):
    
    # Tenemos un intervalo que nos ayudara con las iteraciones
    interval = len( arr ) // 2


    while interval > 0:

        # Ciclo que ira iterando y evaluando los valores
        # Me di cuenta que cada vez que iteramos se sale de los limites
        # entonces el intervalo marca el limite de la iteración cada que recorre el ciclo
        # Por ejemplo:
        # 1er ciclo:
        """ 
            arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
            intervalo = 4
            range( len( arr ) - intervalo ) :: [ *1, *2, *3, *4, *5, 6, 7, 8, 9 ]
            intervalo -= 1 :: 3
        """

        # 2do ciclo:
        """ 
            arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
            intervalo = 3
            range( len( arr ) - intervalo ) :: [ *1, *2, *3, *4, *5, *6, 7, 8, 9 ]
            intervalo -= 1 :: 2
        """

        # 3er ciclo:
        """ 
            arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
            intervalo = 2
            range( len( arr ) - intervalo ) :: [ *1, *2, *3, *4, *5, *6, *7, 8, 9 ]
            intervalo -= 1 :: 2
        """
        # Y asi hasta llegar a intervalo == 0...

        for i in range( len( arr ) - interval):

            print( arr )

            if arr[i] > arr[ i + interval ]:

                # Pues solo intercambiamos
                aux = arr[i]
                arr[ i ] = arr[ i + interval ]
                arr[ i + interval ] = aux
        
        interval -= 1
    
    return arr


print( shell_sort( [8, 12, 1, 3, 5] ) )

# Función shell_sort

# intervalo = 2
# [ 1, 12, 8, 3, 5 ]
# [ 1, 3, 8, 12, 5 ]
# [ 1, 3, 5, 12, 8 ]

# intervalo = 1
# [ 1, 3, 5, 12, 8 ]
# [ 1, 3, 5, 12, 8 ]
# [ 1, 3, 5, 12, 8 ]
# [ 1, 3, 5, 8, 12 ]
