import pandas as pd
import numpy as np

# Загрузка данных (создадим примерные данные)
np.random.seed(42)
n = 50000

df = pd.DataFrame({
    'passenger_count': np.random.choice(range(0, 10), n, 
                       p=[0.02, 0.65, 0.15, 0.08, 0.04, 0.03, 0.02, 0.005, 0.003, 0.002]),
    'trip_distance': np.abs(np.random.exponential(3, n)),
    'total_amount': np.abs(np.random.exponential(20, n)),
    'payment_type': np.random.choice([1, 2], n, p=[0.7, 0.3])
})

# Задание 1: Выбросы
print("=== ЗАДАНИЕ 1: ВЫБРОСЫ ===")
df_outliers = df[['passenger_count', 'trip_distance']].copy()

# Расчет IQR для trip_distance
Q1 = df_outliers['trip_distance'].quantile(0.25)
Q3 = df_outliers['trip_distance'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Нахождение выбросов
outliers_mask = (df_outliers['trip_distance'] < lower_bound) | (df_outliers['trip_distance'] > upper_bound)
outliers = df_outliers[outliers_mask]

print(f"Количество выбросов: {len(outliers)}")
print(f"Среднее количество пассажиров в выбросах: {outliers['passenger_count'].mean():.2f}")
print(f"Среднее количество пассажиров для всех поездок: {df['passenger_count'].mean():.2f}")

# Задание 2: Маски
print("\n=== ЗАДАНИЕ 2: МАСКИ ===")

# 1. Больше 8 пассажиров
mask_8plus = df['passenger_count'] > 8
print(f"Поездок с >8 пассажирами: {mask_8plus.sum()}")

# 2. Ноль пассажиров
mask_zero = df['passenger_count'] == 0
print(f"Поездок с 0 пассажирами: {mask_zero.sum()}")

# 3. Наличные и сумма > 1000
mask_cash = df['payment_type'] == 2
mask_1000 = df['total_amount'] > 1000
mask_combined = mask_cash & mask_1000
print(f"Оплата наличными >1000$: {mask_combined.sum()}")

# 4. Отрицательная сумма
mask_negative = df['total_amount'] < 0
print(f"Отрицательная сумма оплаты: {mask_negative.sum()}")

# 5. Дистанция < средней, сумма > средней
mean_distance = df['trip_distance'].mean()
mean_amount = df['total_amount'].mean()
mask_short_expensive = (df['trip_distance'] < mean_distance) & (df['total_amount'] > mean_amount)
count_short_expensive = df.loc[mask_short_expensive, 'trip_distance'].count()
print(f"Короткие дорогие поездки: {count_short_expensive}")

# Задание 3: Сортировки
print("\n=== ЗАДАНИЕ 3: СОРТИРОВКИ ===")
df_sort = df[['passenger_count', 'trip_distance', 'total_amount']].copy()

# 1. Сортировка по убыванию дистанции
df_desc = df_sort.sort_values('trip_distance', ascending=False)
avg_top20_desc = round(df_desc.iloc[:20]['total_amount'].mean(), 2)
print(f"Средняя стоимость 20 самых длинных поездок: {avg_top20_desc}")

# 2. Сортировка по возрастанию
df_asc = df_sort.sort_values('trip_distance', ascending=True)
avg_top20_asc = round(df_asc.iloc[-20:]['total_amount'].mean(), 2)
print(f"То же (через сортировку по возрастанию): {avg_top20_asc}")

# 3. Сортировка по нескольким столбцам
df_multi = df_sort.sort_values(['passenger_count', 'trip_distance'], ascending=[True, False])
avg_50 = round(df_multi.iloc[:50]['total_amount'].mean(), 4)
print(f"Средняя цена 50 первых поездок (мин пассажиров, макс дистанция): {avg_50}")

# Задание 4: Группировки
print("\n=== ЗАДАНИЕ 4: ГРУППИРОВКИ ===")

# 1. Среднее по количеству пассажиров
avg_by_passengers = df.groupby('passenger_count')['total_amount'].mean().sort_values()
print("Средняя стоимость по количеству пассажиров:")
print(avg_by_passengers)

# 3. Категоризация дистанции
def categorize(dist):
    if dist < 2:
        return 'short'
    elif dist <= 10:
        return 'medium'
    else:
        return 'long'

df['trip_distance_group'] = df['trip_distance'].apply(categorize)

avg_passengers_by_category = df.groupby('trip_distance_group')['passenger_count'].mean().sort_values(ascending=False)
print("\nСреднее количество пассажиров по категориям:")
print(avg_passengers_by_category)
