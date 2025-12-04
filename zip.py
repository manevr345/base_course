names = ['John', 'David', 'Maria']
ages = [23, 45, 65]
isTeee = [True, False, False]
users = list(zip(names, ages, isTeee))
print(users)
print('Userage', dict(zip(names, ages)))