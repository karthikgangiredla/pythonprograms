#occurence of vowels in the sentence
s="good morning welcome to the jungle".lower()
d={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in s:
    if i in d.keys():
        d[i]+=1
print(d)
print(sum(d.values()))
# general approach
count=0
for i in s:
    if i in "aeiou":
        count+=1
print(count)