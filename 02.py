#highest scorer
d1={"amar":98,"bargav":86,"karthik":100,"ram":74}
marks =0
name=""
for k,v in d1.items():
    if v>marks:
        marks=v
        name=k
print(f"{name} scores {marks}")