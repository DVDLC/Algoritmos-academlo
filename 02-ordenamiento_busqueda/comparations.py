import time

from shell_sort import shell_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort


# arr = [ 1, 4, 2, 10, 3, 2, -1, 0 ]
arr = [ 
    2, 5, 10, 1, 100, 20, 97, 12, 5, 4, 6, 6, 
    7, 8, 90, 10390, 90, 10, 980, 87, 9037, 2890, 
    7878, 299, 3, 8, 90, 10, -45, -200, 0, -1, 1 
]

# Complejidad Big O(n2) 
print( 'Bubble sort: ' )

inicio = time.time()
bubble_sort( arr )
final = time.time()

print( final - inicio, '\n' )

# arr = [ 1, 4, 2, 10, 3, 2, -1, 0 ]
arr = [ 
    2, 5, 10, 1, 100, 20, 97, 12, 5, 4, 6, 6, 
    7, 8, 90, 10390, 90, 10, 980, 87, 9037, 2890, 
    7878, 299, 3, 8, 90, 10, -45, -200, 0, -1, 1 
]

# Complejidad Big O(n2) 
print( 'Insertion sort: ' )

inicio = time.time()
insertion_sort( arr )
final = time.time()

print( final - inicio, '\n' )

# arr = [ 1, 4, 2, 10, 3, 2, -1, 0 ]
arr = [ 
    2, 5, 10, 1, 100, 20, 97, 12, 5, 4, 6, 6, 
    7, 8, 90, 10390, 90, 10, 980, 87, 9037, 2890, 
    7878, 299, 3, 8, 90, 10, -45, -200, 0, -1, 1 
]

# Complejidad Big O(n2) 
print( 'Selection sort: ' )

inicio = time.time()
selection_sort( arr )
final = time.time()

print( final - inicio, '\n' )

# arr = [ 1, 4, 2, 10, 3, 2, -1, 0 ]
arr = [ 
    2, 5, 10, 1, 100, 20, 97, 12, 5, 4, 6, 6, 
    7, 8, 90, 10390, 90, 10, 980, 87, 9037, 2890, 
    7878, 299, 3, 8, 90, 10, -45, -200, 0, -1, 1 
]

# Complejidad Big O(n logn) 
print( 'Shell sort: ' )

inicio = time.time()
print( shell_sort( arr ) )
final = time.time()

print( final - inicio, '\n' )

# arr = [ 1, 4, 2, 10, 3, 2, -1, 0 ]
arr = [ 
    2, 5, 10, 1, 100, 20, 97, 12, 5, 4, 6, 6, 
    7, 8, 90, 10390, 90, 10, 980, 87, 9037, 2890, 
    7878, 299, 3, 8, 90, 10, -45, -200, 0, -1, 1 
]

# Complejidad Big O(n logn) 
print( 'Merge sort: ' )

inicio = time.time()
print( merge_sort( arr ) )
final = time.time()

print( final - inicio, '\n' )

