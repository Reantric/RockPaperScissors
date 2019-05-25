#PLAY THE GAME HERE: https://repl.it/@GoogleAdmin/RockPaperScissors

from random import randint
from time import sleep
from math import factorial 

def sumNum(f):
  nd = {}
  for x in range(f+1):
    nd[f-x] = x
  return nd

print("Credits to Bhuvanesh Prabakar Jr. for the loss percentage calculator. \n")
rps = ['r','p','s']
translate = {'r':'rock','s':'scissors','p':'paper'}
winDic = {'r':'s','s':'p','p':'r'}
cPlay = input('Would you like the computer to play on your behalf? (yes or no) ')
gAmt = input("Please enter how many games you want to play (number) or \"a\" for autoplay ")
def game(gAmt=3,cPlay=True):
  i = 0; a = 0; b = 0; replay = True
  while i < int(gAmt) if gAmt.isdigit() else 199999:
    if gAmt.isdigit():
      nd = sumNum(int(gAmt))
    print('\n')
    moveSelect = rps[randint(0,len(rps)-1)]
    hPlay = input('What is your move? (r,p,s) ') if not cPlay else rps[randint(0,len(rps)-1)]
    sleep(0.2)
    if hPlay == '':
      continue
    try:
      if winDic[hPlay[0].lower()] == moveSelect:
        print(f"Congratulations, you won! The computer played {translate[moveSelect]}")
        a += 1
      elif winDic[moveSelect] == hPlay[0].lower():
        print(f"I am sorry, you played {translate[hPlay[0].lower()]} and the computer played {translate[moveSelect]}")
        b += 1
      else:
        print("It seems you played the same thing as the computer. Nice.")
        i -= 1
      print(f"The game score is: {a}:{b}")
      if gAmt.isdigit():
        for z in range(a):
          del nd[a-1-z]
        for z in range(b):
          del nd[(int(gAmt)-b)+1+z]
        nd = list(nd.items())
        tpos = len(nd)
        try: 
          os = round(100*s/lowerBound,1)
        except:
          os = 50
        s = 0
        lowerBound = 2**(nd[0][0] - a)
        for e in range(len(nd)):
          pA = nd[e][0] - a
          pB = nd[e][1] - b
          if nd[e][1] > nd[e][0]:
            continue
          s += factorial(pA + pB)/(factorial(pA)*factorial(pB))
        print(f"Percent chance of not losing: {round(100*s/lowerBound) if round(100*s/lowerBound,1).is_integer() else round(100*s/lowerBound,1)}% ({'+' + str(round(100*s/lowerBound - os,1)) if round(100*s/lowerBound - os,1) > 0 else round(100*s/lowerBound - os,1)}%)")
        if (100*s/lowerBound == 100 or 100*s/lowerBound == 0) and replay and i != int(gAmt)-1:
          replay = not input("\nWould you like to end this game? ").upper().startswith('Y')
          if not replay:
            return "\n"
    except KeyError or IndexError:
      print("Why don't you try and actually input a correct letter this time.")
      i -= 1
    i += 1
game(gAmt,True if cPlay.upper().startswith('Y') else False)
while input('Would you like to play more games? ').upper().startswith('Y'):
  game(input("Please enter how many games you want to play or \"a\" for autoplay "),input('Would you like the computer to play on your behalf? ').upper().startswith('Y'))
