# lcm of 1-10 = 2520

# find lcm of 1-20

def sieveEratosthenes(n):
    array = []              #array of primes
    prime = [True for i in range(n+1)]
    p = 2 
    while(p*p <= n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
                
        p+=1
    
    for p in range(2,n):
        if prime[p]:
            array.append(p)
    return array

primes = sieveEratosthenes(20)

lcm = 1

for i in range(len(primes)):
    power = 0
    while primes[i]*primes[i]<20:
        primes[i]*=primes[i]
    lcm*=primes[i]
    
        
print(lcm)
        