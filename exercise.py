try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percent = (value / total) * 100
    print(f"This is {percent}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value can not be zero.")


