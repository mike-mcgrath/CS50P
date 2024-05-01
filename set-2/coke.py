# CS50’s Introduction to Programming with Python.
# Problem Set 2 - Coke Machine.

def main() :
    
    try : 
        # Fixed cost of Coke.
        COST = 50
        
        # Counter for coins entered.
        coins = 0
        
        # Calculate remaining amount.
        due = COST - coins

        # Output remaining amount.
        while coins < COST :
            print( '\nAmount Due: '+ str( due ) )
            coin = int( input( 'Insert Coin: ' ) )
                
            # Increment coin count for valid coins.
            if coin in [50,25,10] :
                coins += coin
                # Decrement amount due.
                due -= coin 
                
            # Output change due, if any.
            if due < 0 :
                print( 'Change Owed:', abs( due ) )
    
    except EOFError:
        exit( 'Done' )
        
if __name__ == '__main__' :
    main()   