# lcm of 1-10 = 2520

# find lcm of 1-20

lcm = 1

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

# For any number
# n = int(input("Enter number 'n' to print lcm of first n natural numbers:"))


c = sieveEratosthenes(20)                       #n for 20
numbers = [x for x in range(1,21)]              #n+1 for 21

        
print(numbers)       
        

print(range(len(c)))

for i in c:
    
    count = [0 for x in range(len(numbers))]
    
    j = 0
    
    for j in range(len(numbers)):
        
        if numbers[j]%i==0:
            print("now",numbers[j],"on repeated division with",i)
            while(numbers[j]/i>=1 and numbers[j]%i==0):
                numbers[j]/=i
                count[j]+=1
                
            print("becomes",numbers[j])
            
            
        
    print("max = ",max(count))
    for x in range(max(count)):
        lcm*=i        
    print(i,numbers,"\n\n")
            
            
        
    
print(lcm)
