import pandas as pd
from datetime import datetime

df_autumn = pd.read_csv('autumn.csv', sep=';')
df_spring = pd.read_csv('spring.csv', sep=';')

df_autumn['Семестр'] = 'Осень'
df_spring['Семестр'] = 'Весна'

df_summary = pd.concat([df_autumn, df_spring], ignore_index=True)

year = datetime.now().year
out_path = f'Сводный_{year}.csv'
df_summary.to_csv(out_path, sep=';', index=False, encoding='utf-8-sig')


print(f'Готово! Файл сохранён: {out_path}')
print(f'  Строк из «Осень»:  {len(df_autumn)}')
print(f'  Строк из «Весна»:  {len(df_spring)}')
print(f'  Итого строк:       {len(df_summary)}')
print(f'  Столбцов:          {df_summary.shape[1]}')
