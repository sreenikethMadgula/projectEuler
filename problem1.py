#multiples of 3 & 5. sum before 1000
''' a=0
i=0
while i<1000:
    if i%3 == 0:
        a += i
    if i%5 == 0:
        a+=i
    if i%15==0:
        a-=i
    i+=1
    
print(a) '''

#Method of AP

# l = a + (n-1)d
# s = n/2(a + l)



a1 = 3 
a2 = 5 
a3 = 15

d1 = 3
d2 = 5
d3 =15

l1 = 999
l2 = 995
l3 = 990

n1 = int((l1 - a1) /d1 + 1)
n2 = int((l2 - a2) /d2 + 1)
n3 = int((l3 - a3) /d3 + 1)

s1 = int(n1/2*(a1 + l1))
s2 = int(n2/2*(a2 + l2))
s3 = int(n3/2*(a3 + l3))

sum1 = s1 + s2 - s3
print(sum1)