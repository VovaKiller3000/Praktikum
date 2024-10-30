import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv(r'C:\Users\user\Desktop\intensiv\cleaned_file_19.csv')

# Удаление колонок deal_type и accommodation_type
df.drop(columns=['deal_type', 'accommodation_type'], inplace=True)

# Сохранение нового DataFrame в новый CSV файл
df.to_csv('updated_file.csv', index=False)