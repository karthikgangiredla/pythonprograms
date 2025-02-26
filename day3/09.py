students = [("Alice", 85), ("Bob", 92), ("Charlie", 67)]
grades = {name: ('A' if score >= 90 else  'B' if score >= 80 else 'C' 
                 if score >= 70 else 'F') for name, score in students}
print(grades)
