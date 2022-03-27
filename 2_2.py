'''
import sys

for path in sys.path:
    print(path)
'''
#1
'''
import datetime

y, m, d = input().split()

y, m, d = map(int, [y, m, d])

base_date = datetime.date(y, m, d)

delta = datetime.timedelta(days=int(input()))

new_date = base_date + delta

print(new_date.year, new_date.month, new_date.day)
'''

#2
'''
import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

passwords = open('passwords.txt', 'r')
for password_alise in passwords.readlines():
    password_alise = password_alise.strip()
    try:
        print(simplecrypt.decrypt(password_alise, encrypted))
    except:
        print('Error')
'''






