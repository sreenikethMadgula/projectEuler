# sum of squares -- 1^2 + 2^2 + ...
# = n(n+1)(2n+1)/6

n = int(input())

answer = (n)*(n*n-1)*(3*n+2)/12

print("Square of sum of first %d natural numbers - Sum of squares of first %d natural numbers = "%(n,n),answer)