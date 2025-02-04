import random

card_select = {
    "A" : 10, 
    "K" : 9, 
    "Q" : 8, 
    "J" : 7, 
    "10": 6
}

total_money = 1000

player_cards = random.choices(list(card_select.keys()), k=2)
player_numbers = [card_select[card] for card in player_cards]
player_total = sum(player_numbers)

bar_cards = random.choices(list(card_select.keys()), k=2)
bar_numbers = [card_select[i] for i in bar_cards]
bar_total = sum(bar_numbers)

wager = int(input(f"You decide to take a break at the bar. The bartender shuffles some cards. He wants to gamble with you. How much do you wager?\n$"))

look = input("The dealer deals you two cards. If your cards are higher, you win. Do you look at your cards? (Y/N)\n")
if look.lower() == "y":
    print(f"Your cards are: {player_cards}")
    if player_total > bar_total:
        total_money = (total_money + wager)
        print(f"You won! The Bartenders cards were {bar_cards}. Your total money is {total_money}.")
    else:
        total_money = (total_money - wager)
        print(f"The dealer's cards were {bar_cards}. You lost ${wager}. Your total money is {total_money}.")
elif look.lower() == "n":
    total_money = (total_money - wager)
    print(f"The dealer's cards were higher. You lost ${wager}. Your total money is {total_money}.")