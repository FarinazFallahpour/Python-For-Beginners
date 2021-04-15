#Farinaz Fallahpour

def isPalindrome(x):
    x = x.lower()
    length = len(x) // 2
    count = 0
    while count < length:
        if x[-1-count] != x[count]:
            return False
        count +=1
    return True


string = input()
if isPalindrome(string):
    print("palindrome")
else:
    print("not palindrome")
