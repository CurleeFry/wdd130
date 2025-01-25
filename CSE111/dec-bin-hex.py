have = (input("What type of number would you like to convert? Please enter 'Binary', 'Decimal', or 'Hexadecimal', or type 'quit' to quit. ")).lower()

def binary_input():
    ""

def decimal_input():
    ""

def hex_input():
    ""
def reroute():
    if have == 'binary' or have == 'bi':
        binary_input()
    elif have == 'decimal'or have == 'dec':
        decimal_input()
    elif have == 'hexadecimal' or have == 'hex':
        hex_input()

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