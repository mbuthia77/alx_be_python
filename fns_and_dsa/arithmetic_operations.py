def perform_operation(num1, num2, operator):
    num1 = float
    num2 = float
    operator = ('add', 'substract' , 'multiply', 'divide')
    match operator:
         case "add": return num1 + num2
         case "substract": return num1 - num2
         case "multiply": return num1 * num2
         case "divide":
          if num2 !=0:
            return num1 / num2
          else: return print("Cannot divide by zero.")
