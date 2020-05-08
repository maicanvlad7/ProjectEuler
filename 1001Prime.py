def isPrime(n):
    for i in range (2,n//2 + 1):
        if n%i == 0:
            return 0
    return 1

init = 14
toBe = 10001
count = 6

while count != toBe:
    if isPrime(init):
        count = count + 1
    init = init + 1
    
print(count,init-1)