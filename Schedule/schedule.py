""" This is my study schedule for 2018 """

import random
import time

start = time.localtime()
start_min = str(start.tm_min)
if len(start_min) == 1:
    start_min = '0' + start_min

start_hour = '{}:{}'.format(start.tm_hour, start_min)
print('Started at: {}, {}/{}/{}'.format(start_hour,start.tm_mon, start.tm_mday, start.tm_year))

notes = ''

days = ['sunday', 'monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

subjects = ['Mathematics I', 'Mathematics II', 'Mathematics III', 'Physics I','Physics II', 'Physics III',
            'Programming','English', 'Other languages','Programming','Chemistry']

day = input('What day is it? ')
while day not in days:
    print('Please insert a valid day')
    day = input('What day is it? ')

first = ''
second = ''
third = ''

if day == 'sunday':
    sub1 = str(random.choice(subjects)) + ' and ' + str(random.choice(subjects))
    sub2 = random.choice(subjects)
    sub3 = random.choice(subjects)

    while sub2 == sub1:
        sub2 = random.choice(subjects)

    while sub3 == sub1:
        while sub3 == sub2:
            sub3 = random.choice(subjects)

    first += sub1
    second += sub2
    third += sub3

    a = print('a)' + first)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}\n{} \n'.format(sub1, note)

    b = print('b)' + second)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}\n{} \n'.format(sub2, note)

    c = print('c)' + third)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}:\n  {} \n'.format(sub3, note)

elif day == 'saturday':
    sub1 = random.choice(subjects)
    
    first = '8:00am - 10:00am: read about the exams '
    print(first)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}: \n{} \n'.format('read about the exams and stuff ', note)

    second = '1:00pm - 5:00pm: ' + sub1
    print(second)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}:\n{} \n'.format(sub1, note)


else:
    sub1 = random.choice(subjects)
    sub2 = random.choice(subjects)
    sub3 = random.choice(subjects)

    while sub2 == sub1:
        sub2 = random.choice(subjects)

    while sub3 == sub1:
        while sub3 == sub2:
            sub3 = random.choice(subjects)

    first += sub1
    second += sub2
    third += sub3

    a = print('a)' + first)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}\n{} \n'.format(sub1, note)

    b = print('b)' + second)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}\n{} \n'.format(sub2, note)

    c = print('c)' + third)
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()

    notes += '\n{}:\n  {} \n'.format(sub3, note)

finish = time.localtime()
finish_hour = '{}:{}'.format(finish.tm_hour, finish.tm_min)
print('Finished at: {}'.format(start_hour))

strt = str('\n' + '='*30 + ' Started at ' + start_hour + ', {}/{}/{}'.format(start.tm_mon, start.tm_mday, start.tm_year) + ' ' + '='*30)

amount_min = finish.tm_min - start.tm_min

if amount_min < 0:
    amount_min = 60 + amount_min
    amount_hour = finish.tm_hour - start.tm_hour - 1
    if amount_hour == 0:
        amount = 'Study time: {} minute(s) - you need to study more!'.format(amount_min)

    else:
        amount = 'Study time: {} hour(s) and {} minute(s)'.format(amount_hour, amount_min)


else:
    amount_hour = finish.tm_hour - start.tm_hour
    if amount_hour == 0:
        amount = 'Study time: {} minute(s) - you need to study more!'.format(amount_min)

    else:
        amount = 'Study time: {} hour(s) and {} minute(s)'.format(amount_hour, amount_min)

f = open('notes.txt','a')
f.write(strt)
f.write('\n' + day + '\n' + notes)
f.write('\n' + amount)
f.close()

print('You are done today!')

