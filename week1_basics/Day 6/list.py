import random
import time


# for i in range(10):
#     distance = random.randint(1, 20)
#     speed = random.randint(1, 30)
#     battery = random.randint(1, 100)

#     sensor_readings = [distance, speed, battery]

#     print(f"Sensor Readings: {sensor_readings}")

#     time.sleep(1)


commands = ["forward", "backward", "left", "right", "stop"]
for command in commands:
    print(f"Executing command: {command}")
    time.sleep(1)