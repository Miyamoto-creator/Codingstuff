from adafruit_circuitplayground import cp  # impandts the CPX library from its subfolder
import time

cp.pixels.brightness = 0.1  # set pixel brightness
cp.pixels.fill((0, 0, 0))  # turns all pixels off
cp.pixels.show()  # sends data to pixels
num_pixels = 10

GREEN = (0, 255, 0)
EMPTY = (0, 0, 0)

while True :
    for i in range(0, 3, 1) :
        cp.pixels[i] = GREEN
        continue
    for j in range(7, 10, 1) :
        cp.pixels[j] = GREEN
    time.sleep(2)
