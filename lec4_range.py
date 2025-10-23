a = range(0, 10, 2)
print(a)
print(type(a))
print(a[3])
a = 'GOOD'
for i in range(0, 10, 2):
    if i < len(a):
        print(a[i]+ ' - Bad')
for i in range(0, 10, 1):
    if i < len(a):
        print(a[i]+ ' - Bad')