import re
from time import sleep
import requests
from telethon import TelegramClient , events
import os
from telethon.sessions import StringSession


id= 14295855
hash = "d7c97d558577a8633485c557a41174ef"

print("Starting Deployment..!")
client = TelegramClient("main2str" , api_id=id , api_hash=hash)

#mdiskapi
mdisk_api = 'jNgyWyCG2KK4tvh5RVFX'
sapi= '1832790492-eakHGycryH'
#footer
footer = '''\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⭐️JOIN OUR BACKUP CHANNEL
➡️https://t.me/+_NZFqNwyfHpmYTcx'''

black = ["Adult Whatsapp Group Join Karne Ke Liye Click Kare 👇👇👇👇","Gb Whatsapp Download Karne Ke Liye Click Kare 👇👇👇","Please Join Our Backup Channel :-","https://www.instagram.com/haq.sebakchodi/","𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇","❤Earning app🤑🤑","http://share.royalgame.in?invite_code784297","💟𝗕𝗘𝗦𝗧 𝗘𝗔𝗥𝗡𝗜𝗡𝗚 𝗔𝗣𝗣","https://www.boow.in/agent-74-1782101","⭐JOIN OUR BACKUP CHANNEL","➡","Must watch guys🔥🔥🔥","Join backup channel 👇","Cricket fans ke liye bahut sunhara mauka khele free contest and win kre daily 1lac","Is IPL season daily 1000k","prize 🏆","https://assets-1.mdisk.me/assets/apk/Winner11-1.02.apk","❤Join Channel❤","➡️","⭐️JOIN OUR BACKUP CHANNEL","Aagya INDIA'S 1st FREE WINNING Fantasy APP","Visit :- www.winner11.net","Install now 👇","https://mdisk.me/convertor/203x360/jn2SYC","@ EZINETWORK","Must watch 🤩🤩🔥🔥🔥🔥","Join Our Telegram Backup Channel In Case This Channel Delete Please Join It Please👇👇","Must watch Guys 🔥🔥🔥🔥🔥","Enjoy it ❤❤❤","♨️ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙺𝙰𝚁𝙽𝙴 𝙽𝙰𝙷𝙸 𝙰𝙰𝚁𝙰 𝚃𝙾𝙷 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙲𝙷𝙴𝙲𝙺 𝙺𝙰𝚁𝙾","👉 🅱🅰🅲🅺🆄🅿  🅲🅷🅰🅽🅽🅴🅻","=" ,"●╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼●" ,"🔥Backup file🔥" ,"🔥Join channel 🔥" ,"JOIN CHANNEL 👇" ,"Join adult network🍌💦" ,"SHARE OUR CHANNEL👇" ,"𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹" ,"𝐉𝐎𝐈𝐍 𝐔𝐒 ➪" ,"🙆‍♀ Join Our Backup:- ","Join now best channel" ,"♨️ SEARCH & JOIN NOW👇","☆☆☆••••••••••••••••☆☆☆","➥"]

##### ios new

iosNewS = [-1001320268729,-1001269643652,-1001592280578,-1001725626602]
iosNewD = -1001146630538

#eng variables
indchats = [-1001679399038,-1001599913233,-1001794604239,-1001316413287,-1001665192861,-1001626636022,-1001168213397,-1001708628164,-1001562499878,-1001493682832]
indsend_to1 = -1001607066545


#webseries var 
webchat = [-1001593607523,-1001028498885,-1001708829219,-1001421452039,-1001725626602]
websend_to = -1001649482502

#desi vars
deschat = [-1001711248489,-1001541608805,-1001767045981,-1001303095255,-1001314689320,-1001387860550,-1001250363281,-1001314689320,-1001138671226,-1001461291601]
dessend_to = -1001754232236

#tango vars
tanchat = [-1001330259957,-1001785029855,-1001745646849,-1001577675291,-1001568191558,-1001589153647]
tansend_to = -1001591226590


