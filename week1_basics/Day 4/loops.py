# cycles = 10

# for cycle in range(cycles):
#     print("No of cycles:", cycle + 1)

import random
import time

battery = random.randint(0, 100)

while True:
    if battery > 20 and battery <= 100:
        print("Battery is okay")
    else:
        print("Low battery! recharge")
        break
    time.sleep(1)
