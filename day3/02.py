users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,
"Chicago")]
d={k:v for k,v,p in users if v>18}
print(d)