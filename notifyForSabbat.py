import datetime
import time
import requests
from playsound import playsound
#-----------start--------------
while 'true':
    now = datetime.datetime.now()
    timeNow=now.strftime("%H:%M:%S").split(':')[0]
    day=now.strftime("%Y-%m-%d %H:%M:%S").split('-')[2].split(' ')[0]
    month=now.strftime("%Y-%m-%d %H:%M:%S").split('-')[1].split(' ')[0]
    year=now.strftime("%Y-%m-%d %H:%M:%S").split('-')[0].split(' ')[0]
    publicDate=str(year+'-'+str(month)+'-'+str(day))
    #-------------api requests-------------
    responseForParash=requests.get('https://www.hebcal.com/shabbat/?cfg=json&geonameid=281184&m=42&a=on').json()
    #-------------respones-----------------
    date=responseForParash['items'][1]['date']
    parashat=responseForParash['items'][1]['hebrew']
    publicTime=responseForParash['items'][0]['title'].split(': ')[1]
    hour=int(responseForParash['items'][0]['title'].split(': ')[1].split(':')[0])+11
    #-------------play music for shabat----
    if publicDate==date and timeNow==hour :
        playsound('binyamin.mp3')
        time.sleep(300)

