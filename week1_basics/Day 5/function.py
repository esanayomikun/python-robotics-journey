import random
import time

def check_enviroment():
    """Check if the environment is set up correctly."""
    print("Checking environment...")
    time.sleep(2)  # Simulate some checks
    distance = random.randint(1, 10)
    if distance <= 3:
        print("Environment check failed: Obstacle too close!")
        return False
    print("Environment is set up correctly.")
    return True

def moving_forward(steps):
    for _ in range(steps):
        print(f"Moving forward step {_ + 1}")
        time.sleep(1)  # Simulate time taken to move
    print("Reached the destination!")

def perform_task():
    """Perform the main task if the environment is correct."""
    if not check_enviroment():
        print("Task aborted due to environment issues.")
        return
    moving_forward(10)
    
    
check_enviroment()
perform_task()