"""Lift status"""

import time as ts
import pandas as pd

florrs = [1,2,3,4]
lift_position = 2
max_floors = 4





# print(f'The lift is in {lift_position}')

arr =[]



# nandubatchu
# print(arr)

checked = False
user_floor = []
current_floor_no = 0

def check_user(checked):
    user_floor = pd.read_excel('test.xlsx')['user_floor'][0]
    if user_floor != current_floor_no:
        checked = False
    if not checked:
        if user_floor != 'Nan':
            print(f'user has pressed {user_floor}...going in 2 seconds')
            ts.sleep(2)
            df = pd.read_excel('test.xlsx')
            df['lift_state'] = user_floor
            df.to_excel('test.xlsx',index=False)
            checked = True
    return checked 

    
while True:
    checked = check_user(checked)
    current_floor_no = pd.read_excel('test.xlsx')['lift_state'][0]
    print(current_floor_no,'check')
    print(f'Currently the lift is in {current_floor_no} floor')
    for row in range(0,1):
        a = []
        for col in range(4,0,-1):
            if col == current_floor_no:
                a.append('L1')
            else:
                a.append(0)
        arr.append(a)
    for col in arr[0]:
        print(col,end=' ')
        print()
    ts.sleep(5)
    arr.clear()






    





