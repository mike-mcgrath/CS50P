# CS50’s Introduction to Programming with Python.
# Problem Set 3 - Felipe’s Taqueria.

def main() :

    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    # Count ongoing total cost.
    total = 0
        
    while True :
    
        try :
            # Get text string, in Title case.
            s = input( 'Item: ' ).strip().title()
            
            # Add to total cost if item is on the menu.
            total += menu[ s ]
            
            # Output the total cost
            print( f'Total: ${total:.2f}' )  
        
        except KeyError :
            print( f'{s} not on the menu!' )        
        except EOFError :
           exit( 'Done' )
        
if __name__ == '__main__' :
    main() 