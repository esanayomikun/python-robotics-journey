# I know about functions before now so i'm just gonna write a simple project

elevator_sensor = input("Is the elevator sensor working? (yes/no): ")

def elevator_status(sensor_working, distance, floor):
    if sensor_working == "yes":
        elevator_sensor_readings = int(input("Enter the distance of the elevator from you (in feet): "))
        while True:
            if elevator_sensor_readings <= 2:
                elevator_doors = "open"
                print("The elevator doors are", elevator_doors)
            else:
                elevator_doors = "closed"
                print("The elevator doors are", elevator_doors)
            if elevator_doors == "open":
                print("You can enter the elevator and select floor")
                floor_number = int(input("Enter the floor number you want to go to (1-10): "))
                if 1 <= floor_number <= 10:
                    print(f"You have selected floor {floor_number}. Enjoy your ride!")
                    break
                else:
                    print("Invalid floor number. Please select a floor between 1 and 10.")
                    
    else:
        print("The elevator sensor is not working. Please contact maintenance.")
        
elevator_status(elevator_sensor, 0, 0)