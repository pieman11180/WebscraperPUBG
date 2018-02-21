# Grabing modules needed for project
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
from gtts import gTTS
import os
from playsound import playsound




#Functions

def Speak (s,val):
    my_tts = s
    tts = gTTS(text=my_tts, lang='en')
    tts.save('voice'+ val + '.mp3')
    playsound('voice'+ val + '.mp3')
    os.remove('voice'+ val + '.mp3')
    


#Grabing data
my_url = "https://pubg.op.gg/leaderboard"
uClient = uReq(my_url)
page_html = uClient.read()
# html Parsing



#Voice testing
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("li",{"leader-board-top3__item"})
count = 1
Speak("The Top PUBG players in N A are","")
for container in containers:
    p_name = container.find("a",{"leader-board-top3__nickname"})
    P_rating = container.find("span",{"leader-board-top3__rating-value"})
    p_game = container.find("span",{"leader-board-top3__matches-cnt-value"})
    line = p_name.contents[0] + " with a rating of " + P_rating.contents[0] + " and " +  p_game.contents[0] + " games"
    
    print line
    Speak(line,str(count))
    print "Name: " + p_name.contents[0]
    print "Rating: " +  P_rating.contents[0]
    print "Number of games: " + p_game.contents[0]
    print "\n"
    count = count+1

#p1 = containers[0]
#p1_name = p1.div
#print p1_name.a.contents[0]



#Closeing connection
uClient.close()
#Printing
