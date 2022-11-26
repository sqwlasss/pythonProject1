nums=range(1,1000)

def prime(num):
    for x in range(2,num):
        if(num%x) == 0:
            return False
    return True
primes=list(filter(prime, nums))
print(primes)
