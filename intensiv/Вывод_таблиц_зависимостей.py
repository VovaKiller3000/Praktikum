import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv(r'C:\Users\user\Desktop\intensiv\cleaned_file_20.csv')

# Получение всех колонок, кроме 'Цена за квадратный метр'
columns_to_plot = df.columns[df.columns != 'Цена за квадратный метр']

# Определение количества графиков за раз
graphs_per_figure = 6
num_figures = (len(columns_to_plot) + graphs_per_figure - 1) // graphs_per_figure  # Количество фигур

for figure in range(num_figures):
    plt.figure(figsize=(15, 10))
    for i in range(graphs_per_figure):
        index = figure * graphs_per_figure + i
        if index < len(columns_to_plot):
            column = columns_to_plot[index]
            plt.subplot(2, 3, i + 1)
            plt.scatter(df[column], df['Цена за квадратный метр'], alpha=0.5)
            plt.title(f'Зависимость цены за квадратный метр от {column}')
            plt.xlabel(column)
            plt.ylabel('Цена за квадратный метр')
    
    plt.tight_layout()
    plt.show()