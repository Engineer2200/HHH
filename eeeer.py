import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

excel_data = pd.read_excel('test.xlsx')

data = pd.DataFrame(excel_data, columns=['name', 'inn', 'debit_date','debit_balance','guarantee'])

print("The content of the file is:\n", data)
print (data.shape)
w = data.iloc[0,3]
e = data.iloc[0,2]
for i in range(data):
    if i > 3 :
        
        w = data.iloc[(0+1),3]
        e = data.iloc[(0+1),2]

# A = ['Проблемная задолженность в сумме', data.iloc[0,3], 'рублей признана безнадежной и списана на внебалансовые счета',data.iloc[0,2] ]
# total_value = [A,'B','C']
# data.insert(loc=len(data.columns), column='total', value=total_value)
# print(data)
# data.to_excel('test.xlsx')