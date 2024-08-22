oprts = 'addition','subtraction','multiplication','division'

def doSum(val1,val2):
    return val1 + val2

def doSub(val1,val2):
    return val1 - val2

def doMul(val1,val2):
    return val1 * val2

def doDiv(val1,val2):
    if val2 != 0: 
     return val1 / val2
    else: 
     return "undefined (division by zero is not allowed)"


#VERSION 3 
while True: 
    query = input(f'What operation you want to do? {oprts},Enter "exit" to close the programme ');

    if query == 'exit':
      print('Exiting the program. Goodbye!');
      break;
    
    if query not in oprts :
        print('Invalid operation selected. Please choose from the given list.');
    else :
       # Handle the case where the user enters something that is not a valid number
     try:
        val1 = float(input('Enter the first value: '));
        val2 = float(input('Enter the second value: '));

        if query == 'addition': 
            result = doSum(val1,val2);
            print(f'The result of {val1} + {val2} is equal to: {result}');
        elif query == 'subtraction':
            result = doSub(val1,val2);
            print(f'The result of {val1} - {val2} is equal to: {result}');
        elif query == 'multiplication':
            result = doMul(val1,val2);
            print(f'The result of {val1} * {val2} is equal to: {result}');
        elif query == 'division':
             result = doDiv(val1,val2);
             print(f'The result of {val1} / {val2} is equal to: {result}');

     except ValueError:
         print("Error: Please enter a valid number.")  # Friendly message for invalid input
        
        
         
    
