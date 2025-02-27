import random
l=[i for i in [random.randint(0,100) for _ in range(10)]]
print(sum(l),sum(l)/len(l))