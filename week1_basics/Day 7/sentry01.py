import random
import time

robot_name = "AyoBot"
battery_level = random.randint(0, 100)
is_obstacle_ahead = random.choice([True, False])
is_obstacle_left = random.choice([True, False])
is_obstacle_right = random.choice([True, False])
is_obstacle_back = random.choice([True, False])

def check_battery():
    if battery_level < 20:
        print(f"{robot_name}: Warning! Low battery at {battery_level}%. Please recharge soon.")
        return False
    else:
        print(f"{robot_name}: Battery level is sufficient at {battery_level}%.")
        return True
    
def move_forward():
    print(f"{robot_name} is moving forward.")
    
def turn_left():
    print(f"{robot_name} is turning left.")
    
def turn_right():
    print(f"{robot_name} is turning right.")
    
def turn_back():
    print(f"{robot_name} is turning back.")

def check_obstacles():
    if is_obstacle_ahead:
        print(f"{robot_name}: Obstacle ahead!")
    if is_obstacle_left:
        print(f"{robot_name}: Obstacle to the left!")
    if is_obstacle_right:
        print(f"{robot_name}: Obstacle to the right!")
    if is_obstacle_back:
        print(f"{robot_name}: Obstacle behind!")
        
def navigate():
    if not check_battery():
        return
    
    check_obstacles()
    
    if not is_obstacle_ahead:
        move_forward()
    elif not is_obstacle_left:
        turn_left()
        move_forward()
    elif not is_obstacle_right:
        turn_right()
        move_forward()
    elif not is_obstacle_back:
        turn_back()
        move_forward()
    else:
        print(f"{robot_name}: Surrounded by obstacles! Cannot move.")
        
if __name__ == "__main__":
    print(f"{robot_name} starting navigation sequence...")
    check_battery()
    navigate()
    print(f"{robot_name} navigation sequence complete.")
    
    time.sleep(1)
    print(f"{robot_name} shutting down.")  