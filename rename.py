#!/usr/bin/env python3

import os

#def sortbyname(x,y):

mp3 = [x for x in os.listdir() if x.endswith(".mp3")]
mp3.sort(key=lambda x: x.split('.')[1])
#print(mp3)
index=1
for file in mp3:
    name = file[file.index('.'):]
    name ='{0:02d}{1}'.format(index, name)
    print(file, name)
    index += 1
    os.rename(file, name)



