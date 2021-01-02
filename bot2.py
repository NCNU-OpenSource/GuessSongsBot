# -*- coding: utf-8 -*-
import telepot
import urllib.request
from urllib.parse import quote
import re
import random
import pafy                                                                                                                                 
import vlc    
# import requests
# from bs4 import BeautifulSoup
from pytube import YouTube
import time
import speech_recognition as sr
from telepot.loop import MessageLoop
import logging
# import ftransc.core as ft
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) 
bot = telepot.Bot('1050112594:AAHu5aEBiIROVw-nFhK5AlNqyGvHqUFTfp4')
# 抓歌曲 

def music(search_keyword) :
    # time.time() = 0
    a = quote(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + a)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(len(video_ids))
    num = random.randint(0,len(video_ids)-1)
    print('num',num)
    url = "https://www.youtube.com/watch?v=" + video_ids[num] + "#t=1m23s"
    yt = YouTube(url)
    # print("url2",url)
    length = yt.length
    print("len",length)
    result = yt.title
    web = yt.video_id
    print('result',result)
    print('web',web)
    # result_no_eng = re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?\(\)\》\《]", "", result)
    print('result',result)
    # print('noeng',result_no_eng)
    a = 'remix'
    b = 'cover'
    c = 'Cover'
    d = '翻唱'
    result = result.replace('[','【')
    result = result.replace('《','【')
    result = result.replace('『','【')
    string = "【"
    if string not in result :
        music(search_keyword)
    # find = re.findall('cover', result, flags=re.IGNORECASE)
    # tmp = str(find)
    # print('find',)
    # find1 = re.findall('remix', result, flags=re.IGNORECASE)
    # print('find1',find1)
    # if find != None:
    #     music(search_keyword)
    if a in result or b in result or c in result or d in result or length > 480:
        print('11',result)
        url = ''
        music(search_keyword)
        # new_set = new_set + 1
    # if result_no_eng == '':
    #     music(search_keyword)
    donename = check(url,result)
    donename2 = str(donename)
    print('donename',donename2)
    result_no_eng = re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?\(\)\》\《]", "", donename2)
    if result_no_eng == '':
        music(search_keyword)
    # if donename.isalpha() == True:
    #     music(search_keyword)
    # print("id",video_ids[num])
    print('url1',url)
    print("https://www.youtube.com/watch?v=" + video_ids[num])
# print(url)
# url = "https://www.youtube.com/watch?v=G0OqIkgZqlA"   
    print('url1',url)
    print('donename2',donename2)
    return url,donename2

# 利用VLC播放歌曲
def paly_music(url,game):
    print('plat_music',url)
    video = pafy.new(url)                                                                                                                       
    best = video.getbestaudio()                                                                                                                 
    playurl = best.url              
    # print("a")                                                                                                            
    player = vlc.MediaPlayer(playurl)     
    # print("b")                                                                                            
    player.play()
    print('gameplay',game)
    timeout = time.time() + playtime[game-1]
    # name = check(url,result)
    # answertalk(name)
    # answerinput(name)

    # print('siad',said)
    # while said is None:
    #     print("a")
    #     answertalk(name)
    print('time',time.time())
    print('timeout',timeout)
    while True:
        if time.time() > timeout:
            player.stop()
            print("這題結束了~")
            break


    # time.sleep(60) # 讓程式暫停指令的秒數

# def transcribe_voice(bot, context):
#     print('context',context)
#     duration = context['voice']['duration']
#     print('duration',duration)
#     durationstr = str(duration)
#     # logger = logging.getLogger(__name__)
#     logging.info('transcribe_voice. Message duration: '+durationstr)
    
#     # Fetch voice message
#     voice_id = context['voice']['file_id']
#     voice = bot.getFile(voice_id)
    
#     # Transcode the voice message from audio/x-opus+ogg to audio/x-wav
#     # One should use a unique in-memory file, but I went for a quick solution for demo purposes
#     ft.transcode(voice.download('file.ogg'), 'wav')
    
