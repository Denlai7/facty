import random

ob1 = "grapes and grapes"
ob2 = "apple"
ob3 = "nail"

bingo = [ob1, ob2, ob3]
random.shuffle(bingo)
print(bingo)

for i in bingo:
    print(i)
    
print(f"Hello\nWorld!")