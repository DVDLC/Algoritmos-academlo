# Este codigo es bueno para un numero pequeño de datos
# Con datos más grandes, es más eficiente que el selection sort

arr = [ 100, 10, 101, 20, 1, -200, -1, 0 ]

def insertion_sort( arr ):
    
    for j in range( 0, len(arr) ):

        aux = arr[j]

        i = j - 1
        while i >= 0 and arr[i] > aux:
            arr[ i + 1 ] = arr[i]
            i -= 1
        
        arr[ i + 1 ] = aux

    print( arr ) 
    
        
