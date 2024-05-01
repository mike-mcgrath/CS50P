# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Um.
# Solution without Regular Expression pattern matching.

def main():

    # Get user's text string.
    print( count( input( 'Text: ' ).strip() ) )

def count( s ) :

    # Counter for number of um occurrence.
    counter = 0
    
    # Separate string into words.
    s = s.split(' ')
    
    # Examine each word.
    for word in s :
        for char in word :
        
            # Remove punctuation.
            if char in [ '.', ',', '?' ] : 
            # To fail test, change above to...
            # if char in  [ '.', ',', '?', '#' ] :   
                word = word.replace( char, '' )
                
        # Increment counter for um occurrence.       
        if word.lower() == 'um' :
            counter += 1
            
    # Output number of um occurrence.      
    return counter
    
if __name__ == '__main__':
    main()