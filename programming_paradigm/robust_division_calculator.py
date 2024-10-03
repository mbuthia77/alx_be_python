import sys

def safe_divide(numerator, denominator):
    try: 
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
    return f"The result of the division is {result}"


#Testing code
#Q = safe_divide(10, 2)
#P = safe_divide(10, 0)
#R = safe_divide(10, 'c')
