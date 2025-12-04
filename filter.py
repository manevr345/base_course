names = ['John', 'David', 'Maria']
ages = [23, 45, 65]
isTeee = [True, False, False]
def checker(users):
    name, age =users
    return age > 21
users = list(zip(names, ages))
candrenk = list(filter(checker, users))
print(candrenk)