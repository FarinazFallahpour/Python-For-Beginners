#Farinaz Fallahpour
import random

flag = True
start = 1
end = 99

while flag:
    guess = random.randint(start, end)
    print(guess)
    bkm = input()
    if bkm == 'k':
        end = guess
    elif bkm == 'b':
        start = guess
    elif bkm == 'd':
        flag = False
        print("You win!")
