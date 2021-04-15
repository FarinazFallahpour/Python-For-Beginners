#Farinaz Fallahpour

prompt = input()
l = len(prompt)
flag = True
count = 0
abPos = prompt.find("AB")
baPos = prompt.find("BA")
if abPos < 0 or baPos < 0:
    flag = False
elif abPos > baPos:
    if abPos - baPos <= 1:
        flag = False
elif baPos > abPos:
    if baPos - abPos <= 1:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
