from turtle import *
try:
    color('red', 'yellow')
    begin_fill()
    while True:
      forward(200)
      left(170)
      if abs(pos()) < 1:
          break
    end_fill()
    done()
except:
    print("No monitor Found!")
