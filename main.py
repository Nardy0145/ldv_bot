from pyrogram import Client, types, filters
from config import api_id, api_hash

app = Client('zxcvvffee', api_id=api_id, api_hash=api_hash)
words = ['бравл', 'дединсайд', 'геншин', 'гейшин', '15', 'машины', 'ищю', 'татар', 'татарка', '🖤', 'покатушки', 'на машине', 'автозвук']
names = ['ева', 'eva']

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
app.run()