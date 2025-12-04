name = 'IvanSidoroff'
a = '_'.join(name)
capsup = a.upper()
caplow = a.lower()
mass1 = [ord(symbol) for symbol in capsup]
mass2 = [ord(symbol) for symbol in caplow]
print(capsup)
print(caplow)
print(mass1)
print(mass2)