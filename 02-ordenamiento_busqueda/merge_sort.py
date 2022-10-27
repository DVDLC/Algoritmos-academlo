
def merge( left_arr, right_arr ):
    # Array auxiliar
    arr_aux = []

    # 1er Caso: Cuando los dos arrays tienen un largo mayor a 0 
    while len( left_arr ) > 0 and len( right_arr ) > 0:
        if left_arr[0] > right_arr[0]:
            arr_aux.append( right_arr[0] )
            right_arr.pop(0)
        else:
            arr_aux.append( left_arr[0] )
            left_arr.pop(0)

    # 2do y 3er Caso: Cuando alguno de los arrays ya no tiene valores entra a alguno de estos ciclos,
    # Como ya estan ordenados solo les hacemos un append e nuestra variable auxiliar
    while len( left_arr ) > 0:
        arr_aux.append( left_arr[0] )
        left_arr.pop(0)

    while len( right_arr ) > 0:
        arr_aux.append( right_arr[0] )
        right_arr.pop(0)

    return arr_aux



def merge_sort( arr ):

    # Caso base que da un return cuando el largo del array es igual a uno
    if len( arr ) == 1:
        return arr
    
    # Variables auxiliares
    # Parte a la mitad el array
    middle    = len( arr ) // 2
    # Lado izquierdo del array
    left_arr  = arr[ :middle ]
    # Lado derecho del array
    right_arr = arr[ middle: ]

    # Varibles con valores recursivos
    left_merge_sort  = merge_sort( left_arr )
    right_merge_sort = merge_sort( right_arr )

    # Cuando mi función entra al caso base returna una funcioón que une los arrays
    return merge( left_merge_sort, right_merge_sort )


print( merge_sort( [ 8, 12, 1, 3, 5 ] ) )

# función merge_sort "main"

# left_merge_sort  = merge_sort( [ 8, 12 ] )
#                  ↓ 
# left_merge_sort  = merge_sort( [ 8 ] )
# right_merge_sort = merge_sort( [ 12 ] )
#                  ↓ 
# * left_merge_sort  = arr_aux = [ 8, 12 ] *


# right_merge_sort = merge_sort( [ 1, 3, 5 ] )
#                  ↓ 
# left_merge_sort  = merge_sort( [ 1 ] )
# right_merge_sort = merge_sort( [ 3, 5 ] )
#                  ↓ 
# left_merge_sort  = merge_sort( [ 3 ] )
# right_merge_sort = merge_sort( [ 5 ] )
#                  ↓ 
# right_merge_sort = arr_aux = [ 3, 5 ]
# * right_merge_sort = arr_aux = [ 1, 3, 5 ] *




# función merge

# left_merge_sort  = arr_aux = [ 8, 12 ]
# right_merge_sort = arr_aux = [ 1, 3, 5 ]


# 8 > 1 
# arr_aux    = [1]
# left_arr   = [8, 12]
# right_ arr = [3, 5]
#       ↓
# 8 > 3
# arr_aux    = [1, 3]
# left_arr   = [8, 12]
# right_ arr = [5]
#       ↓
# 8 > 5
# arr_aux    = [1, 3, 5]
# left_arr   = [8, 12]
# right_ arr = []
#       ↓
# len( left_arr ) > 0
# arr_aux    = [1, 3, 5, 8]
# left_arr   = [12]
# right_ arr = []
#       ↓
# len( left_arr ) > 0
# arr_aux    = [1, 3, 5, 8, 12]
# left_arr   = []
# right_ arr = []
