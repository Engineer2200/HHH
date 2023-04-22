import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

excel_data = pd.read_excel('test.xlsx')

data = pd.DataFrame(excel_data, columns=['name', 'inn', 'debit_date','debit_balance','guarantee','total'])

print("The content of the file is:\n", data)

h = data.count()[0]
n = 0
for i in range(h):
    if data.iloc[n,4] == 1.0:
        data.at [n, 'total'] = 'Что-то здесь ' + str(data.iloc[n,3] ) + 'и что-то здесь' + str(data.iloc[n,2] ) + 'и вроде тута шото.' 
        n += 1
    else:
        data.at [n, 'total'] = 'Проблемная задолженность в сумме ' + str(data.iloc[n,3] ) + 'рублей признана безнадежной и списана на внебалансовые счета ' + str(data.iloc[n,2] )
        n += 1

print(data)
data.to_excel('test.xlsx')