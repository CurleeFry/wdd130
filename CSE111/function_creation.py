names = ["Alice", "Bob", "Charlie"]
primes = []
calculations = 0

def find_primes():
    for num in range(2, 10001):  # Start from 2, since 1 is not a prime number
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def num_of_primes():
    find_primes()
    calculations = 0
    for num in primes:
        focus = num
        for num2 in primes:
            focus * num2
            calculations += 1
    print(f"{calculations}")

num_of_primes()

            

#print names
def printer(names):
    for name in names:
        print(f"Welcome, {name}!")

#Calculate and print areas
def calculator(vars):
    count= 0
    for var in vars:
        count += 1
        area = var * (var + 1)
        print(f"Area {count}: {area}")

# printer(names)
# calculator(numbers)