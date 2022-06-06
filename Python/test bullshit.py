from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.1                     # set pixel brightness
cp.pixels.fill((0, 0, 0))                          # turns all pixels off
cp.pixels.show()   # sends data to pixels

RED = (255, 0, 0),
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
EMPTY = (0, 0, 0)

colors = [RED, GREEN, BLUE, WHITE, YELLOW, EMPTY]

while True:
    if not(cp.button_a or cp.button_b):
        cp.pixels[3] = RED
        cp.pixels[6] = RED


"""def traffic_light():
    for i in range(3, 6, 3):
        cp.pixels[i] = colors"""

"""def red3_6():
    for _ in num_pixels
    pixel_index = int(i + j)
    pixels[i] ="""


"""while True:
num_pixels = 10
    if not(cp.button_a or cp.button_b):
        type(cp.pixels)
        print(type(cp.pixels))
        print(type(cp.temperature))
        print(type(cp.pixels[1]))
        print(type(time.sleep))
        print(type(num_pixels))
        print(type(range))
        print("--------------------------------------------------------------------------")
        time.sleep(5)"""