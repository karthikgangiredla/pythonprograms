def prime(num):
    if num<2:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
num=50
print([i for i in range(1,num+1) if prime(i)])