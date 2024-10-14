#task1234


def temp_conversion():
    try:
        temperature_in_f = float(input("What is the temperature in Fahrenheit?: "))
        temperature_in_c = (temperature_in_f - 32) * 5/9
    except ValueError:
        print("That's not a valid number! Please run the app again and input a valid number.")
    else:
        print(f"{temperature_in_f} degrees Fahrenheit is {temperature_in_c} degrees Celsius!")
    finally:
        print("Thank you for using my Temperature Conversion App!")

temp_conversion()