#onlyfans vars  
onchat = [-1001608452561,-1001199943325,-1001491824023]
onsend_to = -1001295828233   




############### ENGLISH 1 ##########

@client.on(events.NewMessage(chats=indchats))
async def hello1(event):

    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        
        caption = re.sub("hehe" , "" , caption)
        
        caption = re.sub("hoho" , "" , caption)
        caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
        caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
        caption = re.sub("https://t.me/open_streaam/14" , "https://t.me/Watch_Streaam_Links/9" , caption)



        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , "@X3Links" , caption)
        caption = re.sub("t.me/.*" , "@X3Links" , caption)
        caption = re.sub("T.me/.*" , "@X3Links" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n"
        if media:
            await client.send_file(indsend_to1,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to1, caption)
            
            
            
            ###############  IOS ##########

@client.on(events.NewMessage(chats=iosNewS))
async def hello2(event):
    # chat = await event.get_chat()
    caption = event.message.message
    # link syntax = https://streaam.net/S/$UydxddrFxb 
    urls_to_change = re.findall('https?://streaam.net/S/.*' , caption)
    # print(urls_to_change)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 

        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
        caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
        caption = re.sub("https://t.me/open_streaam/14" , "https://t.me/Watch_Streaam_Links/9" , caption)
   
        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)
        caption = re.sub("T.me/.*" , "" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)
            
        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            linkid = link.split("/")[-1]
            # print(linkid)
            key = sapi
            url  = f'https://api.streaam.net/save?linkid={linkid}&key={key}'
            # print(url)
            # param = {
            #     'token': mdisk_api,
            #     'link':link.strip()
            #     }
            try:
                res = requests.get(url)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['link']
            except:
                print("error in share")
                shareLink = ""
            print("changed link : " , shareLink)
            caption = re.sub(re.escape(i) , shareLink , caption)
            # print(caption)
            # sleep(0.2)
        caption = caption + "\n"
        if media:
            await client.send_file(iosNewD, file=media, caption=caption)
            os.remove(media)
        else:
            await client.send_message(iosNewD, caption)



  ##################### WEBSERIES #############  

@client.on(events.NewMessage(chats=webchat))
async def hello3(event):
    # chat = await event.get_chat()
    caption = event.message.message
    # link syntax = https://streaam.net/S/$UydxddrFxb 
    urls_to_change = re.findall('https?://streaam.net/S/.*' , caption)
    # print(urls_to_change)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 

        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
        caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
        caption = re.sub("https://t.me/open_streaam/14" , "https://t.me/Watch_Streaam_Links/9" , caption)
   
        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)
        caption = re.sub("T.me/.*" , "" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)
            
        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            linkid = link.split("/")[-1]
            # print(linkid)
            key = sapi
            url  = f'https://api.streaam.net/save?linkid={linkid}&key={key}'
            # print(url)
            # param = {
            #     'token': mdisk_api,
            #     'link':link.strip()
            #     }
            try:
                res = requests.get(url)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['link']
            except:
                print("error in share")
                shareLink = ""
            print("changed link : " , shareLink)
            caption = re.sub(re.escape(i) , shareLink , caption)
            # print(caption)
            # sleep(0.2)
        caption = caption + "\n"
        if media:
            await client.send_file(dessend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(dessend_to , caption)
            
            
  
############ TANGO ###############

@client.on(events.NewMessage(chats=tanchat))
async def hello5(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , "@X3Links" , caption)
        caption = re.sub("t.me/.*" , "@X3Links" , caption)
        caption = re.sub("T.me/.*" , "@X3Links" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(tansend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(tansend_to , caption)
            
        
########### ONLYFANS #####################
@client.on(events.NewMessage(chats=onchat))
async def hello6(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , "@X3Links" , caption)
        caption = re.sub("t.me/.*" , "@X3Links" , caption)
        caption = re.sub("T.me/.*" , "@X3Links" , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(onsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(onsend_to , caption)


         


    
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()




