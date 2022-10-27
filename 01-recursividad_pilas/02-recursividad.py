
# Es un metodo matimatico y computacional.
# El problema con la recursividad es que la pila de la memoria se desborda.
# Esto es ineficiente y es mejor evitarlo.

# Leyes de recursividad
# 1.- Caso base ( el romper el metodo recursivo sino se haría un bucle infinito ).
# 2.- Debe de llamarse así mismo 
# 3.- Debe de cambiar de estado hasta que se acerque al caso base.


def i_am_recursive( value:int ):

    print( f'Me repito: {value}' )

    if value >= 10:
        quit()

    i_am_recursive( value + 1 ) 


def i_am_recursive2( value:int ):

    print( f'Me repito: {value}' )

    if value <= 0:
        quit()

    i_am_recursive2( value - 1 )

def fibonnaci( n:int ):

    if n == 0:
        return 0

    if n == 1:
        return 1
    
    return fibonnaci( n - 1 ) + fibonnaci( n - 2 )


def sum_list( items:list ):

    if items == []:
        return 0

    return items[0] + sum_list( items[1:] )
    # arr[0] -> 1 + ? [ 2, 3, 4, 5 ]
    # arr[0] -> 2 + ? [ 3, 4, 5 ]
    # arr[0] -> 3 + ? [ 4, 5 ]
    # arr[0] -> 4 + ? [ 5 ]
    # arr[0] -> 5 + ? [] -> 0


def reverse_list( items:list ):

    if len( items ) == 1:
        return [items[0]]
    
    return [items[-1]] + reverse_list( items[:-1] )



# i_am_recursive( 10 )
# i_am_recursive2( 10 )
# for i in range( 50 ):
#     print( i, fibonnaci( i ) )
# print( sum_list( [ 999, 2, 3, 4, 5 ] ) )
print( reverse_list( [ 999, 2, 3, 4, 5 ] ) )

