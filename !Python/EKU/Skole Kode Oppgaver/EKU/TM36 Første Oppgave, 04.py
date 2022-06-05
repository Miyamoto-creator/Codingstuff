import board
import analogio
import time

digital = analogio.AnalogIn(board.A0)

def greg(digital):
    spenning = digital.value * 3.3 / 65535
    temp = (spenning - 0.5) * 100
    print(f"Digital verdi = {digital.value}")
    print(f"Spennings verdi = {spenning:.2f}V")
    print(f"Temperatur verdi = {temp:.2f}C")
    print("=======================================")

while True:
    greg(digital)
    time.sleep(5)