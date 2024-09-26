def perform_operation(num1, num2, operator):
    if operator == 'add':
        return num1 + num2
    elif operator == 'substract':
        return num1 + num2
    elif operator == 'multiply':
        return num1 + num2
    elif operator == 'divide':
        if num2 !=0: 
            print("The result is ", num1 / num2)
        else: print("Cannot divide by zero.")
