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
bot = telepot.Bot('YOUR BOT API TOKEN')
# 抓歌曲 

def music(search_keyword) :
    video_tmp = []
    # time.time() = 0
    a = quote(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + a)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for i in range(len(video_ids)):
        if video_ids[i] not in video_tmp:
            video_tmp.append(video_ids[i])
    
    video_ids_random = random.sample(video_tmp, len(video_tmp))
    # print('random',video_ids_random)
    print('ids',len(video_ids))
    print('tmp',len(video_tmp))
    num = random.randint(0,len(video_ids_random)-1)
    print('num',num)
    url = "https://www.youtube.com/watch?v=" + video_ids_random[num] + "#t=1m23s"
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
    else:
        donename = check(url,result)
        donename2 = str(donename)
        print('donename',donename2)
        result_no_eng = re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?\(\)\》\《\！]", "", donename2)
        if result_no_eng == '':
            music(search_keyword)
        # if donename.isalpha() == True:
        #     music(search_keyword)
        # print("id",video_ids[num])
        print('url1',url)
        print("https://www.youtube.com/watch?v=" + video_ids_random[num])
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
        ansmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?\(\)\》\《\！]", "", ans)
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
    global pass_list
    # updater = Updater('1050112594:AAHu5aEBiIROVw-nFhK5AlNqyGvHqUFTfp4')
    print(msg) 
    chat_id = msg['chat']['id']
    from_id = msg['from']['username']
    # winer_list = []
    # winer = update.message.chat.last_name

    # join - 加入遊戲  
    # rule - 遊戲規則  
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
    # if msg['chat']['id'] == '-466887320' :
    if (from_id in playerList):
        if ('/music' in msg['text']):
            print('msgtext',msg['text'])
            # bot.sendMessage(chat_id,'遊戲規則')
            precheck = msg['text'].replace('/music','')
            print('precheck',precheck)
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
        elif ('/rule' in msg['text']):
            r = '遊戲規則:\n1. 輸入 /music 加上歌手名稱以選擇範圍，共有五關，每關三題\n2. 每關分數依題目難度而有增減\n3. 若題目太難，可使用 /prompt 提示，但使用提示會導致分數下降！請務必謹慎使用！\n4. 如果等的有點久，可以重新下一次指令(/music + 歌手名)'
            bot.sendMessage(chat_id,r)
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
            infoans = 'the answer is :' + answer
            bot.sendMessage(chat_id,infoans)
            # bot.sendMessage(chat_id,answer)
            bot.sendMessage(chat_id,url1)
            info = '第' + str(game) + '關，' + '第' + str(gamenum+1) + '題結束'
            bot.sendMessage(chat_id,info)
            # print('groupname',group_name)
            # url1,answer = music(group_name)
            # print(url1,answer)
            # if (answer != 'None'):
            #     paly_music(url1,game)
            # answer = check(url1,result)
            gamenum = gamenum + 1
            gametmp = gamenum
            pass_list = []
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
                p = ''
                for i in range(len(playerList)):
                    ranknum = i + 1

                    p = '第' + str(ranknum) + '名: ' + s[i][0] +' 分數:' + str(s[i][1])

                    # p = str(p)
                    bot.sendMessage(chat_id,p)
                    print('pppppppp',p)
                # rankname = playerList[0].keys() #+ playerList[0].valu1jes()
                # bot.sendMessage(chat_id,p)
                # bot.sendMessage(chat_id,next)
            else:
                winer = '1'
                wantansnum = 0
                pt = False
                print('gn',group_name)
                url1,answer = music(group_name)
                print(url1,answer)
                if (answer != 'None'):
                    paly_music(url1,game)
                    print('gamein3',game)

                # answer = check(url1,result)

            
            


        else:
            print('HERERERERRE~~~~~~')
            msgmin =  re.sub("[A-Za-z0-9\!\%\[\]\,\。\s\'\-\?]", "", msg['text'])
            print('msgmin',msgmin)
            print('answer',answer)
            print('group',group)
            print('winer',winer)
            if from_id not in pass_list:
                if '/' not in msg['text'] :
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
                pass_list = []
                y = 0
                y = game + game + game + game + game  
                print('game',y)
                if (pt == True): # 使用提示之後進行一個扣分的動作
                    y = y - game - game # 扣分的動作
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
                    p = ''
                    for i in range(len(playerList)):
                        ranknum = i + 1

                        p = '第' + str(ranknum) + '名: ' + s[i][0] +' 分數:' + str(s[i][1])

                        # p = str(p)
                        bot.sendMessage(chat_id,p)
                        print('pppppppp',p)
                    # if (len(playerList) <= 3) :
                    #     p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n'
                    # else:
                    #     p = '第一名: ' + s[0][0] +' 分數:' + str(s[0][1]) +'\n' + '第二名: ' + s[1][0] +' 分數:' + str(s[1][1]) + '第三名: ' + s[2][0] +' 分數:' + str(s[2][1])
                    # rankname = playerList[0].keys() #+ playerList[0].valu1jes()
                    # bot.sendMessage(chat_id,p)
                    # bot.sendMessage(chat_id,next)
                else:
                    url1,answer = music(group_name)
                    winer = '1'
                    wantansnum = 0
                    pt = False
                    print(url1,answer)
                    
                    if (answer != 'None'):
                        paly_music(url1,game)
                        print('gamein3',game)

                    # answer = check(url1,result)
                    
                    
            else:
                if ('/replay' in msg['text']):
                    paly_music(url1,game)
                
    elif('/join' in msg['text']):
        # chat_id = msg['chat']['id']
        # if msg['chat']['id'] ==  :
        if len(playerList) == 0:
            chat_id = msg['chat']['id']
            i = 0
            playerList[from_id] = i
            print(playerList)
        else :
            if chat_id == msg['chat']['id'] :
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
playtime = [60,40,30,20,10]
pt = False # 有沒有公布提示

MessageLoop(bot,handle).run_as_thread()
game = 5 # 第幾關
gamenum = 2 # 第幾題
# new_set = 0 # 用來算要不要重新輸入歌曲
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
