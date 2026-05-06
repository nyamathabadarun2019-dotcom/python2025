import os
import time

floors = 6
requests = input("enter the value")
current_floor = 0

def draw_lift(requests):
    current = 5 - requests
    print('🏢 LIFT SIMULATION')
    for floor in range(floors):
        if floor == current: #3, 3
            print(f"   🟫 | 🚇 |") #lift body
        else:
            print(f"   🟦 |    |") #floor wihtout lift


#MAIN LOGIC
print('Starting lift simulation..\n')


for request in requests:
    print(f'Moving to floor: {requests}')
    time.sleep(2)
    draw_lift(int(requests))


            