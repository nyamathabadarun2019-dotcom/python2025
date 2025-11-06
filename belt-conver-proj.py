import os 
import time

rooms = 6
requests = [1,2,3,4,5]
current_room = 0


def convenyor_belt(requests):
    # current = 5 - request
    # print('📦 belt stopped')
    for room in range(rooms):
        if room == request:
            print(f'   | 📦   |')
        else:
            print(f'   |    |')


#main code
print('starting convenyor_belt')

for request in requests:
    print(f'Moving to room: {request}')
    time.sleep(2)
    convenyor_belt(requests) 