import array
l=array.array('f',[1.1,2.8,3.2,4.5,5.9,6.78,7.1])
product=1
for i in l:
    product*=i
print(product)