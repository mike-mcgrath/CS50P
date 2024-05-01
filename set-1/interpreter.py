# CS50’s Introduction to Programming with Python.
# Problem Set 1 - Math Interpreter.

def main() :

    while True :

        try :
            # Get expression.
            s = input( 'Expression: ' ).strip()
            
            # Separate expression components.
            x,y,z = s.split( ' ' )
            
            # Convert string numbers to floats.
            x = float( x )
            z = float( z )
            
            # Calculate appropriate sum result.
            match y :
                case '+' : s = x + z
                case '-' : s = x - z
                case '*' : s = x * z
                case '/' : s = x / z
                
            # Output formatted result to one decimal place.
            print( f'{s:.1f}' )
        
        except EOFError :
            exit( 'Done' )
		
if __name__ == '__main__' :
    main()