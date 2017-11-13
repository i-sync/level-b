#!/usr/bin/env python3

import os
import os.path
#def sortbyname(x,y):

mp3 = [x for x in os.listdir() if x.endswith(".mp3")]
mp3.sort(key=lambda x: x.split('.')[1])
#print(mp3)
index=1
name_list = []
for file in mp3:
    name = file[file.index('.'):]
    name ='{0:02d}{1}'.format(index, name)
    print(file, name)
    name_list.append(name)
    index += 1
    os.rename(file, name)

if os.path.exists('names.txt'):
    os.remove('names.txt')

with open('names.txt', 'w') as f:
    for n in name_list:
        f.write('{}\n'.format(n))

