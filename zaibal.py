import requests, time
from json import loads

print("""
⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⣿ 
⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿ 
⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿ 
⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠋ 
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⢀ 
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟ 
⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⠃ 
⣿⣿⣿⣿⣿⡆⠄ Yakima⠹⠈⢋⣽⣿⣿⣿⣿⣵⠃ 
⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠄ 
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁ 
⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁ 
⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁ 
⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃  
""")
print('затрахай всех в беседе')
print('------------------------------------')
print('Git: https://github.com/YakimaVisus')
def call(method, options={}, **kwargs):
    '''Фукнция вызова api ВК.'''
    options['access_token'] = tok
    options['v'] = '5.81'
    options.update(kwargs)
    resp = requests.get('https://api.vk.com/method/'+method, params=options).json()
    if 'error' in resp:
        print('VKERROR: {error_code}: {error_msg}'.format(**resp['error']))
    return resp
def send_message(chat_id, textmessage='',photovar=''):
    '''Функция отправки сообщений.'''
    options = {
        'message' : textmessage,
        'chat_id' : chat_id,
    }
    if photovar != '':
        options['attachment'] = 'photo' + photovar
    call('messages.send', options)
    print('Отправлен {message} и {photo} к {chat_id}'.format(message = textmessage, photo = photovar, chat_id = chat_id))
def main(chat_id):
            send_message(chat_id,text, photo)


tok = ('ТУТ ТОКЕН')
chat_id = input('Введите id беседы: ')
text = input('Введите текст для рейда или упоминания хз: ')
photo = ('-202566069_457239025')
e = requests.get("https://api.vk.com/method/messages.getChatUsers?chat_id="+chat_id+"&access_token="+tok+"&v=5.126")
e = loads(e.text)
for obj in e['response']:
    if obj > 0:
        text = text+'   @id'+str(obj)+''
        time.sleep(2)
        print(text)
        main(chat_id)
        