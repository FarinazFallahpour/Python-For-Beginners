#Farinaz Fallahpour

prompt = input()
l = len(prompt)
counter = 0
flag = False
while counter < l and not flag:
    posh = prompt[counter:l].find('h')
    if posh >= 0:
        pose = prompt[posh + 1:l].find('e')
        if pose >= 0:
            posl1 = prompt[posh + pose + 2:l].find('l')
            if posl1 >= 0:
                posl2 = prompt[posh + pose + posl1 + 3:l].find('l')
                if posl2 >= 0:
                    poso = prompt[posh + pose + posl1 + posl2 + 4:l].find('o')
                    if poso >= 0:
                         flag = True
                    else:
                        flag = False
                else:
                    flag = False
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False
    counter += 1

if flag:
    print("YES")
else:
    print("NO")
