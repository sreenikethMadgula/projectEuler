# lcm of 1-10 = 2520

# find lcm of 1-20

a = [x for x in range(1,21)]
print(a)
lcm = 1
def isPrime(n) : 
  
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

def sieveEratosthenes(n):
    c= []
    prime = [True for i in range(n+1)]
    p = 2 
    while(p*p <= n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
                
        p+=1
    
    for p in range(2,n):
        if prime[p]:
            c.append(p)
    return c
c = sieveEratosthenes(10)

d = {}

np = []  #NON PRIMES


for x in a:
    d[x]=isPrime(x)
    if d[x] == 1 and x>10:
        # print(x)
        lcm *= x
        print(" ",lcm)
        d[x] = 0
    else:
        np.append(x)
        
print(np)       
        

print(range(len(c)))

for i in c:
    
    count = [0 for x in range(len(np))]
    
    j = 0
    
    for j in range(len(np)):
        
        if np[j]%i==0:
            print("now",np[j],"on repeated division with",i)
            while(np[j]/i>=1 and np[j]%i==0):
                np[j]/=i
                count[j]+=1
                
            print("becomes",np[j])
            
            # j+=1
        
    print("max = ",max(count))
    for x in range(max(count)):
        lcm*=i        
    print(i,np,"\n\n")
            
            
        
    
print(lcm)
