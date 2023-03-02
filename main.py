import time
from pynput.mouse import Button, Controller

print("init controller")
mouse = Controller()

#mouse.move(-100,100)
vari = 0
while vari < 1000:
  time.sleep(0.01)
  mouse.press(Button.left)
  mouse.release(Button.left)

  print(vari)
  vari = vari + 1
  

print("finished")