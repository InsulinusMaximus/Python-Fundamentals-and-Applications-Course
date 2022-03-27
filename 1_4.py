'''
x, y = 1, 2

def foo():
    global y
    if y == 2:
        x = 2
        y = 1

foo()
print(x)
if y == 1:
    x = 3
print(x)
'''

# 1 Namespace

n = int(input())
graph = {'global': []}
result = []


def search(graph, spacename, arg):
    if arg in graph[spacename]:
        return spacename
    else:
        for key in graph:
            if spacename in graph[key]:
                return search(graph, key, arg)


while n != 0:
    query, spacename, arg = input().split()
    if query == 'create':
        graph[arg].append(spacename)
        graph.update({spacename: []})
    elif query == 'add':
        graph[spacename].append(arg)
    elif query == 'get':

        result.append(search(graph, spacename, arg))
    n -= 1

print('\n'.join(map(str, result)))
