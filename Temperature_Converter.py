def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
