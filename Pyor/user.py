import pandas as pd
import openpyxl


user_floor = int(input('Enter the floor you are now\n'))


df = pd.read_excel('test.xlsx')

df['user_floor'] = user_floor

df.to_excel('test.xlsx',index=False)




