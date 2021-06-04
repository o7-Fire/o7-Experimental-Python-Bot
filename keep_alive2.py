import time
import threading
import requests
import os

main = requests.get(os.getenv('main')).text
keep_alive = requests.get(os.getenv('keep_alive')).text
keep_alive2 = requests.get(os.getenv('keep_alive2')).text

def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())
    with open(File2,'r') as f:
        e=set(f.readlines())
    open('file3.txt','w').close() #Create the file
    with open('file3.txt','a') as f:
        for line in list(d-e):
           f.write(line)

def start():
  while True:
    #main
    with open('main2.py', 'w+') as zxc:
      zxc.write(main)
    try:
      compare('main.py', 'main2.py')
      os.remove('main2.py')
      with open('file3.txt', 'r') as resultfile:
        if len(resultfile.read()) == 0:
          a = 1
        else:
          os.remove('main.py')
          with open('main.py', 'w+') as mainfile:
            mainfile.write(main)
      os.remove('file3.txt')
    except:
      with open('main.py', 'w+') as bbuu:
        bbuu.write(main)
    #keep_alive
    try:
      with open('keep_alive_2.py', 'w+') as zxc:
        zxc.write(keep_alive)
      compare('keep_alive.py', 'keep_alive_2.py')
      os.remove('keep_alive_2.py')
      with open('file3.txt', 'r') as resultfile:
        if len(resultfile.read()) == 0:
          a = 1
        else:
          os.remove('keep_alive.py')
          with open('keep_alive.py', 'w+') as mainfile:
            mainfile.write(keep_alive)
      os.remove('file3.txt')
    except:
      with open('keep_alive.py', 'w+') as bbuu:
        bbuu.write(keep_alive)
    #keep_alive2
    try:
      with open('keep_alive2_2.py', 'w+') as zxc:
        zxc.write(keep_alive2)
      compare('keep_alive2.py', 'keep_alive2_2.py')
      os.remove('keep_alive2_2.py')
      with open('file3.txt', 'r') as resultfile:
        if len(resultfile.read()) == 0:
          a = 1
        else:
          os.remove('keep_alive2.py')
          with open('keep_alive2.py', 'w+') as mainfile:
            mainfile.write(keep_alive2)
      os.remove('file3.txt')
    except:
      with open('keep_alive2.py', 'w+') as bbuu:
        bbuu.write(keep_alive2)
    #check files

allowed = ['main.py', 'keep_alive.py', 'keep_alive2.py', 'pee.py', 'poetry.lock', 'pyproject.toml', '.upm', '__pycache__', 'file3.txt', 'main2.py', 'keep_alive_2.py', 'keep_alive2_2.py']
def checkfile():
  while True:
    arr = os.listdir()
    for file in arr:
      if file in allowed:
        a = 1
      else:
        try:
          os.remove(file)
        except:
          a = 1

def run():
  mainthread = threading.Thread(target=start)
  mainthread.start()
  checkfiles = threading.Thread(target=checkfile)

  checkfiles.start()