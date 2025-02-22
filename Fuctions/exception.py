def dividing():
    while True:
        try:
            given = int(input("Enter denominator: "))
            answer = 100 / given
            break  # Exit loop if successful
        except ZeroDivisionError:
            print("Unable to divide by zero. Please enter a nonzero number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return answer

if __name__ == "__main__":
    result = dividing()
    print(f"Result: {result}")