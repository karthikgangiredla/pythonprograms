def fib(n):
    b=1
    a=0
    c=0
    if n<2:
        return n
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c
l=[fib(i) for i in range(10)]
print(l)