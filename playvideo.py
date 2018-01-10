
#opens youtube and plays a video
#runs after a certain amount of time

import webbrowser
import time

totalBreaks=3
breakCount=0


print('This program began on'+time.ctime())
while(breakcount<totalBreaks):
time.sleep(5)
webbrowser.open('https://www.youtube.com/watch?v=Jta56wBl7SM')
breakCount+=1

