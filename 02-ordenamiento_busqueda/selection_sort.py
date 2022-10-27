def selection_sort( arr ):

    for i in range( len( arr ) ):

        idx_min = i

        for j in range( i + 1, len(arr) ):

            if arr[ idx_min ] > arr[ j ]:  # Puede ser mayor o menor, depende de como lo queremos acomodar
                idx_min = j

        temp = arr[i]
        arr[i] = arr[idx_min]
        arr[ idx_min ] = temp

    print( arr )

