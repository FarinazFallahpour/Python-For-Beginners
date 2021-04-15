#Farinaz Fallahpour

number = input()
participation = input()
pstrList = participation.split(' ')
team = []
for i in range(0, len(pstrList)):
    element = int(pstrList[i])
    if element <= 2:
        team.append(element)

print(len(team) // 3)
