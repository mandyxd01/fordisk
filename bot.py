import re
from time import sleep
import requests
from telethon import TelegramClient , events
import os


id= 14295855
hash = "d7c97d558577a8633485c557a41174ef"


client = TelegramClient("main_session"  , api_id=id , api_hash=hash)
chats = [1001781580295, 1001646432242]
mdisk_api = 'vXCZhoG9PKMe0Agyrjfz'
send_to = -1001527597206

footer = "\n━━━━━━━━━━━━━━━\n⚙️ How to Download / Watch Online\n━━━━━━━━━━━━━━━\n⭐️JOIN CHANNEL ➡️ t.me/"

@client.on(events.NewMessage(chats=chats))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , "@X3Links" , caption)
        caption = re.sub("t.me/.*" , "@X3Links" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(send_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(send_to , caption)

    
    


client.start()
client.run_until_disconnected()
