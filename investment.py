
def invest(amount, rate, time):
    for n in range(1, time+1):
        amount = amount * (1+rate)
        print("Year:", n,"Amount:", amount)

invest(100, .05, 8)
