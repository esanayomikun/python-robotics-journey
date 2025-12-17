# ==============================
# SENTRY-01 PATROL ROBOT SIMULATION
# Week 1 Mini Project
# ==============================

# -------- Robot Actions --------

def move_forward():
    print("SENTRY-01: Moving forward")


def turn_left():
    print("SENTRY-01: Turning left")


def stop():
    print("SENTRY-01: Robot stopped")


# -------- Sensor Simulation --------

def check_battery(battery_level):
    """
    Returns True if battery is sufficient,
    False if battery is low
    """
    if battery_level < 20:
        return False
    return True


def detect_obstacle(obstacle_detected):
    """
    Returns True if obstacle is detected
    """
    return obstacle_detected


# -------- Main Control Logic --------

def execute_patrol(commands, battery_level, obstacle_detected):
    print("SENTRY-01: Patrol started")
    print("Initial battery level:", battery_level, "%")
    print("--------------------------------")

    for command in commands:

        # Safety check: Battery
        if not check_battery(battery_level):
            print("WARNING: Battery low")
            stop()
            break

        # Safety check: Obstacle
        if detect_obstacle(obstacle_detected):
            print("WARNING: Obstacle detected")
            stop()
            break

        # Execute command
        if command == "forward":
            move_forward()
            battery_level -= 10

        elif command == "left":
            turn_left()
            battery_level -= 5

        elif command == "stop":
            stop()
            break

        else:
            print("Unknown command:", command)

        print("Battery remaining:", battery_level, "%")
        print("--------------------------------")

    print("Patrol ended")
    print("Final battery level:", battery_level, "%")


# -------- Program Entry Point --------

battery_level = 50
obstacle_detected = False

patrol_commands = [
    "forward",
    "forward",
    "left",
    "forward",
    "stop"
]

execute_patrol(patrol_commands, battery_level, obstacle_detected)
