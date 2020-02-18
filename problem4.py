#Largest palindromic product of two 3-digit no.s
import math
def checkDigits(n):
    n2 = n
    d = 1
    while int(n2/10)!=0:
        d+=1
        n2 = int(n2/10)
        # print(n2)
    return d

# print(checkDigits(45))

def getDigits(n):
    d=[]
    n2 = n
    l = checkDigits(n)
    # print(l)
    for i in range(l):
        d.append(n2%10)
        n2 = int(n2/10)
    
    return d

def checkPalindrome(n):        
    d = checkDigits(n)
    # print("\n",n)
    # print("\nNo. of digits: ",d)
    digits = getDigits(n)
    # print("\nDigits: ", digits)
    flag = 0
    if d%2!=0:
        for i in range(d):
            if i == int(d/2):
                break
            else:
                if(digits[i]==digits[d-1-i]):
                    # print("\n",digits[i],digits[d-1-i])
                    flag = 0
                else:
                    flag = -1
                    # print("\n",digits[i],digits[d-1-i])
                    break
    else:
        # print("Even")
        for i in range(d):
            if(digits[i]==digits[d-1-i]):
                # print("\n",digits[i],digits[d-1-i])
                flag = 0
            else:
                # print("\n",digits[i],digits[d-1-i])
                flag = -1
                break
    if(flag==0):
        return 1
    else:
        return 0        

# a = int(input())
# checkPalindrome(a)
product = 10
palindrome = []

o= []

a = 902
l = 990
d = 11
n = int((l-a)/d) +1
for i in range(n):
    o.append(a+(i*d))



print(o)
i = 0
for i in range(n):
    for j in range(i,n):
        product = o[i]*o[j]
        if checkPalindrome(product)==1:
            palindrome.append(product)
            print(product)

for i in range(n):
    for j in range(11):
        product = o[i] * (990+j)
        if checkPalindrome(product)==1:
            palindrome.append((product))
            print(o[i], "x", 990+j, " = ", product)
            # print(product)

# palindrome.sort(reverse=True)

# print(palindrome[0])
    