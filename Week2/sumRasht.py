#Farinaz Fallahpour
win = 0
sum = 0
for i in range(1, 31):
    x = int(input())
    sum = sum + x
    if x == 3:
        win = win + 1
print(sum, win)
