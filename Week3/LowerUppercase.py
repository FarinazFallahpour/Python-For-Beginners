#Farinaz Fallahpour

prompt = input()
lower = 0
upper = 0
for i in range(0, len(prompt)):
    if prompt[i].islower():
        lower += 1
    else:
        upper += 1
if upper > lower:
    print(prompt.upper())
else:
    print(prompt.lower())
