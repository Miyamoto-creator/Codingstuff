from adafruit_circuitplayground import cp  # impandts the CPX library from its subfolder
import time

cp.pixels.brightness = 0.1  # set pixel brightness
cp.pixels.fill((0, 0, 0))  # turns all pixels off
cp.pixels.show()  # sends data to pixels
num_pixels = 10
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

EMPTY = (0, 0, 0)

num = 0
while True:
    for i in range(0, num_pixels, 1):
        if i % 2 != 0:
            cp.pixels[i] = RED
        else:
            cp.pixels[i] = BLUE
        time.sleep(0.5)
