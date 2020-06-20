def intro():
  import time as sec; import os
  print('Welcome to...')
  sec.sleep(1)
  os.system('clear')
  print('S')
  sec.sleep(.1)
  print('u')
  sec.sleep(.1)
  print('p')
  sec.sleep(.1)
  print('e')
  sec.sleep(.1)
  print('r')
  sec.sleep(.1)
  print('T')
  sec.sleep(.1)
  print('u')
  sec.sleep(.1)
  print('r')
  sec.sleep(.1)
  print('t')
  sec.sleep(.1)
  print('l')
  sec.sleep(.1)
  print('e')
  sec.sleep(.1)
  print('R')
  sec.sleep(.1)
  print('u')
  sec.sleep(.1)
  print('s')
  sec.sleep(.1)
  print('h')
  sec.sleep(2)
  os.system('clear')
def makeprmpt():
  import turtle, os, time
  t = turtle.Pen()
  os.system('clear')
  print('To go forward, type "q". If you want to go backwards, type "a". And for left or right type "l" or "r"')
  time.sleep(2)
  t.penup()
  print('\n')
  usrname = input('SuperTurtleRush 1.0 Login\nUsername: ')
  passwrd = input('Password: ')
  oof1 = len(passwrd)
  oof = '*'*oof1
  if usrname == 'SuperTurtleRush-DEV' and passwrd == 'myDevPowr':
    while True:
      prmpt = input('DEVPRMPT: ')
      if prmpt == 'q':
        t.forward(10)
        print('exec.forward;')
      if prmpt == 'a':
        t.back(10)
        print('exec.backward;')
      if prmpt == 'l':
        t.left(45)
        print('exec.left;')
      if prmpt == 'r':
        t.right(45)
        print('exec.right;')
  while True:
    prmpt = input('USER: %s, PASS: %s | PRMPT: ' % (usrname, oof))
    if prmpt == 'q':
      t.forward(10)
    if prmpt == 'a':
      t.back(10)
    if prmpt == 'l':
      t.left(45)
    if prmpt == 'r':
      t.right(45)
def _main_():
  intro()
  makeprmpt()
_main_()