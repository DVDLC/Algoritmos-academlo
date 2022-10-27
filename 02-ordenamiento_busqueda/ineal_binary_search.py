import time
siu = range(1, 1000)


def lineal_search( arr, n ):
    iters = 0
    arr_len = len(arr)
   
    for i in range( arr_len ):
        iters += 1
        if arr[i] == n:
            return f'{arr[i]} in position { i }; iters={ iters } - lineal'

def my_binary_search( arr, n ):
    iters = 0
    arr_len = len(arr)

    arr_first_num = 0
    arr_last_num  = 1000
    arr_mid_num   = arr[ round( arr_len / 2 ) ]
   
    if n > arr_mid_num and n <= arr_last_num :

        for i in range( arr_mid_num, arr_last_num + 1 ):
            iters += 1
            if arr[i] == n:
                return f'{arr[i]} in position { i }; iters={ iters } - my binary search 1'

    elif n <= arr_mid_num and n >= arr_first_num:

        for i in range( arr_first_num, arr_mid_num + 1 ):
            iters += 1
            if arr[i] == n:
                return f'{arr[i]} in position { i }; iters={ iters } - my binary search 2'


def class_binary_search( arr, value ):
    n     = len(arr)
    left  = 0
    right = n - 1

    iters = 0 

    while left <= right:
        iters += 1

        middle = ( left + right ) // 2

        print( left, middle, right )

        if value < arr[middle]:
            right = middle - 1
        elif value > arr[middle]:
            left  = middle + 1
        else:
             return f'{arr[middle]} in position { middle }; iters={ iters } - class binary search'


# inicio = time.time()
# print(lineal_search( siu, 600 ))
# final = time.time()

# print( final - inicio, '\n' )

# inicio = time.time()
# print(my_binary_search( siu, 600 ))
# final = time.time()

# print( final - inicio, '\n' )

inicio = time.time()
print(class_binary_search( siu, 200 ))
final = time.time()
print( final - inicio )