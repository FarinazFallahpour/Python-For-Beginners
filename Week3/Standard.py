#Farinaz Fallahpour

listName =[]
for i in range(0,10):
    name = input()
    name = name.lower()
    name = name[0].upper()+name[1:]
    listName.append(name)

for i in range(0,10):
    print(listName[i])
