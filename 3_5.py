import requests
import json

from operator import itemgetter

client_id = 'd635ab6059fa7995d293'
client_secret = 'd8dd7be1831df41dea8749be952498a4'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('Python Basics and Applications/dataset_24476_4.txt') as file:
    dict = {}
    for line in file:
        line = line.strip()
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/{line}".format(line=line), headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        dict.update({j['sortable_name'] : j['birthday']})
dict=sorted(dict.items(), key=itemgetter(1,0))        
for turple in dict:
    print(turple[0])      



