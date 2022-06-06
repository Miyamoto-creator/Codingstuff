from adafruit_circuitplayground import cp  # impandts the CPX library from its subfolder
import time
cp.pixels.brightness = 0.1  # set pixel brightness
cp.pixels.fill((0, 0, 0))  # turns all pixels off
cp.pixels.show()  # sends data to pixels
num_pixels = 10

GREEN = (0, 255, 0)

while True:
    for i in range(0, num_pixels, 2):
        cp.pixels[i] = GREEN
        time.sleep(0.5)
    cp.pixels.fill(EMPTY)
    time.sleep(2)
