import string
import random


symbols = list(string.ascii_letters)


card1 = [0]*5
card2 = [0]*5


pos1 = random.randint(0,4)
pos2 = random.randint(0,4)


same_symbol = random.choice(symbols)


card1[pos1] = same_symbol
card2[pos2] = same_symbol

print(card1)
print(card2)

symbols.remove(same_symbol)




