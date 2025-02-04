import random

def slot_machine():
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

slot_machine()