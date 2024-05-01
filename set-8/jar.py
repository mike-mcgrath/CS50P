# CS50’s Introduction to Programming with Python.
# Problem Set 8 - Cookie Jar.

class Jar:

    # Automatically called when instance is created.
    def __init__( self, capacity=12 ):
    
        try :
            # Ensure argument is a positive integer.
            if not isinstance( capacity, int ) or capacity < 1 :
                raise ValueError
            else :
                # Initialize class variables.
                self.space = capacity
                self.cookies = 0
                
        except ValueError :
            exit( 'Capacity must be a positive integer' )
        
    # Output when str() includes the instance name as its argument.   
    def __str__( self ) :  
        return f'{"🍪"*self.cookies}'
 
    # Ensure space is sufficient, then add argument value to class variable.
    def deposit( self, n ) :
        try :
            if self.cookies + n <= self.space :
                self.cookies += n
                print( 'Deposited:', n )
            else :
                raise ValueError( f'Not Enough Space to Deposit {n}' )
        except ValueError as e :
            print( e )

    # Ensure sufficient cookies available, then deduct argument value from class variable.
    def withdraw( self, n ) :
        try :     
            if n <= self.cookies :
                self.cookies -= n 
                print( 'Withdrawn:', n )
            else :
                raise ValueError( f'Not Enough Cookies to Withdraw {n}' )
        except ValueError as e :
            print( e )

    # Output for instance properties... 
    @property
    def capacity( self ) :
        return self.space

    @property
    def size( self ) :
        return self.cookies
  
def main() :
  
    jar = Jar()
    print( 'Capacity:', jar.space, 'Cookies:', jar.cookies )
    jar.deposit(20)
    jar.deposit(10)
    print( 'Capacity:', jar.space, 'Cookies:', jar.cookies )
    print( str( jar ) )
    jar.withdraw(20)
    jar.withdraw(5)
    print( 'Capacity:', jar.space, 'Cookies:', jar.cookies )
    print( str( jar ) )
    
if __name__ == '__main__' :
    main()
