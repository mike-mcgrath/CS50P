# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Frank, Ian & Glen's Letters.

import sys
from pyfiglet import Figlet
figlet = Figlet()

def main() :

    # Grab the valid font names list.
    # e.g. slant, rectangles, alphabet.
    fonts = figlet.getFonts()

    while True :
    
        try :
            # Ensure option is valid.
            if sys.argv[1] != '-f' and sys.argv[1] != '--font' :
                raise TypeError
        
            # Ensure font name is valid.        
            if sys.argv[2] not in fonts :
                raise TypeError
        
            # Set the font with the validated font name.
            figlet.setFont( font = sys.argv[2] )
           
            # Get string and output formatted text.   
            s = input( 'Input: ' ).strip()
            print( figlet.renderText( s ) )
        
        except TypeError :
            sys.exit( 'Invalid usage' )
        except IndexError :
            sys.exit( 'Command-line argument missing!' )
        except EOFError :
            sys.exit( 'Done' )
        
if __name__ == '__main__' :
    main() 