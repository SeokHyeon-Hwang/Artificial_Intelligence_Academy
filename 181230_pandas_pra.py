import pandas as pd

#01

df = pd.read_csv('C:/Users/campu/Downloads/Do it! 데이터 분석을 위한 판다스 입문 실습 자료/data/gapminder.tsv', sep='\t')

print('#1')
print(df.head())

print('#2')
print(type(df))

print('#3')
print(df.shape)

print('#4')
print(df.columns)

print('#5')
print(df.dtypes)

print('#6')
print(df.info())

#02

print('#7')
country_df = df['country']
print(type(country_df))

print('#8')
print(country_df.head())

print('#9')
print(country_df.tail())

print('#10')
subset = df[['country', 'continent', 'year']]
print(type(subset))

print('#11')
print(subset.head())

print('#12')
print(subset.tail())

#print('#13')
#print(subset)

print('#14')
print(df.head())

print('#15')
print(df.loc[0])

print('#16')
print(df.loc[99])

#print('#17')
#print(df.loc[-1])

print('#18')
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

print('#19')
print(df.tail(n=1))

print('#19-1')
print(df.tail(n=2))

print('#20')
print(df.loc[[0,99,999]])

print('#20-1')
subset_loc = df.loc[0]
subset_tail = df.tail(n=1)

print(type(subset_loc))
print(type(subset_tail))

print('#21')
subset2 = df.loc[:, ['year', 'pop']]
print(subset2.head())

print('#22')
subset3 = df.iloc[:, [2, 4, -1]]
print(subset3.head())

print('#23')
small_range = list(range(5))
print(small_range)

print('#24')
print(type(small_range))

print('#25')
subset4 = df.iloc[:, small_range]
print(subset4.head())

print('#25-1')
print(df.iloc[1])

print('#25-2')
print(df.iloc[99])

print('#25-3')
print(df.iloc[-1])

#print('#25-4')
#print(df.iloc[1710])

print('#26')
small_range2 = list(range(3, 6))
print(small_range2)

print('#27')
subset5 = df.iloc[:, small_range]
print(subset5.head())

print('#28')
small_range3 = list(range(0, 6, 2))
subset = df.iloc[:, small_range3]
print(subset3.head())

print('#29')
subset6 = df.iloc[:, :3]
print(subset6.head())

print('#30')
subset7 = df.iloc[:, 0:6:2]
print(subset7.head())

print('#31')
print(df.iloc[[0,99,999], [0,3,5]])

print('#32')
print(df.loc[[0,99,999], ['country', 'lifeExp', 'gdpPercap']])

print('#33')
print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])

print('#34')
subset8 = df.loc[:, ['year', 'pop']]
print(subset8.head())
