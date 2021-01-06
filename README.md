# 猜歌遊戲 in LSA

[![hackmd-github-sync-badge](https://hackmd.io/ktRec9XuQniTA3w9MsG5xw/badge)](https://hackmd.io/ktRec9XuQniTA3w9MsG5xw)

## 動機發想
就因為喜歡玩猜歌遊戲，可是每次都要有一個人出題，所以乾脆讓樹梅派來幫我們出題好了

## 所需設備
- 安裝好作業系統的 Raspbarry Pi 3 or 4
- USB to TTL
- 一台能動的電腦
- 音響


## 事前準備
1. [Download Python](https://www.python.org/downloads/)
2. 確認你的`python`及`pip`有成功安裝
```shell=
python --version
# 版本須為3.x.x
pip --version
# 須為 from python3.x.x
```

3. 安裝
```shell=
pip install telepot
pip install re2
pip install vlc
pip install python-vlc
pip install pafy
pip install youtube-dl
pip install urllib
pip install python3-urllib
# 窗戶作業系統需要另外在網路上搜尋 vlc 下載
# 若電腦內同時有 python2 及 python3
# 上述所有 pip 都要改成 pip3
```

4. 安裝 Telegram Bot
    - 加 @BotFather 為好友
    - `/newbot`為你的機器人取個名字
    - 記住`TOKEN`，然後就可以開始你的 Telegram Bot了
    ![](https://i.imgur.com/sXXNTTh.jpg )



## 遊戲玩法
### 遊戲流程
![](https://i.imgur.com/GO0LXcU.png)

### 群組玩法
1. 將 telegram bot 加入群組

![](https://i.imgur.com/uh6nNzX.jpg )

![](https://i.imgur.com/2eSRi4d.jpg )

2. 成員選擇`/join`加入遊戲
3. optional 選擇`/rule`顯示遊戲規則
4. 輸入 `/music` + **歌手名** 並開始遊戲
5. 遊戲共有 5 關，每關 3 題，並依據關卡難度提高得分
6. 若該題無人回答正確，且所有人都回答過至少一次的情況下，超過半數人選擇`/prompt`，則可使用提示，**但使用提示會降低得分**(請參照下表)
7. 若使用提示後依舊無法答對，可`/pass`此題，並公布正確答案(答案錯了就是你衰到)
8. 每關結束，列出得分**前三高**的分數及 telegram ID
9. 遊戲結束，列出所有人的得分及 telegram ID
- optional
    - `/replay` 重播題目
    - `/rank` 列出前三名
    - `/exit` 離開遊戲

|關卡| 1| 2| 3| 4|5|
| -------- | -------- | -------- |--------|---------|-------|
| 關卡秒數 | 60 | 40 |   30 |  20 | 10|
| 關卡得分  | 5 | 10 |  15|   20|  25|
| 使用提示後的得分 |  3 |  6 |  9| 12 |15| 

### 個人玩法
1. 加 @Bingtrybot 好友
2. `/join` 加入遊戲
3. optional `/rule` 顯示遊戲規則
4. `/music 歌手` 設定遊戲範圍並開始遊戲
5. 遊戲共有 5 關，每關 3 題，並依據關卡難度提高得分
6. 若題目太難無法答對，且回答過至少一次，可使用`/prompt`顯示提示，**但使用提示會降低得分**
7. 若使用提示後依舊無法答對，可`/pass`此題，並顯示正確答案(答案錯了就算你衰到)
8. 遊戲結束，列出得分
- optional
    - `/replay` 重播題目
    - `/rank` 列出排名 a.k.a. 查看你的得分
    - `/exit` 離開遊戲

|關卡| 1| 2| 3| 4|5|
| -------- | -------- | -------- |--------|---------|-------|
| 關卡秒數 | 60 | 40 |   30 |  20 | 10|
| 關卡得分  | 5 | 10 |  15|   20|  25|
| 使用提示後的得分 |  3 |  6 |  9| 12 |15|

## 遊戲控制
- `/join` 加入遊戲
- `/rule` 顯示遊戲規則
- `/music 歌手` 設定遊戲範圍
- `/replay` 重新播放題目
- `/exit` 離開遊戲
- `/pass` 跳過此題
- `/prompt` 顯示提示
- `/rank` 列出排名前三高

## 困難 & 克服
- youtube 惱人的廣告
    - 換另一種方式就沒這個問題了
- VLC 安裝
    - 除了 `pip install vlc` 之外，還要`pip install python-vlc`
    - 窗戶還要下載 VLC 才可以正常執行


## 未來展望
- 希望歌曲語種可以更多元，涵蓋英文、日文等其他語言的歌
- 增加關卡變化ex: 變速
- 提高歌曲名稱準確率

## 參考資料
- https://hackmd.io/@truckski/HkgaMUc24?type=view
- https://blog.sean.taipei/2017/05/telegram-bot
- https://letswrite.tw/telegram-bot-commands/
- https://oscarada87.github.io/2019/05/25/%E7%94%A8-Python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84-Telegram-Bot/
- https://github.com/NCNU-OpenSource/MOLi-PA-Bot/blob/master/PABot.py

## 工作分配
- 葉衣玲
    - 投影片製作
- 程芮瑄
    - Telegram Bot 功能製作
- 詹佳穎
    - Telegram Bot 功能製作
- 陳又瑀
    - 文件製作 樹梅派操作

## 特別感謝愛心TA漢偉
