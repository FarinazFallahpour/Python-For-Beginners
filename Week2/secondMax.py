#Farinaz Fallahpour
maxAge = 0
maxAge2 = 0
age = int(input())
while age != -1:
    if age > maxAge:
        maxAge2 = maxAge
        maxAge = age
    elif age > maxAge2 and maxAge != age:
        maxAge2 = age
    age = int(input())

print(maxAge, maxAge2)
