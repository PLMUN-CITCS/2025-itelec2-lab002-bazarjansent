# Jansent Bazar
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    print("Simple Calculator Program")

    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    print(f"The sum is {num1 + num2}")
    print(f"The difference is {num1 - num2}")
    print(f"The product is {num1 * num2}")

    # Check for division by zero
    if num2 != 0:
        print(f"The quotient is {num1 / num2:.2f}")
    else:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    main()
