import datetime

# Get the current time in EST
import os
import os.path
import sys
import time
import re

from pytz import timezone

##########################################################

def cmdHelp():
  '''Prints all commands'''
  
  print("Commands:")
  print("1. help")
  print("2. time")
  print("3. clear")
  print("4. history")
  print("5. exit")
  print("6. echo")
  print("7. wait")
  print("8. touch")
#end of help
def cmdTime():
  '''current time and date'''
  
  now = datetime.datetime.now(timezone('US/Eastern'))
  print(now.strftime("Date:"+"%B %d, %Y"+" Time:"+" %I:%M %p"+"\n"))
#end of time
def cmdClear():
  '''Clear all text in the console'''
  
  os.system("clear")
#end of clear
def cmdHistory(user):
  '''Prints user history'''
  
  print(user['History'])
#end of history
def cmdExit():
  '''This function exits the program'''
  
  print("See you later!")
  time.sleep(0.5)
  sys.exit()
#end of quit
def cmdEcho(input):
  """Prints the input after typing echo input."""

  print("please type echo input")
  echo = input()
  print(echo)
#end of echo
def cmdWait(input):
  """Wait for a amount of time"""
  
  cmdwaittime = input()
  time.sleep(cmdwaittime)
#end of wait
import os

def cmdTouch():
  """Creates an empty file with the specified name."""
  """Thank you for the help, @Benjamin """
  """I'm sorry for there being no editor yet"""
  
  while True:
      try:
          filename = input("Enter the filename: ")
          filename = re.sub(r'\W+', '', filename) + '.txt'  # Using re's sub method for string sanitization
          with open(filename, 'w'):
              pass
          break
      except FileNotFoundError:
          print("Invalid filename. Please try again.")
      except FileExistsError:
          print("File already exists. Please choose a different filename.")

