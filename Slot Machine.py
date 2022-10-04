import random
i=1
money=10
print("Welcome to the game")
def slot_machine(money):
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    if a == b == c:
        print(a,b,c)
        print('Jackpot!')
        return money + 9.75
    elif a == b or b == c or a == c:
        print(a,b,c)
        print('Hmm... 2nd Prize')
        return money + 0.25
    else:
        print(a,b,c)
        print('Lost')
        return money - 0.25

      
while (i == 1) or (i == 2) or (i == 3):
    i = int(input('Choose the option:'))
    if (i == 1):
        money = slot_machine(money)
        print('Your current money is',money)
        while money <= 0:
            print('You are out of money. Goodbye')
            break

    elif (i == 2):
        print("Let's take a rest")
        print("Your current money is",money)
    elif (i == 3):
        print("The money you gonna take is",money,"Goodbye")
# Phan Thi Mai Phuong
    
                

        