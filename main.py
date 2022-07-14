from pyrogram import Client, types, filters
from config import api_id, api_hash
from time import sleep

app = Client('zxcvvffee', api_id=api_id, api_hash=api_hash)
words = ['бравл', 'дединсайд', 'геншин', 'гейшин', '15', 'машины', 'ищю', 'татар', 'татарка', '🖤', 'покатушки',
         'на машине', 'автозвук']
names = ['ева', 'eva', 'tatarskayamafia']


@app.on_message(filters.chat('leomatchbot'))
def check(penis, msg: types.Message):
    if msg.caption is None:
        return
    string = msg.caption
    name = str(string.replace('\n', '').lower().split(', ')[:1]).replace('[', '').replace(']', '').replace("'", "")
    age = int(string.replace('\n', '').lower().split(',')[1].split(', ')[0].strip())
    text = str(string.replace('\n', '').lower().split(', ')[2:]).replace('[', '').replace(']', '').replace("'", "")
    if name in names:
        app.send_message(chat_id='leomatchbot', text='👎')
    if age == 15 or any(word in text for word in words):
        app.send_message(chat_id='leomatchbot', text='👎')


@app.on_message(filters.chat('zxcvvffee'))
def admin(penis, msg: types.Message):
    temp_string = ""
    if msg.text == 'words':
        for word in words:
            temp_string += f"{word}, "
        app.edit_message_text('me', message_id=msg.id, text=temp_string)
        sleep(1.5)
        app.delete_messages('me', message_ids=msg.id)
    if msg.text[0:8] == 'add.word':
        words.append(msg.text[9:].replace(' ', ''))
        app.edit_message_text('me', message_id=msg.id, text='ADDED')
        sleep(1.2)
        app.delete_messages('me', message_ids=msg.id)

    if msg.text[0:8] == 'pop.word':
        words.remove(msg.text[9:].replace(' ', ''))
        app.edit_message_text('me', message_id=msg.id, text='POPED')
        sleep(1.2)
        app.delete_messages('me', message_ids=msg.id)



    if msg.text == 'names':
        for name in names:
            temp_string += f"{name}, "
        app.edit_message_text('me', message_id=msg.id, text=temp_string)
        sleep(1.5)
        app.delete_messages('me', message_ids=msg.id)
    if msg.text[0:8] == 'add.name':
        names.append(msg.text[9:].replace(' ', ''))
        app.edit_message_text('me', message_id=msg.id, text='ADDED')
        sleep(1.2)
        app.delete_messages('me', message_ids=msg.id)

    if msg.text[0:8] == 'pop.name':
        names.remove(msg.text[9:].replace(' ', ''))
        app.edit_message_text('me', message_id=msg.id, text='POPED')
        sleep(1.2)
        app.delete_messages('me', message_ids=msg.id)

app.run()
