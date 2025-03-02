import pandas as pd
temperature = []
conductivity = []
depth = []
path = r'H:\2021.8.25-8.28深蓝一号海试\204485_20210830_104214hour\204485_20210830_104214hour_data.txt'
data = pd.read_csv(path,header=None)

for i in data.index:
    if i%9000==0:
        temperature.append(data[i+1][2])
        conductivity.append(data[i+1][1])
        depth.append(data[i+1][5])
# for i in data.index:
#     print(i)
# df = pd.DataFrame(data)

# for i in range(0,len(df),20):##每隔20行取数据
#     a.append(i)
# file = df.iloc[a]
# f = pd.DataFrame(file)
# f.to_csv(r'E:\**\*****.csv', index=False,encoding='utf_8_sig')
print(temperature)
print('ok')
