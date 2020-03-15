#largest prime factor of 600851475143
import math
a = 600851475143
# a1 = int(input())
b=[]

def primeFactors(n):
    b = []
    n2 = n
    if(n2%2 == 0):
        while n2%2 == 0:
            n2/=2
            b.append(2)
    if(n2%3 == 0):
        while n2%3 == 0:
            n2/=3
            b.append(3)
    
    i = 5
    
    while(i*i<=n2):
        if(n2%i==0):
            n2/=i
            b.append(i)        
        elif(n2%(i+2)==0):
            n2/=(i+2)
            b.append(i+2)
        i+=6
    
    if n2>2:
        b.append(int(n2))
     
    ''' while n2 % 2 == 0: 
        b.append(2), 
        n2 = n2 / 2
          
    
     
    for i in range(3, int(math.sqrt(n2))+1, 2): 
          
        while n2 % i == 0: 
            b.append(i), 
            n2 = n2 / i 
              
   
    if n2 > 2: 
        b.append(int(n2))     ''' 
    return b
b = primeFactors(a)
b.sort(reverse=True)

print ("Largest Prime Factor of ", a,": ", b[0])
print(b,sep = ",")
            
    