school_journal = {}
keys_for_subjects = []
def add_subjects(*args):
    for i in range(len(args)):
        global school_journal
        global keys_for_subjects
        school_journal[args[0][:3]] = dict({})
        keys_for_subjects.append(args[0][:3])
    return school_journal, keys_for_subjects
subs = int(input('Скок предметов хочешь записать: '))
for _ in range(subs):
    sub = input('Предмет: ')
    add_subjects(sub)
def add_student(a):
    global school_journal
    for i in range(0, len(keys_for_subjects)):
        school_journal[keys_for_subjects[i]] = a
    return school_journal
    


studs = int(input('Скок учеников хош добавить: '))
students = {}
for i in range(studs):
    stud = input('Ученик: ')
    students[stud]= []
add_student(students)
print(school_journal)
def rate_journal(subname, studname, mark ):
    global school_journal
    school_journal[subname][studname].append(mark)
    return school_journal
while True:
    mark = int(input('КАкая оценка? '))
    subname = input("Какой предмет?")
    studname = input('какой ученик?')
    rate_journal(subname, studname, mark)
    isfinich = input('Это все? ')
    if isfinich == 'Yes' or 'Да':
        break
    else:
        continue

print(school_journal)
print(keys_for_subjects)

