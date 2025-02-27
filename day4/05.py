def batch(number,size):
    data=list(range(number))
    for i in range(0,number,size):
        end=i+size
        b=list(range(i,end))
        print(b)
batch(50,5)