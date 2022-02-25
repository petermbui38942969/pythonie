#winning number
import random
wn=random.randint
(0-100)
winning_number=100
number=int(input("Guess a number:"))
if number==winning_number:
  print("CONGRATULATIONS YOU WON!!!")
else:
  print("YOU DIDN'T MATCH")
  if number>winning_number:
    print("TOO HIGH")
  else:
    print("TOO LOW")
    if number>=99 and number<=100:
      print("YOU WERE CLOSE TO WINNING!!!")
    else:
      print("TRY AGAIN!!!")