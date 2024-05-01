# CS50’s Introduction to Programming with Python.
# Problem Set 4 - Emojize.

import emoji

def main() :

    while True :
    
        try :
            # Get emoticon as text string.        
            # e.g. :thumbsup:, :1st_place_medal:, :money_bag:, :heart:, :kiss:.
            s = input( 'Input: ' ).strip()
            
            # Output equivalent graphic emoji.
            print( 'Output:', end='' )
            # Requires the language attribute to enable full set of aliases. 
            print( emoji.emojize( s, language='alias' ) )   
            
        except EOFError :
            exit( 'Done' )
        
if __name__ == '__main__' :
    main() 