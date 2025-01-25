def main():
    userinput()

# Figure out which conversion to do, prompt the user for their input
def userinput():
    input_ = ''
    while input_.lower() != 'quit':
        input("To convert a decimal to binary, type '1'. To convert binary to decimal, type '2' Type 'Quit' to end program. ")
        if input_ == '1':
            number = int(input("Please enter the decimal you would like converted: "))
            convert = calculatebinary(number)
            printer1(convert)
        elif input_ == '2':
            number = int(input("Please enter the integer you would like converted: "))
            convert = binary_to_decimal(number)
            printer2(convert)
        elif input_ == 'quit':
            break
        else:
            print("Sorry! Input not recognized.")
        userinput()

# Convert the number into binary code and store that in a list
def calculatebinary(decimal):
    binary = []  
    binary.append(decimal % 2)
    remainder = decimal // 2
    while remainder != 0:
        add_to_binary = remainder % 2
        remainder = remainder // 2
        binary.append(add_to_binary)
    return binary 

# Convert binary into decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        binary //= 10
        power += 1

    return decimal

# Print the binary in its correct order
def printer1(translated):
    print("That number in binary is:", end=" ")
    for digit in reversed(translated):
        print(f"{digit}", end=" ")
    print()

def printer2(translated):
    print(f"That number in decimal is: {translated}")

# Run the program
if __name__ == "__main__":
    main()
