def safe_divide(numerator, denominator):
    try:
        top = float(numerator)
        bottom = float(denominator)
        return f"The result of the division is {top/bottom}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."