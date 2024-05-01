# CS50’s Introduction to Programming with Python.
# Problem Set 6 - P-Shirt.

import sys, csv
from PIL import Image, ImageOps

def main() :

    try :
        # Specify acceptable file extensions.
        exts = ['.jpg', 'jpeg', '.png']
    
        # Ensure there are two arguments specifying files.
        if len( sys.argv ) < 3 :
            raise TypeError( 'Too few command-line arguments' )
        elif len( sys.argv ) > 3 :
            raise TypeError( 'Too many command-line arguments' )
            
        # Ensure input file type is acceptable.   
        if sys.argv[1][-4:].lower() not in exts :
            raise TypeError( 'Invalid input file' )

        # Ensure output file type is acceptable.   
        if sys.argv[2][-4:].lower() not in exts :
            raise TypeError( 'Invalid output file' )
            
        # Ensure file types match.
        if sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower() :
            raise TypeError( 'Input and output have different extensions' )
        else : 
            file_in = sys.argv[1]
            file_out= sys.argv[2]
            
        # Load muppet image.
        pic = Image.open( sys.argv[1] )
        # Load shirt image.
        shirt = Image.open( 'shirt.png' )

        # Resize muppet to shirt size.
        pic = ImageOps.fit( pic, shirt.size )
        
        # Paste the shirt onto the muppet.
        pic.paste( shirt, shirt )
        
        # Output the combined image.
        pic.save( sys.argv[2] )
             
    except FileNotFoundError :
        sys.exit( 'Input does not exist' )    
    except TypeError as e :
        sys.exit( e )
    except EOFError :
        sys.exit( 'Done' )

if __name__ == '__main__' :
    main()