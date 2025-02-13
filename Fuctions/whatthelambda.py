
# numsquared = lambda x: x**2 
# print(numsquared(5))

# numbers=[1,2,3,4,5]
# doublenums = numbers.map (lambda num: num*2)
# print(doublenums)

# print (doublenums)

# numbers=[10, 15, 25,30] 
# evens = numbers.filter (lambda num: num%2==0)

# list = [ "apple", "Kiwi", "banana"] 
# new_list = list.sorted(lambda word: word.length)
import math

# def numroot(originalnum):
#     square = math.sqrt(originalnum)
#     return square
# print(numroot(25))

# def palind_check(string):
#     check = []
#     for letter in string.strip().lower():
#         check.append(letter)
#     if check == check.reverse():
#         return True
#     else:
#         return False


def palind_check(string):
    cleaned_string = string.strip().lower()  
    return cleaned_string == cleaned_string[::-1]


print(palind_check("tacocat"))
print(palind_check("goat"))