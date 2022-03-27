#1
'''
lst = []

with open('file.txt', 'r') as file:
    for line in file:
        lst.append(line.rstrip())

print('\n'.join(lst[::-1]))
'''

#2

from asyncore import write
import os
from tkinter.tix import Tree

from pip import main
res = []
dir = os.walk('main')
for current_dir, dirs, files in dir:
    for file in files:
        if '.py' in file:
            res.append(current_dir.replace('\\', '/'))
            break
#print(current_dir)
#print(dirs)
#print(files)
print('\n'.join(sorted(res)))

with open('new_txt_file.txt', 'w') as f:
    line = '\n'.join(res)
    f.write(line)

