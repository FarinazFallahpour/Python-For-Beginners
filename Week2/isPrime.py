#Farinaz Fallahpour
number = int(input())
flag = True
end = number // 2
divider = 2
while flag and divider <= end:
    if number % divider == 0:
        flag = False
    else:
        divider += 1
if flag:
    print("prime")
else:
    print("not prime")
