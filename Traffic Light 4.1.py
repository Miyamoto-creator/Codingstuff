from adafruit_circuitplayground import cp  # imports the CPX library from its subfolder
cp.pixels.brightness = 0.1                     # set pixel brightness
cp.pixels.fill((0, 0, 0))                          # turns all pixels off
cp.pixels.show()   # sends data to pixels
import time

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
EMPTY = (0, 0, 0)

while True:
    if not(cp.button_a or cp.button_b):
        print("Trafikk lys for biler!")
        cp.pixels[1] = GREEN
        cp.pixels[2] = EMPTY
        cp.pixels[3] = EMPTY
        cp.pixels[6] = RED
        cp.pixels[7] = EMPTY
        cp.pixels[8] = EMPTY
    if cp.button_b:
        print("Button B pressed!")
        continue
    if cp.button_a:
        print("Trafikk lys starter for en gående!")
        cp.pixels[1] = EMPTY
        cp.pixels[2] = YELLOW
        cp.pixels[3 and 6] = RED
        cp.pixels[7 and 8] = EMPTY
        time.sleep(2)
        for x in range(0, 4):
             print(f"Blinke loop har virket {x+1:2} ganger")
             cp.pixels[1:3] = EMPTY *2
             cp.pixels[3] = RED
             cp.pixels[6:8] = EMPTY *2
             cp.pixels[8] = GREEN
             print("Dip (1)")
             cp.play_file("dip.wav")
             time.sleep(0.5)
             cp.pixels[1:3] = EMPTY *2
             cp.pixels[3] = RED
             cp.pixels[6:9] = EMPTY *3
             print("Rise (2)")
             cp.play_file("rise.wav")
             time.sleep(0.5)
        cp.pixels[1] = EMPTY
        cp.pixels[2] = YELLOW
        cp.pixels[3] = RED
        cp.pixels[6] = RED
        cp.pixels[7:9] = EMPTY *2
        time.sleep(1)