#     # extract voice from the audio file
#     r = sr.Recognizer()
#     with sr.WavFile('file.wav') as source:
#         #r.adjust_for_ambient_noise(source) # Optional
#         audio = r.record(source)
        
#     # Convert voice to text
#     try:
#         txt = r.recognize_google(audio)
#         logger.info(txt)
#     except sr.UnknownValueError:
#         logger.warn('Speech to Text could not understand audio')
#     except sr.RequestError as e:
#         logger.warn('Could not request results from Speech to Text service; {0}'.format(e))
    
#     # return the voice message in text format
#     context.message.reply_text(txt)     

# 處理歌名雜訊
def check(url,result):
    result = result.replace('[','【')
    result = result.replace('《','【')
    result = result.replace('『','【')
    result = result.replace(']','】')
    result = result.replace('》','】')
    result = result.replace('』','】')
    string = "【"
    string2 = "】"
    # string3 = "["
    # string4 = "]"
    # string5 = "《"
    # string6 = "》"
    # string7 = "『"
    # string8 = "』"
    # string9 = "("
    # string10 = ")"
    # video_list = []
    # video_list2 = []
    # video_list3 = []
    # video_list = str(result)
    print('re',result)
    # video_list2 = re.sub("[\s\,\。]", "",video_list)
    # print('22',video_list2)
    # video_list3 = video_list2[2:-2]
    # print('33',video_list3)
        # yesorno = re.compile('[]<>')
        # yesorno.findall(video_list)
        # for i in string:
    if string in result :

            # for j in string2:
            #     if j in video_list2:
        pos1 = result.find(string)
        pos2 = result.find(string2)
            # print("oh no")
        ans = result[pos1+1:pos2]
        ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\s\。\-\?\.]", "", ans)
        # if string9 in anstmp :
        #     pos3 = anstmp.find(string9)
        #     pos4 = anstmp.find(string10)
        #     remove = anstmp[pos3:pos4]
        #     ansmin = ansmin.replace(remove,"")
        # print(pos1)
        # print(pos2)
        # print(ans)
        # print(remove)
        print("ansmin",ansmin)
        return ansmin


    # elif string3 in result:
    #         # for i in string3:
    #             # if i in video_list2:
    #                 # for j in string4:
    #                 #     if j in video_list2:
    #     pos1 = result.find(string3)
    #     pos2 = result.find(string4)
    #         # print("oh no")
    #     z = 0
    #     if pos1 == z:
    #         ans = result[pos1+2:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\。\s\-\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #         return ansmin
    #     else : 
    #         ans = result[pos1+1:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\。\s\-\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #     # print(pos1)
    #     # print(pos2)
    #     # print(ans)
    #     # print(remove)
    #     print("ansmin",ansmin)
    #     return ansmin
    # elif string7 in result:
    #         # for i in string3:
    #             # if i in video_list2:
    #                 # for j in string4:
    #                 #     if j in video_list2:
    #     pos1 = result.find(string7)
    #     pos2 = result.find(string8)
    #         # print("oh no")
    #     z = 0
    #     if pos1 == z:
    #         ans = result[pos1+2:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\。\s\-\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #     else : 
    #         ans = result[pos1+1:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #     # print(pos1)
    #     # print(pos2)
    #     # print(ans)
    #     # print(remove)
    #     print("ansmin",ansmin)
    #     return ansmin
    # elif string5 in result:
    #         # for i in string5:
    #     # if string5 in result:
    #                 # for j in string4:
    #                 #     if j in video_list2:
    #     pos1 = result.find(string5)
    #     pos2 = result.find(string6)
    #     # print("oh no")
    #     z = 0
    #     if pos1 == z:
    #         ans = result[pos1+2:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\。\s\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #     else : 
    #         ans = result[pos1+1:pos2]
    #         ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\'\s\。\?]", "", ans)
    #         # if string9 in anstmp :
    #         #     pos3 = anstmp.find(string9)
    #         #     pos4 = anstmp.find(string10)
    #         #     remove = anstmp[pos3:pos4]
    #         #     ansmin = ansmin.replace(remove,"")
    #     # print(pos1)
    #     # print(pos2)
    #     # print(ans)
    #     # print(remove)
       

