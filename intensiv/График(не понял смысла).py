import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Загрузка данных из CSV файла
df = pd.read_csv(r'C:\Users\user\Desktop\intensiv\cleaned_file_20.csv')

# Инициализация LabelEncoder
label_encoder = LabelEncoder()

# Кодирование указанных колонок
df['location'] = label_encoder.fit_transform(df['location'])
df['house_material_type'] = label_encoder.fit_transform(df['house_material_type'])

# Создание графика Boxplot для зависимости цены от местоположения
plt.figure(figsize=(14, 6))
sns.boxplot(x='location', y='Цена за квадратный метр', data=df)
plt.title('Зависимость цены за квадратный метр от местоположения')
plt.xlabel('Местоположение')
plt.ylabel('Цена за квадратный метр')
plt.xticks(rotation=45)
plt.show()

# Создание графика Violinplot для зависимости цены от типа материала дома
plt.figure(figsize=(14, 6))
sns.violinplot(x='house_material_type', y='Цена за квадратный метр', data=df)
plt.title('Зависимость цены за квадратный метр от типа материала дома')
plt.xlabel('Тип материала дома')
plt.ylabel('Цена за квадратный метр')
plt.xticks(rotation=45)
plt.show()