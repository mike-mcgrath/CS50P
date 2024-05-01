# CS50’s Introduction to Programming with Python.
# Problem Set 7 - Watch on YouTube.
# Solution without Regular Expression pattern matching.


def main() :

    print( parse( input( 'HTML: ' ) ) )

def parse( s ):

    flag = False
    s = s.split( '"' )

    # Find URL, if any.
    for i in s :
        if i[:4].lower() == 'http' :
            s = i
            flag = True
    
    # Simplify URL string.
    if 'embed/' in s :
        s = s.replace( 'embed/', '' )
    if 'www.' in s :
        s = s.replace( 'www.', '' )
    if 'youtube.com' in s :
        s = s.replace( 'youtube.com', 'youtu.be' )
    else : flag = False 
    
    # Return simple URL, or None.  
    if flag : 
        return s
    else : 
        return None 

if __name__ == '__main__' :
    main()