#Aim: To find nth prime number
#Approach: Use find prime numbers until required prime number is reached


def isPrime(n): 
    
    # Corner cases 
    if (n <= 1) : 
        return 0
    if (n <= 3) : 
        return 1
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return 0
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return 0
        i = i + 6
  
    return 1


def nthPrime(k):
    p=0
    i=0
    while True:
        if isPrime(i):
            p += 1
            if p == k:
                print(i)
                break
        i+=1

k = int(input())
nthPrime(k)
