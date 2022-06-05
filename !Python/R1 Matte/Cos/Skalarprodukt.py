import math
import numpy as np


a = 3
b = 2
while True:
    ans = int(input("Choose angle value: "))
    print(round(a * b * np.cos(math.radians(ans))))