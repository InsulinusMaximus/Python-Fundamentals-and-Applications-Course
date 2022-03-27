'''
import csv, re

with open ('Python Basics and Applications/Crimes.csv') as file:
    reader = csv.DictReader(file)
    

    dict_crimes = {}
    for line in reader:
        #print(line) 
        pat = '\w{2}/\w{2}/2015\s'
        find = re.search(pat, line['Date'])
        if find != None:
            if line['Primary Type'] in dict_crimes:
                dict_crimes[line['Primary Type']] += 1
            else:
                dict_crimes.update({line['Primary Type'] : 1})
    max_num = 0
    max_key = str()
    for key, num in dict_crimes.items():
        if num > max_num:
            max_num = num
            max_key = key
    print(max_key)
'''

import json

js = json.loads(input())
dic1 = {}
dic2 = {}

for dir in js:
    dic1.update({dir['name'] : dir['parents']})
    dic2.update({dir['name'] : 1})

def search(child, parents=[]):
    for parent in parents:
        if parent not in visited:
            try:
                dic2[parent] += 1
            except:
                dic2.update({parent : 1})
            visited.append(parent)
            search(child, dic1[parent])

for child, parents in dic1.items():
    visited = []
    search(child, parents)

for k_v in sorted(dic2.items()):
    print(k_v[0] + ' : ' + str(k_v[1]))