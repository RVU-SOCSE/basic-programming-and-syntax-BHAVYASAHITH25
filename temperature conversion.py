temp = input("temperature (C/F): ")
match temp:
    case 'C':
        C = float(input("Enter celsius value: "))
        print("Celsius to Fahrenheit:", (C * 9/5) + 32)
    case 'F':
        F = float(input("Enter fahrenheit value: "))
        print("Fahrenheit to Celsius:", (F - 32) * 5/9)
    case _:
        print("Invalid choice")
