

robots_name = "SENTRY-01"

def move_forward():
    print(f"{robots_name} Moving Forward")

def turn_left():
    print(f"{robots_name} Turning Left")

def turn_right():
    print(f"{robots_name} Turning Right")

def stop():
    print(f"{robots_name} Stopped")

def check_battery(level):
    if level < 20:
        return False
    return True

def detect_obstacle(is_obstacle):
    return is_obstacle

def execute_patrol(commands, battery_level, obstacle_detected):
    print(f"{robots_name} Patrol Started")
    print(f"Initial Battery Level: {battery_level}%")
    print("-----------------------------------")

    for command in commands:
        if not check_battery(battery_level):
            print("WARNING: Battery Low")
            stop()
            break

        if command == "forward":
            move_forward()
        elif command == "left":
            turn_left()
        elif command == "right":
            turn_right()
        elif command == "stop":
            stop()

battery_level = 60
obstacle_detected = False
commands = ["forward", "left", "forward", "right", "forward"]

execute_patrol(commands, battery_level, obstacle_detected)