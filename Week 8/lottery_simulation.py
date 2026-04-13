import random
import matplotlib.pyplot as plt

account = 1000
x=[]
y=[]



for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    # print("Bet :",bet)
    # print("Lucky Draw :",lucky_draw)

    if bet==lucky_draw:
        account=account+825-100
    else:
        account=account-100
    y.append(account)

    
print("Amount in Your Game account :",account)

plt.plot(x,y)

plt.show()