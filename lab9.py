import pandas as pd
import numpy as np

# 1. Генерация данных
np.random.seed(42)
data = pd.Series(np.random.normal(0, 100, 100000))

# 2. Описательная статистика
print("=== Исходная описательная статистика ===")
stats = data.describe()
print(stats)
print(f"\nРазница между средним и медианой: {abs(stats['mean'] - stats['50%']):.4f}")

# 3. Замена минимального значения
min_idx = data.idxmin()
max_val = data.max()
data[min_idx] = 5 * max_val

# 4. Новая описательная статистика
print("\n=== Описательная статистика после замены ===")
new_stats = data.describe()
print(new_stats)

print("\n=== Изменения ===")
print(f"Среднее: {stats['mean']:.4f} → {new_stats['mean']:.4f}")
print(f"Медиана: {stats['50%']:.4f} → {new_stats['50%']:.4f}")
print(f"Std: {stats['std']:.4f} → {new_stats['std']:.4f}")

print("\nОбъяснение: Среднее и std значительно изменились из-за выброса,")
print("а медиана осталась практически неизменной (устойчива к выбросам).")



import pandas as pd
import numpy as np

# Загрузка данных (замените путь на реальный)
# df = pd.read_csv('taxi_data.csv')

# Создадим примерные данные
np.random.seed(42)
n = 10000
df = pd.DataFrame({
    'passenger_count': np.random.choice([0, 1, 2, 3, 4, 5, 6], n, p=[0.02, 0.6, 0.2, 0.1, 0.04, 0.02, 0.02]),
    'trip_distance': np.random.exponential(3, n)
})

# 2a. Процент поездок с 1 и 6 пассажирами (метод count)
total = df['passenger_count'].count()
one_passenger = (df['passenger_count'] == 1).sum()
six_passengers = (df['passenger_count'] == 6).sum()
print(f"1 пассажир: {one_passenger/total*100:.2f}%")
print(f"6 пассажиров: {six_passengers/total*100:.2f}%")

# 2b. С использованием value_counts
print("\n=== value_counts ===")
print(df['passenger_count'].value_counts(normalize=True) * 100)

# 3. Категоризация поездок
def categorize_trip(distance):
    if distance <= 2:
        return 'short'
    elif distance <= 10:
        return 'medium'
    else:
        return 'long'

# 3a. Без pd.cut
df['trip_category'] = df['trip_distance'].apply(categorize_trip)

# 3b. С pd.cut
df['trip_category_cut'] = pd.cut(df['trip_distance'], 
                                  bins=[0, 2, 10, float('inf')],
                                  labels=['short', 'medium', 'long'])

# 4. Количество поездок в каждой категории
print("\n=== Количество поездок по категориям ===")
print(df['trip_category'].value_counts())



import pandas as pd
import numpy as np

# Создание датафрейма складских запасов
data = {
    'id': [10, 20, 30, 40, 50],
    'name': ['Ноутбук', 'Клавиатура', 'Мышь', 'Монитор', 'Наушники'],
    'wholesale_price': [45000, 1500, 500, 15000, 3000],
    'retail_price': [60000, 2500, 800, 22000, 5000],
    'sales_volume': [25, 150, 200, 40, 80]
}

df = pd.DataFrame(data)
df.index = df['id']
df = df.drop('id', axis=1)

print("Датафрейм складских запасов:")
print(df)

# Расчет общего дохода
df['revenue'] = df['retail_price'] * df['sales_volume']
total_revenue = df['revenue'].sum()

print(f"\n=== Выручка по товарам ===")
print(df['revenue'])
print(f"\nОбщий доход: {total_revenue:,} руб.")
