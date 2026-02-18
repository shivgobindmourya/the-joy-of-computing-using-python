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

symbols.remove(same_symbol)

for i in range(5):
    if i != pos1:
        alphabet1 = random.choice(symbols)
        card1[i] = alphabet1
        symbols.remove(alphabet1)

    if i != pos2:
        alphabet2 = random.choice(symbols)
        card2[i] = alphabet2
        symbols.remove(alphabet2)

print("Card 1:", card1)
print("Card 2:", card2)

ch = input("Spot the common symbol: ")

if ch == same_symbol:
    print("Right")
else:
    print("Wrong")
