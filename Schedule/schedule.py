""" This is my study schedule for 2018 """

import random
import time

def start():
    start = time.localtime()
    start_min = str(start.tm_min)
    if len(start_min) == 1:
        start_min = '0' + start_min

    start_hour = '{}:{}'.format(start.tm_hour, start_min)
    started = 'Started at: {}, {}/{}/{}'.format(start_hour,start.tm_mon, start.tm_mday, start.tm_year)

    return (started, start_hour)

notes = ''

days = ['sunday', 'monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

subjects = ['Mathematics I', 'Mathematics II', 'Mathematics III', 'Physics I','Physics II',
            'Physics III', 'Programming','English', 'Other languages','Programming','Chemistry',
            'Python', 'Java', 'Web development', 'C++', 'Data Science', 'Biology']

day = str(input('What day is it? \n')).lower()
while day not in days:
    print('Please insert a valid day')
    day = str(input('What day is it? \n')).lower()



def notes_():
    x = 1
    note = str(x) + '- ' + str(input('Notes? \n'))
    ask = str(input('Anymore notes? \n')).lower()
    while ask == 'yes':
        x += 1
        note += '\n' + str(x) + '- ' + str(input('\n  \n'))
        ask = str(input('Anymore notes? \n')).lower()
    return note



def notes_save(sub):

    finish = time.localtime()
    finish_hour = '{}:{}'.format(finish.tm_hour, finish.tm_min)
    finished = 'Finished at: {}, {}/{}/{}'.format(finish_hour,finish.tm_mon, finish.tm_mday, finish.tm_year)

    strt = str('\n\n' + '=' * 30 + start()[0] + ' ' + '=' * 30)
    fnsh = str('\n\n' + '=' * 30 + finished + ' ' + '=' * 29)

    amount_min = finish.tm_min - int(start()[1][-2:])

    if amount_min < 0:
        amount_min = 60 + int(start()[1][-2:])
        amount_hour = finish.tm_hour - int(start()[1][:2]) - 1
        if amount_hour == 0:
            amount = 'Study time: {} minute(s)'.format(amount_min)

        else:
            amount = 'Study time: {} hour(s) and {} minute(s)'.format(amount_hour, amount_min)


    else:
        amount_hour = finish.tm_hour - int(start()[1][:2])
        if amount_hour == 0:
            amount = 'Study time: {} minute(s)'.format(amount_min)

        else:
            amount = 'Study time: {} hour(s) and {} minute(s)'.format(amount_hour, amount_min)

    f = open('Notes/' + str(sub) + ' - Notes.txt', 'a')
    f.write(strt)
    f.write('\n' + day.title() + '\n' + notes)
    f.write('\n' + amount)
    f.write(fnsh)
    f.close()


def save(sub):
    save = str(input('Do you want to continue studying this subject later? ')).lower()
    if save == 'yes':
        save_file = open('save/save.txt ', 'a')
        save_file.write(sub + '\n')
        save_file.close()
    return None

def save_(sub):
    save_file = open('save/save.txt ', 'a')
    save_file.write(sub + '\n')
    save_file.close()
    return None

def load_data():
    file = open('save/save.txt', 'r')
    sub = file.readlines()
    file.close()
    return sub

def delete_data():
    file = open('save/save.txt', 'w')
    file.close()
    return None

sub1 = random.choice(subjects)
for i in range(len(subjects) - 2):
    if subjects[i] == sub1:
        subjects.pop(i)

sub2 = random.choice(subjects)
for i in range(len(subjects) - 2):
    if subjects[i] == sub2:
        subjects.pop(i)
        
sub3 = random.choice(subjects)

warranty = load_data()

load = str(input('Load continuation of study? ')).lower()
if load == 'yes':
    assert len(load_data()) > 0, 'No schedule saved'

    sub1 = load_data()[0][:-1]
                
    if len(load_data()) > 1:
        if load_data()[1][:-1] != '':
            sub2 = load_data()[1][:-1]
    
    if len(load_data()) > 2:
        if load_data()[2] != '':
            sub3 = load_data()[2]

    delete_data()


    start()
    print('a)' + sub1)
    a = str(notes_())
    notes = '\n{}\n{} \n'.format(sub1, a)
    notes_save(sub1)

    save(sub1)

    more = str(input('Do you want to study more? ')).lower()
    if more == 'yes':

        start()
        print('b)' + sub2)
        b = str(notes_())
        notes = '\n{}\n{} \n'.format(sub2, b)
        notes_save(sub2)

        save(sub2)

        more2 = str(input('Do you want to study more? ')).lower()
        if more2 == 'yes':

            start()
            print('c)' + sub3)
            c = str(notes_())
            notes = '\n{}:\n{} \n'.format(sub3, c)
            notes_save(sub3)

            save(sub3)

    else:
        if len(warranty) > 2:
            ask = str(input('Do you want to keep the saved schedule?\n'))
            if ask == 'yes':
                save_(sub2)
                save_(sub3)
        elif len(warranty) == 2:
            ask = str(input('Do you want to keep the saved schedule?\n'))
            if ask == 'yes':
                save_(sub2)



else:
    if len(load_data()) > 0:
        keep = str(input('Do you want to keep the saved schedule?\n')).lower()
        if keep != 'yes':
            delete_data()

    start()
    print('a)' + sub1)
    a = str(notes_())
    notes = '\n{}\n{} \n'.format(sub1, a)
    notes_save(sub1)

    save(sub1)

    more = str(input('Do you want to study more? ')).lower()
    if more == 'yes':

        start()
        print('b)' + sub2)
        b = str(notes_())
        notes = '\n{}\n{} \n'.format(sub2, b)
        notes_save(sub2)

        save(sub2)

        more2 = str(input('Do you want to study more? ')).lower()
        if more2 == 'yes':

            start()
            print('c)' + sub3)
            c = str(notes_())
            notes = '\n{}:\n{} \n'.format(sub3, c)
            notes_save(sub3)

            save(sub3)

print('You are done today!')