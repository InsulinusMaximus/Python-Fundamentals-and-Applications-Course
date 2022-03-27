#1
'''
s, a, b = (input() for _ in range(3))

counter = 0
while counter <= 1001:
    if a in b and a == s:
        print('Impossible')
        break
    if counter == 1001:
        print('Impossible')
        break
    if a not in s:
        print(counter)
        break
    s = s.replace(a, b)
    counter += 1
'''

#2
s, t = (input() for _ in range(2))

counter = 0
end = len(t)
start = 0
while start < len(s):
    res = s.find(t, start, end)
    if res != -1:
        counter += 1
    start += 1
    end += 1
print(counter)
