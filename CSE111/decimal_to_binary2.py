def main():
    userinput()

# Prompt the user for their input and handle conversions
def userinput():
    while True:
        input_ = input(
            "To convert a decimal to binary, type '1'. "
            "To convert binary to decimal, type '2'. "
            "Type 'Quit' to end the program: "
        ).strip().lower()

        if input_ == '1':
            try:
                number = int(input("Please enter the decimal you would like converted: "))
                binary = calculatebinary(number)
                printer1(binary)
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")
        elif input_ == '2':
            try:
                binary = input("Please enter the binary number you would like converted: ").strip()
                if not all(c in '01' for c in binary):
                    raise ValueError
                decimal = binary_to_decimal(binary)
                printer2(decimal)
            except ValueError:
                print("Invalid input. Please enter a valid binary number.")
        elif input_ == 'quit':
            print("Goodbye!")
            break
        else:
            print("Sorry! Input not recognized.")

# Convert the number into binary as a string
def calculatebinary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Convert binary string into decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

# Print the binary in its correct order
def printer1(binary):
    print(f"That number in binary is: {binary}")

def printer2(decimal):
    print(f"That number in decimal is: {decimal}")

# Run the program
if __name__ == "__main__":
    main()
