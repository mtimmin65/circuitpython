import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")
dot.brightness=0.2
while True:
dot.fill((255,0,0))
time.sleep(.5)
print("Make it red!")
dot.brightness=0.2
dot.fill((0,0,255))
time.sleep(.5)