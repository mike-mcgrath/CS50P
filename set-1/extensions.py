# CS50’s Introduction to Programming with Python.
# Problem Set 1 - File Extensions.

def main() :

    while True :

        try :    
            #  Get filename in lowercase.
            s = input( 'File name: ' ).strip().lower()
        
            # Separate file name and extension, if any.
            s = s.split( '.' )
            
            # Output default media type if there is no extension.
            if len( s ) < 2 :
                print( 'application/octet-stream' )
                
            # Output appropriate media type if there is an extension.
            else :
                
                match s[1] :
                    case 'gif'  : print( 'image/gif' )
                    case 'jpg'  : print( 'image/jpeg' )
                    case 'jpeg' : print( 'image/jpeg' )
                    case 'png'  : print( 'image/png' )
                    case 'pdf'  : print( 'application/pdf' )
                    case 'txt'  : print( 'text/plain' )
                    case 'zip'  : print( 'application/zip' )
                    case _      : print( 'application/octet-stream' ) 
                    
        except EOFError :
            exit('Done')
	
if __name__ == '__main__' :
    main()
