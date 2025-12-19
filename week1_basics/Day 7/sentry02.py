import time
import random

GRID_SIZE = 5

# Battery settings
battery = 100
BATTERY_DRAIN = 10
LOW_BATTERY_THRESHOLD = 30

# Create grid
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Home position
home_x, home_y = 4, 4
grid[home_x][home_y] = "H"

# Robot starting position
robot_x, robot_y = 2, 2
grid[robot_x][robot_y] = "R"

# Place initial obstacles
for _ in range(4):
    x, y = random.randint(0, 4), random.randint(0, 4)
    if grid[x][y] == ".":
        grid[x][y] = "#"

state = "EXPLORE"

def print_grid():
    for row in grid:
        print(" ".join(row))
    print(f"Battery: {battery}% | State: {state}")
    print("-" * 25)

def is_valid_move(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] != "#"

def add_random_obstacle():
    x, y = random.randint(0, 4), random.randint(0, 4)
    if grid[x][y] == ".":
        grid[x][y] = "#"

def move_robot(new_x, new_y):
    global robot_x, robot_y, battery
    if is_valid_move(new_x, new_y):
        grid[robot_x][robot_y] = "."
        robot_x, robot_y = new_x, new_y
        grid[robot_x][robot_y] = "R"
        battery -= BATTERY_DRAIN
        return True
    return False

def move_towards_home():
    global robot_x, robot_y

    if robot_x < home_x:
        return move_robot(robot_x + 1, robot_y)
    if robot_x > home_x:
        return move_robot(robot_x - 1, robot_y)
    if robot_y < home_y:
        return move_robot(robot_x, robot_y + 1)
    if robot_y > home_y:
        return move_robot(robot_x, robot_y - 1)

    return False


print("AyoBot starting autonomous patrol...\n")
print_grid()

while state != "SHUTDOWN":

    # Switch to return-home mode
    if battery <= LOW_BATTERY_THRESHOLD and state == "EXPLORE":
        print("Low battery detected! Returning home...")
        state = "RETURN_HOME"

    if state == "EXPLORE":
        if random.random() < 0.3:
            add_random_obstacle()

        moved = False
        for dx, dy in [(-1, 0), (0, -1), (0, 1)]:
            if move_robot(robot_x + dx, robot_y + dy):
                moved = True
                break

        if not moved:
            print("Blocked while exploring.")
            battery -= 5

    elif state == "RETURN_HOME":
        if (robot_x, robot_y) == (home_x, home_y):
            print("AyoBot reached home. Ready to recharge.")
            state = "SHUTDOWN"
        else:
            if not move_towards_home():
                print("Path blocked while returning home.")
                battery -= 5

    print_grid()
    time.sleep(1)

print("AyoBot safely shut down.")
