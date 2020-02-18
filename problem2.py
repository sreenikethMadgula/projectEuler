#fibonacci

first  = 0

second = 1 

third = first + second

esum = 0

while third<4000000:
    first = second
    second = third
    third = first + second
    
    if third%2 == 0:
        esum+=third
        
    
print(esum)