def pass_input():
    password = input("What is your password?")
    return password

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_special_char(password):
    special_chars = set("!@#$%^&*()-_+=<>?/{}[]|\\:;\"'`~")
    return any(char in special_chars for char in password)

def has_num(password):
    num_chars = set("1234567890") 
    return any(char in num_chars for char in password)

def count_chars(password):
    return len(password)

def scoretest(password):
    score = 0
    if has_lowercase(password) == True:
        score += 1

    if has_uppercase(password) == True:
        score += 1

    if has_special_char(password) == True:
        score += 1
        
    if has_num(password) == True:
        score += 1

    if count_chars(password) >= 12:
        score += 4
    elif count_chars(password) >= 10:
        score += 3
    elif count_chars(password) >= 8:
        score += 2
    elif count_chars(password) >= 6:
        score += 1
    
    return score

def results(score):
    print(f"Your password scored {score} points our of 8 points.")

def main():
    password = pass_input()
    score = scoretest(password)
    results(score)


if __name__ == "__main__":
    main()
