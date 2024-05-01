# CS50’s Introduction to Programming with Python.
# Problem Set 5 - Vanity Plates revision.

def main() :

    while True :
    
        try :
            # Get desired plate string.
            plate = input( 'Plate: ' ).strip()
            
            # Ensure string is acceptable.
            if is_valid( plate ) :
                print( 'Valid' )
            else :
                print( 'Invalid' )

        except EOFError :
            exit( 'Done' )
         
def is_valid( s ) :  
 
    # Ensure length is 2-6 characters.
    if len(s) < 2 or len(s) > 6 : return False
    
    # Ensure first two characters are letters.
    if not s[0].isalpha() or not s[1].isalpha() : return False
    
    # Ensure there are no punctuation characters.
    for char in s :
         if not char.isalnum() : return False
         
    # Slice substring from first number to end of string.
    sub = False
    for i,char in enumerate( s ) :
        if not char.isalpha() :
            s = s[i:] ; sub = True ; break
     
    # For the substring...
    if sub :
    
        # Ensure first number is not zero.    
        if s[0] == '0' : return False 
        # To fail test, change above to return True.

        # Ensure no letters follow numbers in substloop.
        for char in s :
            if char.isalpha() : return False

    # Otherwise...
    return True 


if __name__ == '__main__' :
    main()