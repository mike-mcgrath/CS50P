# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Adieu, Adieu.

import inflect
p = inflect.engine()

def main() :

    # List to store input names.
    names = []

    while True :
    
        try : 
            # Get name input.
            s = input( 'Name: ' ).strip()
            
            # Add name to list.
            names.append( s )
            
        except EOFError :
            print( 'Adieu, adieu, to', p.join( names ) )
            exit( 'Done' )
        
if __name__ == '__main__' :
    main()