
import re

print(re.match)  # Проверяет подходит ли данная строка шаблону (начало строки или вся строка)
print(re.search)  # Находит первое совпадение с переданным шаблоном (матч быстрее этого метода но этот метон найдет несколько совпадений с шаблоном и необязательно чтоб начало строки начиналось со строки, подходящей под шаблон)
print(re.findall)  # Находит ВСЕ совпадения с шаблоном
print(re.sub)  # Похволяет заменить все совпадения с шаблоном чем-то

'''
. # обозначает просто наличие любого символа
^ # инвертирует/!/not
$ #
* # указывет что мы ожидаем неограниченное [0; + бесконечность) количество какого-то символа -- ab*c ## abbbbc; ac; abbc ЖАДНЫЙ - стремится вовлечь в себя максимальное количество
+ # указывет что мы ожидаем положительное [1; + бесконечность) количество какого-то символа -- ab+c ## abbbbc; abbc ЖАДНЫЙ - стремится вовлечь в себя максимальное количество
? # указывет что мы ожидаем [0; +1] количество какого-то символа -- ab?c ## abc; ac
{ } # указывет что мы ожидаем конкретное количество какого-то символа -- ab{3}c ## abbbc; -- ab{2,4}c ## abbbc; abbbbc; abbc; ЖАДНЫЙ - стремится вовлечь в себя максимальное количество
[ ] #
\ # позволяет сделать метасимвол обычным, а также передать при таком использовани -- r"(\w+)-\1 -- мы сообщаем какую по номеру группу передать
| # OR
( ) # группировка, делает доступным метод groups (нумеруется по открывающей скобке)

[ ] — можно указать множество подходящих символов

^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не-цифра в начале строки).

\d ~ [0-9] — цифры

\D ~ [^0-9]

\s ~ [ \t\n\r\f\v] — пробельные символы

\S ~ [^ \t\n\r\f\v]

\w ~ [a-zA-Z0-9_] — буквы + цифры + _

\W ~ [^a-zA-Z0-9_]

re.IGNORECASE # Передается в любую функцию для того чтобы ингнорировать что-то
re.DEBUG
'''
#1
'''
import re
import sys

pat = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    num = re.findall(pat, line)
    if len(num) >= 2:
        print(line)
'''

#2
'''
import re
import sys

pat = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    num = re.search(pat, line)
    if num != None:
        print(line)
'''

#3
'''
import re
import sys

pat = r"z...z"

for line in sys.stdin:
    line = line.rstrip()
    num = re.search(pat, line)
    if num != None:
        print(line)
'''
#4
'''
import re
import sys

pat = r"\\"

for line in sys.stdin:
    line = line.rstrip()
    num = re.search(pat, line)
    if num != None:
        print(line)
'''
#5
'''
import re
import sys

pat = r"\b[aA]+\b"

for line in sys.stdin:
    line = line.rstrip()
    num = re.sub(pat, 'argh', line, count=1)
    if num != None:
        print(num)
'''
#8
'''
import re
import sys

pat = r"\b(\w)(\w)(\w*)\b"

for line in sys.stdin:
    line = line.rstrip()
    num = re.sub(pat, r'\2\1\3', line, )
    if num != None:
        print(num)
'''
#9
'''
import re
import sys

pat = r"(\w)(\1+)"

for line in sys.stdin:
    line = line.rstrip()
    num = re.sub(pat, r'\1', line)
    if num != None:
        print(num)
'''
#10

import re
import sys

pat = r""

for line in sys.stdin:
    line = line.rstrip()
    num = re.sub(pat, r'\1', line)
    if num != None:
        print(num)