# def answerinput(ans) :
#     guess = input("請輸入答案: ")
#     if guess == ans :
#         print("bingo")
#     else :
#         answerinput(ans)

# def answertalk(ans) :
#     # next = False
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Please wait. Calibrating microphone...")
#         #listen for 5 seconds and create the ambient noise energy level
#         r.adjust_for_ambient_noise(source, duration=5)
#         print("Say something!")
#         audio=r.listen(source)
        
#         # print(audio)
#         # ans = r.recognize_google(audio, language="zh-TW")
#     # recognize speech using Google Speech Recognition
#     # print()
#     try:
#         ans2 = r.recognize_google(audio, language="zh-TW")
#         print("Google Speech Recognition thinks you said:")
#         print(r.recognize_google(audio, language="zh-TW"))
#         print(ans2)
#         if ans2 == ans:
#         # ("恭喜你對了")
#             print("恭喜你對了")
#             # next = True 
#         else :
#             answertalk(ans)
#         return ans2
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#         answertalk(ans)
#     except sr.RequestError as e:
#         print("No response from Google Speech Recognition service: {0}".format(e))
    # print(ans2)
    #print(ans)
    
# def fight():
    
    

def handle(msg):
    global answer
    # global winer_list
    global group
    global winer
    global url1
    global wantansnum
    global pt
    global group_name
    global game
    global gamenum
    global s
    # updater = Updater('1050112594:AAHu5aEBiIROVw-nFhK5AlNqyGvHqUFTfp4')
    print(msg) 
    chat_id = msg['chat']['id']
    from_id = msg['from']['username']
    # winer_list = []
    # winer = update.message.chat.last_name

    # join - 加入遊戲  
    # start - 遊戲規則  
    # music - 播放歌曲
    # exit - 離開遊戲
    # pass - 跳過此題
    # prompt - 提示
    # replay - 重播
    # rank - 列出排名
    
    # if ('audio' in msg['voice']['mime_type']):
    #     transcribe_voice(bot,msg)
    # else:
    print(playerList)
    # print('ga',gamer)
    if (from_id in playerList):
        if ('/music' in msg['text']):
            # bot.sendMessage(chat_id,'遊戲規則')
            precheck = msg['text'].replace('/music','')
            if precheck == '':
                text2 = '請輸入歌曲範圍,EX:/music 五月天'
                bot.sendMessage(chat_id,text2)
            else :
                group = msg['text']
                # print(music(msg['text']))
                url1,answer = music(msg['text'])
                group_name = msg['text']
                print(url1,answer)
                if (answer != 'None'):
                    paly_music(url1,game)
                # answer = check(url1,result)
                winer = '1'
                wantansnum = 0
                print('987')
        elif ('/start' in msg['text']):
            bot.sendMessage(chat_id,'遊戲規則')
        elif ('/rank' in msg['text']):
            print(playerList)
            s = sorted(playerList.items(), key =lambda x : x[1],reverse=True)
            print(s)
            if (len(playerList) <= 3) :
                p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n'
            else:
                p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n' + '第二名: ' + s[1][0] +' 分數:' + str(s[1][1]) + '第三名: ' + s[2][0] +' 分數:' + str(s[2][1])
            # rankname = playerList[0].keys() #+ playerList[0].values()
            bot.sendMessage(chat_id,p)
        elif ('/exit' in msg['text']):
            playerList.pop(from_id)
        elif ('/prompt' in msg['text']):
            wantansnum = wantansnum + 1
            if (wantansnum >= len(playerList)/2 and len(pass_list) == len(playerList)):
                a = '字數:' + str(len(answer))
                bot.sendMessage(chat_id,a)
                pt = True
                wantansnum = 0
        elif ('/pass' in msg['text'] and pt == True):
            bot.sendMessage(chat_id,answer)
            url1,answer = music(group_name)
            print(url1,answer)
            if (answer != 'None'):
                paly_music(url1,game)
            # answer = check(url1,result)
            winer = '1'
            wantansnum = 0
            # 關卡數加加

        else:
            msgmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?]", "", msg['text'])
            print('msgmin',msgmin)
            print('answer',answer)
            print('group',group)
            print('winer',winer)
            if from_id not in pass_list:
                pass_list.append(from_id)
            if (msgmin == answer and winer == '1'): # and msgmin not in group):
                #if true:#winer_list[0] == '1':
                    # print('winer0',winer)
                print(msg['from']['last_name'])
                winer = msg['from']['last_name']
                # winer_list.append(winer)
                print('winer',winer)
                text = winer + '恭喜你答對了' 
                info = '第' + str(game) + '關，' + '第' + str(gamenum+1) + '題結束'
                bot.sendMessage(chat_id,text)
                bot.sendMessage(chat_id,info)
                y = 0
                y = game + game + game + game + game  
                print('game',y)
                if (pt == True):
                    y = y - game - game
                playerList[from_id] = playerList[from_id] + y
                gamenum = gamenum + 1
                gametmp = gamenum
                print('gamenum',gamenum)
                if (gamenum == 3 and game < 5):
                    print('gamein1',game)
                    gamenum = gamenum - gametmp
                    game = game + 1
                    next = '第' + str(game) + '關開始了'
                    
                    s = sorted(playerList.items(), key =lambda x : x[1],reverse=True)
                    print(s)
                    if (len(playerList) <= 3) :
                        p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n'
                    else:
                        p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n' + '第二名: ' + s[1][0] +' 分數:' + str(s[1][1]) + '第三名: ' + s[2][0] +' 分數:' + str(s[2][1])
                        # rankname = playerList[0].keys() #+ playerList[0].values()
                    bot.sendMessage(chat_id,p)
                    bot.sendMessage(chat_id,next)
                if(gamenum == 3 and game == 5) :
                    print('gamein2',game)
                    tt = 'THE END'
                    bot.sendMessage(chat_id,tt)
                    s = sorted(playerList.items(), key =lambda x : x[1],reverse=True)
                    print(s)
                    if (len(playerList) <= 3) :
                        p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n'
                    else:
                        p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n' + '第二名: ' + s[1][0] +' 分數:' + str(s[1][1]) + '第三名: ' + s[2][0] +' 分數:' + str(s[2][1])
                    # rankname = playerList[0].keys() #+ playerList[0].valu1jes()
                    bot.sendMessage(chat_id,p)
                    bot.sendMessage(chat_id,next)
                else:
                    url1,answer = music(group_name)
                    print(url1,answer)
                    if (answer != 'None'):
                        paly_music(url1,game)
                        print('gamein3',game)

                    # answer = check(url1,result)
                    
                    winer = '1'
                    wantansnum = 0
                    pt = False
            else:
                if ('/replay' in msg['text']):
                    paly_music(url1,game)
                
    elif('/join' in msg['text']):
        i = 0
        playerList[from_id] = i
        print(playerList)

            

    # if :
# if __name__=="__handle__":
#     handle()
        


# def repley(msg):
#     print(msg)    
#     chat_id = msg['chat']['id']
#     text = '恭喜你答對了'
#     txt = msg['text']
#     url1 = music(txt)
    # print('answer',answer)
    
        
        # print(type(ans))
    # print(msg['text'])
    # music(msg['text'])
playerList = {}
pass_list = []
playtime = [60,30,20,10,5]
pt = False

MessageLoop(bot,handle).run_as_thread()
game = 1 # 第幾關
gamenum = 0 # 第幾題
new_set = 0 # 用來算要不要重新輸入歌曲
while 1:
    time.sleep(5)
    

# search_keyword = input("輸入歌曲")
# url1 = music(search_keyword)
# # music(search_keyword)
# # print("a")
# name = check(url1)
# # print("b")
# paly_music(url1)
# # print(type(ans))
# # 輸入答案(語音轉文字)
# answertalk(name)