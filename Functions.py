import datetime

# Get the current time in EST
import os
import os.path
import sys

from pytz import timezone

##########################################################

def cmdHelp():
  print("1. help")
  print("2. time")
  print("3. clear")
  print("4. history")
  print("5. exit")
  print("6. echo")
#end of help
def cmdTime():
  now = datetime.datetime.now(timezone('US/Eastern'))
  print(now.strftime("Date:"+"%B %d, %Y"+" Time:"+" %I:%M %p"+"\n"))
#end of time
def cmdClear():
  os.system("clear")
#end of clear
def cmdHistory(user):
  print(user['History'])
#end of history
def cmdExit():
  print("See you later!")
  sys.exit()
#end of quit
def cmdEcho(input):
  """Prints the input after typing echo input."""

  print("please type echo input")
  echo = input()
  print(echo)
#end of echo
