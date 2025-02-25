import os

def runfxn(fxn_name):
    """Reads and executes the given Python file."""
    if not os.path.exists(fxn_name):
        print(f"Error: '{fxn_name}' not found.")
        return

    with open(fxn_name) as lines:
        code = lines.read()
        exec(code, globals()) 

def listfxns():
    """Lists available Python functions in the 'functions' directory."""
    folder = "./"
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' directory not found.")
        return

    print("Available functions include:")
    for fxn in os.listdir(folder):
        if fxn.endswith(".py"):
            print(fxn)

def main():
    """Main function to interact with the user."""
    while True:
        action = input("To run a function, type its name. To see available functions, input '1'. To quit, type 'QUIT': ").strip()

        if action == "1":
            listfxns()
        elif action.lower() == "quit":
            print("Function runner terminated.")
            break
        elif action.endswith(".py"):
            try:
                runfxn(action)
            except Exception as e:
                print(f"An error occurred while running '{action}': {e}")
        else:
            print("Input not recognized. Please enter a valid answer.")

if __name__ == "__main__":
    main()
