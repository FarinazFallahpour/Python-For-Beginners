#Farinaz Fallahpour
maxAge = 0
flag = True
while flag:
    age = int(input())
    if age == -1:
        flag = False
    elif age > maxAge:
        maxAge = age
print(maxAge)
