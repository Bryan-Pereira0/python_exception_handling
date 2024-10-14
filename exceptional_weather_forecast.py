#task1234


def temp_conversion(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def weather_app():
    try:
        fahrenheit = float(input("What is the temperature in Fahrenheit?: "))
        celsius = temp_conversion(fahrenheit)
        
    except ValueError:
        print("Invalid number. Please run the app again and enter a valid number!")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")
    finally:
        print("Thank you for using my weather application!")
weather_app()