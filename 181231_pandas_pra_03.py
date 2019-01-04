import pandas as pd

print('#01')
s = pd.Series(['banana', 42])
print(s)

print('#02')
s2 = pd.Series(['Wes McKinney', 'Creator of Pandas'])
print(s2)

print('#03')
s3 = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s3)

print('#04')
scientists = pd.DataFrame({
    'Name' : ['Rosaline Franklin', 'William Gosset'],
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Age' : [37, 61]})
print(scientists)

print('#05')
scientists2 = pd.DataFrame(
    data = {'Occupation' : ['Chemist', 'Statistician'],
            'Born' : ['1920-07-25', '1876-06-13'],
            'Died' : ['1958-04-16', '1937-10-16'],
            'Age' : [37, 61]},
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Age', 'Died'])
print(scientists2)

from collections import OrderedDict

print('#06')
scientists3 = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37, 61])
])
)

print(scientists3)

print('#07')
scientists4 = pd.DataFrame(
    data = {'Occupation' : ['Chemist', 'Statistcian'],
            'Born' : ['1920-07-25', '1876-06-13'],
            'Died' : ['1958-04-16', '1937-10-16'],
            'Age' : [37, 61]},
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Died', 'Age'])

first_row = scientists4.loc['William Gosset']
print(type(first_row))

print('#08')
print(first_row)

print('#09')
print(first_row.index)

print('#10')
print(first_row.values)

print('#11')
print(first_row.keys())

print('#12')
print(first_row.index[0])

print('#13')
print(first_row.keys()[0])

print('#14')
ages = scientists4['Age']
print(ages)

print('#15')
print(ages.mean())

print('#16')
print(ages.min())

print('#17')
print(ages.max())

print('#18')
print(ages.std())

print('#19')
scientists5 = pd.read_csv('C:/Users/campu/Downloads/Do it! 데이터 분석을 위한 판다스 입문 실습 자료/data/scientists.csv')
ages2 = scientists5['Age']
print(ages2.max())

print('#20')
print(ages2.mean())

print('#21')
print(ages2[ages2 > ages2.mean()])

print('#22')
print(ages2 > ages2.mean())

print('#23')
manual_bool_values = [True, True, False, False,True, True, False, True]
print(ages2[manual_bool_values])

print('#24')
print(ages2 + ages2)

print('#25')
print(ages2 * ages2)

print('#26')
print(ages2 + 100)

print('#27')
print(pd.Series([1, 100]))

print('#28')
print(ages2 + pd.Series([1, 100]))

print('#29')
rev_ages = ages2.sort_index(ascending = False)
print(rev_ages)

print('#30')
print(ages2 *2)

print('#31')
print(ages2 + rev_ages)

print('#32')
print(scientists5['Age'] > scientists5['Age'].mean())

print('#33')
print(scientists5[scientists5['Age'] > scientists5['Age'].mean()])

print('#34')
print(scientists5.loc[[True, True, False, True]])

print('#35')
print(scientists*2)

print('#36')
print(scientists5['Born'].dtype)
print(scientists5['Died'].dtype)

print('#37')
born_datetime = pd.to_datetime(scientists5['Born'], format='%Y-%m-%d')
print(born_datetime)

print('#38')
died_datetime = pd.to_datetime(scientists5['Died'], format = '%Y-%m-%d')
print(died_datetime)

print('#39')
scientists5['born_dt'], scientists5['died_dt'] = (born_datetime, died_datetime)
print(scientists5.head())

print('#40')
print(scientists5.shape)

print('#41')
scientists5['age_days_dt'] = (scientists5['died_dt'] - \
                              scientists5['born_dt'])
print(scientists5)

print('#42')
print(scientists5['Age'])

import random

print('#43')
random.seed(42)
random.shuffle(scientists5['Age'])
print(scientists5['Age'])

print('#44')
print(scientists5.columns)

print('#45')
scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns)

print('#46')
names = scientists5['Name']

print('#47')
names.to_pickle('C:/Users/campu/Downloads/scientists5_names_series.pickle')

print('#48')
scientists5.to_pickle('C:/Users/campu/Downloads/scientists5_names_series.pickle')

print('#49')
scientists5_names_from_pickle = pd.read_pickle('C:/Users/campu/Downloads/scientists5_names_series.pickle')
print(scientists5_names_from_pickle)

print('#50')
names.to_csv('C:/Users/campu/Downloads/scientists5_names_series.csv')

print('#51')
scientists5.to_csv('C:/Users/campu/Downloads/scientists5_df.tsv', sep='\t')

print('#52')
scientists5.to_csv('C:/Users/campu/Downloads/scientists5_df_no_index.csv', index=False)

print('#53')
names_df = names.to_frame()
print(names_df)

print('#54')
import xlwt
names_df.to_excel('C:/Users/campu/Downloads/scientsts5_names_series_df.xls')

print('#55')
import openpyxl
names_df.to_excel('C:/Users/campu/Downloads/scientists5_names_series_df.xlsx')
