
#opens youtube and plays a video
#runs after a certain amount of time
#I choose how long it waits between each running of the video

import webbrowser
import time

totalBreaks=3
breakCount=0

#loop here and run this as many times as I indicated in totalBreaks
print('This program began on '+time.ctime())
while(breakCount<totalBreaks):
    time.sleep(5)   #the number waiting between runs in seconds
    webbrowser.open('https://www.youtube.com/watch?v=Jta56wBl7SM')
    breakCount+=1

    