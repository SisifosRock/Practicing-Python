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

day = input('What day is it? \n')
while day not in days:
    print('Please insert a valid day')
    day = input('What day is it? ')



def notes_():
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()
    return note

if day != 'saturday':
    sub1 = random.choice(subjects)
    for i in range(len(subjects) - 2):
        if subjects[i] == sub1:
            subjects.pop(i)

    sub2 = random.choice(subjects)
    for i in range(len(subjects) - 2):
        if subjects[i] == sub2:
            subjects.pop(i)

    sub3 = random.choice(subjects)

    print('a)' + sub1)
    a = notes_()
    notes += '\n{}\n{} \n'.format(sub1, a)

    more = str(input('Do you want to study more? ')).lower()
    if more == 'yes':
        print('b)' + sub2)
        b = notes_()
        notes += '\n{}\n{} \n'.format(sub2, b)

        more2 = str(input('Do you want to study more? ')).lower()
        if more2 == 'yes':
            print('c)' + sub3)
            c = notes_()
            notes += '\n{}:\n{} \n'.format(sub3, c)

else:
    sub1 = str(random.choice(subjects))
    for i in range(len(subjects) - 2):
        if subjects[i] == sub1:
            subjects.pop(i)

    sub2 = random.choice(subjects)

    print('a)' + 'Read about the tests and stuff ')
    a = notes_()
    notes += '\n{}: \n{} \n'.format('Read about the tests and stuff ', a)

    print('b)' + sub1)
    b = notes_()
    notes += '\n{}:\n{} \n'.format(sub1, b)

    more = str(input('Do you want to study more? ')).lower()
    if more == 'yes':
        print('c)' + sub2)
        c = notes_()
        notes += '\n{}:\n{} \n'.format(sub2, c)



finish = time.localtime()
finish_hour = '{}:{}'.format(finish.tm_hour, finish.tm_min)
print('Finished at: {}'.format(start_hour))

strt = str('\n\n' + '='*30 + ' Started at ' + start_hour + ', {}/{}/{}'.format(start.tm_mon, start.tm_mday, start.tm_year) + ' ' + '='*30)
fnsh = str('\n\n' + '='*30 + ' Finished at ' + finish_hour + ', {}/{}/{}'.format(finish.tm_mon, finish.tm_mday, finish.tm_year) + ' ' + '='*29)

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
f.write('\n' + day.title() + '\n' + notes)
f.write('\n' + amount)
f.write(fnsh)
f.close()

print('You are done today!')