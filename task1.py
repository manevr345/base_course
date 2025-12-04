import random
N = int(input())
def randomi(N):
    mass1 = []
    for i in range(N):
       s = random.randint(0, 100)
       mass1.append(s)
    return mass1
map(randomi(N),)
print(mass1)
print(mass2)
print(max(mass1 + mass2 + mass3))
print(sum(mass1+ mass2 + mass3))