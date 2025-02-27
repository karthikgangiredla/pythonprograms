import random

def randomteam(l):
    l1=list(l.split("\n"))
    m=len(l1)
    random.shuffle(l1)
    d={i//2+1:tuple(l1[i:i+2])  for i in range(0,m,2)}
    return d
d=randomteam("""Chris Harry K
Siddartha Kommu
Mayank Pathak
Balaji Pappala
Sumanth Kumar Valluru
Japa Harish
Lakshmi Sahithi Vanga
G.VANI
Indukuru Sravani
Sirneni Pavan Sai
Suman Kumar Ghorai
Yugesh Karoti
chundi vishnu priya
Sri Sanjana Indugula
G Santosh Kumar
GANGIREDLA KARTHIK
Venkata Naidu Punnana
pedapalli suresh
Prathamesh Pahune
Venkata Krishna kolli
Ram Mishra""")
for k,v in d.items():
    print(f"team {k} is {v}") 