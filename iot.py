#-----------------check wether the internet is connected-------
import urllib
try :
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except :
    status = "Not connect"
#-------------------if internet connected-----------------------
if(status == "Connected"):
  import telepot
  import time
  def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if(command == "ping"):
        bot.sendMessage(chat_id,"pong")
        print"pong"
    if(command == "hi"):
        bot.sendMessage(chat_id,"hello dude")

  bot = telepot.Bot('321092089:AAGDwCA0tg9e0JZp5TDE7gp_oSkzPFFr3go')
  bot.message_loop(handle)


  while 1:
     time.sleep(10)
else:
  print "No internet Connection Plese try again later"


  