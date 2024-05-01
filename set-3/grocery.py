# CS50’s Introduction to Programming with Python.
# Problem Set 3 - Grocery List.

def main() :

    # Dictionary to store grocery items.
    basket = {}

    while True :
    
        try :
            # Get grocery item as text string in uppercase.
            s = input().strip().upper()
            
            # Add new item to basket.
            if s not in basket :
                basket[ s ] = 1
            # Or increment number of existing item.
            else :
                basket[ s ] += 1

        except EOFError :
        
            # Assign sorted dictionary keys to a list.    
            fruit = sorted( basket )
        
            # Output each dictionary value and key.
            for f in fruit :
                print( basket[f], f )
                
            exit( 'Done' )
        
if __name__ == '__main__' :
    main() 