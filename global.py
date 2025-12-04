counter = 0
def update(a):
    global counter
    result = counter + a
    counter = result
    return result
update(5)
print(f'{counter = }')