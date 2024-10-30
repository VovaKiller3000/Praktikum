import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Загрузка данных
df = pd.read_csv(r'C:\Users\user\Desktop\intensiv\cleaned_file_20.csv')



# Кодирование необходимых колонок
label_encoder = LabelEncoder()
df['district'] = label_encoder.fit_transform(df['district'])
df['street'] = label_encoder.fit_transform(df['street'])
df['underground'] = label_encoder.fit_transform(df['underground'])
df['residential_complex'] = label_encoder.fit_transform(df['residential_complex'])
df['house_material_type'] = label_encoder.fit_transform(df['house_material_type'])
df['location'] = label_encoder.fit_transform(df['location'])  # Кодирование колонки location

# Вычисление корреляционной матрицы
correlation_matrix = df.corr()

# Визуализация корреляционной матрицы
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Корреляционная матрица')
plt.show()