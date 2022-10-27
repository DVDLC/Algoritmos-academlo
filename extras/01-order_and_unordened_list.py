from dataclasses import dataclass

def bubble_sort(l):
    bubble = True

    while bubble:
        bubble = False

        for i in range( len(l) - 1 ):
            
            if( l[i] > l[i + 1] ):
                bubble = True
                l[ i ], l[ i + 1 ] = l[ i + 1 ], l[i] 
    return l    


@dataclass
class UnordenedList:

    items = []

    def add( self, e ):
        self.items.insert( len(self.items), e )

    def get_all(self):
        return self.items

@dataclass
class OrdernedList:

    items = []

    def add( self, e ):
        self.items.insert( len(self.items), e )

    def get_all(self):
        # Usamos nuestro bubble sort
        return bubble_sort( self.items )


print( 'Lista desordenada:' )    
u = UnordenedList()
u.add(1)
u.add(2)
u.add(7)
u.add(4)
u.add(-4)
u.add(9)

print( u.get_all() )

print( "\n" )

print( 'Lista ordenada:' ) 
u = OrdernedList()
u.add(1)
u.add(2)
u.add(7)
u.add(4)
u.add(-4)
u.add(9)

print( u.get_all() )