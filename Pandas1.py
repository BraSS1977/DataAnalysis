import pandas as pd

df = pd.read_csv('placementdata.csv')

print(df.head())

print(df.info())

print(df.describe(), end='\n\n')

#Работаем с dz.csv
print('Работаем с dz.csv', end='\n\n')
dz = pd.read_csv('dz.csv')
print(dz, end='\n\n')

dz.fillna(0, inplace=True)
print(dz, end='\n\n')

#Определяю среднюю зарплату (Salary) по городу (City)
print('Средняя зарплата по городам составляет:', end='\n')
group = dz.groupby('City')['Salary'].mean()
print(group)
