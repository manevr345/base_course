for symbol in 'hello world':
    if symbol == 'o':
        break
    print(symbol, end =" ")
for symbol in 'hello world':
    if symbol == 'o' or symbol == 'l':
        continue # пропустим эту итерацию
    print(symbol, end ="")