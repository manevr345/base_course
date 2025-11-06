num = input()
soso = list(num)
for i in range(1, len(soso)+1):
    soso[i] = soso[-1]
print(soso)

