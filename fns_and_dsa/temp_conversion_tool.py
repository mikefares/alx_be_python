FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(farenheit):
    return (farenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_farenheit(celcius):
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
degree = str(input("Is this temperature in Celcius or Farenheit? (C/F):"))

if degree == "F":
    print(f"{temperature}°F is {convert_to_celcius(temperature)}°C")
elif degree == "C":
    print(f"{temperature}°C is {convert_to_farenheit(temperature)}°F")
else:
    print("Invalid temperature. Please enter a numeric value")