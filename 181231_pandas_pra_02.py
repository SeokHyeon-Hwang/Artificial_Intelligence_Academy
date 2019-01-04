import pandas as pd

df = pd.read_csv('C:/Users/campu/Downloads/Do it! 데이터 분석을 위한 판다스 입문 실습 자료/data/gapminder.tsv', sep='\t')

print('#01')
subset = df.loc[:, ['year', 'pop']]
print(subset.head())

print('#02')
subset2 = df.iloc[:, [2, 4, -1]]
print(subset2.head())

print('#03')
small_range = list(range(5))
print(small_range)

print('#04')
print(type(small_range))

print('#05')
small_range2 = list(range(3,6))
print(small_range2)

print('#06')
subset3 = df.iloc[:, small_range]
print(subset3.head())

print('#07')
small_range3 = list(range(0, 6, 2))
subset4= df.iloc[:, small_range3]
print(subset4.head())

print('#08')
subset5 = df.iloc[:, :3]
print(subset5.head())

print('#09')
print(df.iloc[[0, 99, 999], [0, 3, 5]])

print('#10')
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

print('#11')
print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])

print('#12')
print(df.groupby('year')['lifeExp'].mean())

print('#13')
grouped_year_df = df.groupby('year')
print(type(grouped_year_df))

print('#14')
print(grouped_year_df)

print('#15')
grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))

print('#16')
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

print('#17')
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

print('#18')
print(type(multi_group_var))

print('#19')
print(df.groupby('continent')['country'].nunique())

import matplotlib.pyplot as plt
print('#20')
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

print('#21')
global_yearly_life_expectancy.plot()
plt.show()
