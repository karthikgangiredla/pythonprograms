#highest scorer
d1={"amar":98,"bargav":86,"karthik":100,"ram":74}
marks =0
name=""
for k,v in d1.items():
    if v>marks:
        marks=v
        name=k
print(f"{name} scores {marks}")
#good pairs
nums = [1,2,3,1,1,3]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            count+=1
#l=[(i,j) for i in range(len(nums)) for j in range(i+1,len(nums)) if(nums[i]==nums[j])] #list comprehension
#print(len(l))
print(count)
#return duplicates from list
l=[1,2,3,4,2,3,4,5]
print(list(set(l)))