import pandas as pd
data_1=pd.DataFrame(columns=['a'])
for i in range(0,25) :
    data_1=data_1.append({'a':i}, ignore_index= True)
print(data_1)
print('-------------')

data_2=pd.DataFrame()
for j in range(0,25):
    if j%5==0:
        data_2=data_2.append({'a':j}, ignore_index= True)
print(data_2)
#if it is start with 0, the second one will go to 5 but not 4
print('-------------')

data_3=pd.DataFrame()
for k in range(0,25):
    data_3=data_3.append({'a':k}, ignore_index= True)
    k=k+4
print(data_3)
print('-------------')
#not success

data_4=pd.DataFrame()
x=0
while x<25:
    data_4=data_4.append({'a':x}, ignore_index= True)
    x=x+4
print(data_4)