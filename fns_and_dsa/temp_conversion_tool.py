FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celcius):
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = input("Enter the temperature to convert: ")
degree = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))

try:
    numeric_value = float(temperature)
    if degree == "F":
        print(f"{temperature}°F is {convert_to_celcius(numeric_value)}°C")
    elif degree == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(numeric_value)}°F")

except ValueError:
    print("Invalid temperature. Please enter a numeric value")