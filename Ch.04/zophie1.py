#!/usr/local/bin/python3

name = 'Zophie'

for i in name:
    if name.index(i) % 2 == 0:
        print ('* * * ' + i + ' * * *')
    else:
        print (' * *  ' + i + '  * * ')

