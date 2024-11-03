celsius = float(input('Enter temperature in celsius: '))

# Converting
fahrenheit = 1.8 * celsius + 32
kelvin = 273.15 + celsius

# Output
print('%0.3f Celsius = %0.3f Fahrenheit.' % (celsius, fahrenheit))
print('%0.3f Celsius = %0.3f Kelvin.' % (celsius, kelvin))