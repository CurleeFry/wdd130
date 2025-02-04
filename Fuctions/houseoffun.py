import random
def door_one():
        choice = 0
        swag_meter = int(input("On a scale of 1 to 1000000 , how cool are you?"))
        if swag_meter < 1000:
            print("Wow. That's tough... anyways-")
            swag_meter = 5000000
        
        random_number = random.randint(1, swag_meter)
        while choice != random_number:
            choice = int(input(f"I'm thinking of a number 1 through {swag_meter}. What do you think it is?"))
            if choice < random_number:
                print("Too low. Try again!")
            if choice > random_number:
                print("Too high. Try again!")
        print("Took you long enough! You got the number.")


def door_two():
    print("🎰 Welcome to Lucky Number 7 Slot Machine! 🎰")
    money = float(input("Enter how much money you have: $"))
    print("\nEach spin costs $10. Try your luck!\n")
    
    symbols = ["7", "🍒", "🍋", "🔔", "💎", "🎲", "💀"]
    payouts = {
        "7": 10000,       # Jackpot
        "🍒": 100,       # Good win
        "🍋": 10,       # Break even
        "🔔": 5,        # Small win
        "💎": 1000,       # Big win
        "🎲": 0,         # No win
        "💀": -10000     #YOU'RE DEAD
    }

    while money >= 10:
        print(f"\nYou have ${money:.2f}.")
        play = input("Press Enter to spin (or type 'quit' to cash out): ").strip().lower()
        
        if play == "quit":
            print(f"\nYou cashed out with ${money:.2f}. Thanks for playing!")
            break
        
        money -= 10
        
        spin = [random.choice(symbols) for _ in range(3)]
        print("\nSpinning... 🎰")
        print(f"| {' | '.join(spin)} |")
        
        if spin[0] == spin[1] == spin[2]:
            win = payouts[spin[0]]
            money += win
            print(f"🎉 JACKPOT! You won ${win:.2f}! 🎉")
        else:
            print("💀 No win this time. Better luck next spin!")
        
    else:
        print("\nYou're out of money! Better luck next time.")
    print("Game over!")

def door_three():
    print("The House of Fun!")
    level_one()

def level_one():
    while True:
        print("\nYou are driving your car in the middle of Nevada. As you come over the hill, you see a great and spacious building.")
        print("You get a great urge to leave the car and walk up to the building.")
        print("Do you get out of the car and approach the building?")
        print("Or do you stay in the car?")
       
        choice = input("What do you want to do? (OUT/STAY): ").strip().upper()
       
        if choice == "OUT":
            out_path()
            break
        elif choice == "STAY":
            stay_path()
            break
        else:
            print("Invalid choice. Please type 'OUT' or 'STAY'.")

def out_path():
    print('You approach the building and end up next to a random stranger in front of the door. The man whispers in your ear, "I am itching to gamble my life away."')
    play_again()

def stay_path():
    print('You decide to stay in the car.')
    print("All of a sudden, you hear a noise...")
    end_game()

def end_game():
    print("The car blows up. You died!")
    print("Game Over.")

def play_again():
    while True:
        choice = input("\nDo you want to enter and gamble your life away with him? (YES/NO): ").strip().upper()
        if choice == "YES":
            terminal()
            break
        elif choice == "NO":
            print("The man slaps you, and you die from sadness.")
            no_gamble()
            break
        else:
            print("Invalid choice. Please type 'YES' or 'NO'.")

def no_gamble():
    print("You decide not to gamble. The man laughs at you as you walk away.")
    print("You reflect on your decision and live to tell the tale.")
    print("The End.")

def gamble():
    print("You enter the building, drawn to the flashing lights and ringing sounds of slot machines.")
    print("You sit at a poker table and begin gambling...")
    print("After hours of intense betting, you realize you're either a millionaire—or bankrupt!")
    print("What happens next is up to fate.")
    print("The End.")


def door_four():
    print("Function Four Called")

def terminal():
    functions = {
        '1': door_one,
        '2': door_two,
        '3': door_three
    }

    print("Welcome to the House of Fun! You'll have a great time... maybe. \n Type the number of your desired door to start! \
          \nDoor 1 \nDoor 2 \nDoor 3\n\n")

    while True:
        command = input("Which number door do you want to enter? ")
        if command == 'exit':
            print("Exiting terminal.")
            break
        elif command in functions:
            functions[command]()
        else:
            print("Just enter the number of the door!")

if __name__ == '__main__':
    door_three()