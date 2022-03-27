number_of_exceptions_class = int(input())
lines = [input() for _ in range(number_of_exceptions_class)]

#print(lines)
grafs = {}
for line in lines:
    if ':' in line:
        key, val = line.strip().split(':')
        key = key.strip(' ')
        if key in grafs:
            grafs.get[key].append(val)
        else:
            grafs.update({key: val.split()})
    else:
        key = line.strip()
        if key not in grafs:
            grafs.update({key: None})

#print(grafs)


def search(exception, graf):
    for key in graf.keys():
        if graf[key] != None and exception in graf[key]:
            handled_exceptions.add(key)
            search(key, graf)


number_of_exceptions = int(input())
input_exceptions = [input() for _ in range(number_of_exceptions)]

#print(input_exceptions)

handled_exceptions = set()

not_to_catch = []

for input_exception in input_exceptions:
    search(input_exception, grafs)
    if input_exception in handled_exceptions and input_exception not in not_to_catch:
        not_to_catch.append(input_exception)
    handled_exceptions.add(input_exception)

print("\n".join(not_to_catch))