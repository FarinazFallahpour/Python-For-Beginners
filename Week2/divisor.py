#Farinaz Fallahpour
def divisior(number):
    count = 0
    divider = 1
    while divider <= number:
        if number % divider == 0:
            count += 1
        divider += 1
    return count


maxNumber = 0  # Number
divNumber = 0  # Divisor
for i in range(0, 20):
    number = int(input())
    div = divisior(number)
    if div > divNumber:
        maxNumber = number
        divNumber = div
    elif div == divNumber:
        if number > maxNumber:
            maxNumber = number
            divNumber = div

print(maxNumber, divNumber)
