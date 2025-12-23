# ==================== ЗАДАНИЕ 1 ====================

# 1. Генерация Series с 100000 чисел из нормального распределения
# mean=0 (среднее), std=100 (стандартное отклонение)
np.random.seed(42)  # Для воспроизводимости результатов
data = pd.Series(np.random.normal(loc=0, scale=100, size=100000))

print("=" * 60)
print("ЗАДАНИЕ 1: Генерация данных и описательная статистика")
print("=" * 60)

# 2a. Получение показателей описательной статистики
print("\n2a. Описательная статистика (.describe()):")
print(data.describe())

print("\n--- Расшифровка показателей describe() ---")
print("""
count - количество непустых значений (100000)
mean  - среднее арифметическое (должно быть близко к 0)
std   - стандартное отклонение (должно быть близко к 100)
min   - минимальное значение
25%   - первый квартиль (25% данных меньше этого значения)
50%   - медиана (второй квартиль, 50% данных меньше)
75%   - третий квартиль (75% данных меньше этого значения)
max   - максимальное значение
""")

# 2b. Сравнение среднего и медианы
mean_value = data.mean()
median_value = data.median()
print(f"\n2b. Сравнение среднего и медианы:")
print(f"Среднее значение: {mean_value:.4f}")
print(f"Медиана: {median_value:.4f}")
print(f"Разница: {abs(mean_value - median_value):.4f}")
print("Вывод: Среднее и медиана очень близки, что характерно для нормального распределения")

# 3. Замена минимального значения на 5 * максимальное
print("\n3. Замена минимального значения:")
min_val = data.min()
max_val = data.max()
print(f"Минимальное значение ДО замены: {min_val:.4f}")
print(f"Максимальное значение: {max_val:.4f}")
print(f"Новое значение (5 * max): {5 * max_val:.4f}")

# Находим индекс минимального значения и заменяем
min_index = data.idxmin()
data[min_index] = 5 * max_val
print(f"Замена выполнена в индексе: {min_index}")

# 4. Повторное извлечение статистики
print("\n4. Описательная статистика ПОСЛЕ замены:")
print(data.describe())

# 4a,b. Анализ изменений
new_mean = data.mean()
new_median = data.median()
new_std = data.std()

print(f"\n4a. Сравнение показателей:")
print(f"Среднее ДО: {mean_value:.4f}, ПОСЛЕ: {new_mean:.4f}, Изменение: {new_mean - mean_value:.4f}")
print(f"Медиана ДО: {median_value:.4f}, ПОСЛЕ: {new_median:.4f}, Изменение: {new_median - median_value:.4f}")
print(f"Стд.откл. изменилось: {new_std:.4f}")

print("""
4b. Объяснение изменений:
- Среднее ИЗМЕНИЛОСЬ, т.к. оно чувствительно к выбросам (экстремальным значениям)
- Медиана практически НЕ ИЗМЕНИЛАСЬ, т.к. она устойчива к выбросам
- Стандартное отклонение УВЕЛИЧИЛОСЬ из-за появления экстремального значения
- Это демонстрирует, почему медиана часто предпочтительнее среднего при наличии выбросов
""")

# ==================== ЗАДАНИЕ 2 ====================

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Анализ данных о поездках в такси")
print("=" * 60)

# 1. Загрузка CSV файлов
# !!! УКАЖИТЕ ПУТЬ К ВАШИМ ФАЙЛАМ !!!
# Вариант 1: Если файлы в той же папке, что и скрипт
taxi_data_1 = pd.read_csv('taxi_data_1.csv')  # Замените на ваше имя файла
taxi_data_2 = pd.read_csv('taxi_data_2.csv')  # Замените на ваше имя файла

# Вариант 2: С полным путём (пример для Windows)
# taxi_data_1 = pd.read_csv('C:/Users/ИмяПользователя/Desktop/taxi_data_1.csv')
# taxi_data_2 = pd.read_csv('C:/Users/ИмяПользователя/Desktop/taxi_data_2.csv')

# Для демонстрации объединим файлы (если нужно работать с обоими)
# taxi_data = pd.concat([taxi_data_1, taxi_data_2], ignore_index=True)

# Будем работать с первым файлом (или замените на нужный)
taxi_data = taxi_data_1

print("\nПервые 5 строк данных:")
print(taxi_data.head())
print(f"\nФорма датафрейма: {taxi_data.shape}")
print(f"\nНазвания столбцов: {taxi_data.columns.tolist()}")

# 2. Процент заказов с 1 и 6 пассажирами
# Предполагаем, что столбец называется 'passenger_count'
# Если называется иначе, замените на правильное имя

passenger_col = 'passenger_count'  # Замените на реальное имя столбца при необходимости

print(f"\n--- Анализ количества пассажиров (столбец '{passenger_col}') ---")

# 2a. Прямой метод с использованием .count()
total_trips = taxi_data[passenger_col].count()
trips_1_passenger = taxi_data[taxi_data[passenger_col] == 1][passenger_col].count()
trips_6_passengers = taxi_data[taxi_data[passenger_col] == 6][passenger_col].count()

percent_1 = (trips_1_passenger / total_trips) * 100
percent_6 = (trips_6_passengers / total_trips) * 100

print("\n2a. Прямой метод с .count():")
print(f"Всего поездок: {total_trips}")
print(f"Поездок с 1 пассажиром: {trips_1_passenger} ({percent_1:.2f}%)")
print(f"Поездок с 6 пассажирами: {trips_6_passengers} ({percent_6:.2f}%)")

# 2b. Метод с использованием .value_counts()
print("\n2b. Метод с .value_counts():")
passenger_counts = taxi_data[passenger_col].value_counts()
print("Распределение по количеству пассажиров:")
print(passenger_counts)

# Проценты через value_counts()
passenger_percent = taxi_data[passenger_col].value_counts(normalize=True) * 100
print("\nПроценты:")
if 1 in passenger_percent.index:
    print(f"1 пассажир: {passenger_percent[1]:.2f}%")
if 6 in passenger_percent.index:
    print(f"6 пассажиров: {passenger_percent[6]:.2f}%")

# 3. Создание категорий поездок по дистанции
# Предполагаем, что столбец называется 'trip_distance'
distance_col = 'trip_distance'  # Замените на реальное имя столбца

print(f"\n--- Категоризация поездок по дистанции (столбец '{distance_col}') ---")

# 3a. Прямой метод БЕЗ pd.cut()
def categorize_distance(distance):
    """Функция для категоризации дистанции поездки"""
    if distance <= 2:
        return 'short'
    elif distance <= 10:
        return 'medium'
    else:
        return 'long'

# Применяем функцию к каждому значению
trip_categories_direct = taxi_data[distance_col].apply(categorize_distance)

print("\n3a. Прямой метод (без pd.cut()):")
print("Количество поездок по категориям:")
print(trip_categories_direct.value_counts())

# 3b. Метод с использованием pd.cut()
# Определяем границы категорий
bins = [0, 2, 10, float('inf')]  # 0-2, 2-10, 10+
labels = ['short', 'medium', 'long']

trip_categories_cut = pd.cut(taxi_data[distance_col], bins=bins, labels=labels, right=True)

print("\n3b. Метод с pd.cut():")
print("Количество поездок по категориям:")
print(trip_categories_cut.value_counts())

# 4. Количество поездок в каждой категории (итоговое)
print("\n4. Итоговое количество поездок по категориям:")
print(trip_categories_cut.value_counts().sort_index())

# ==================== ЗАДАНИЕ 3 ====================

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Датафрейм складских запасов")
print("=" * 60)

# Создание датафрейма с данными о товарах
warehouse_data = {
    'ID': [23, 96, 97, 15, 87],
    'товар': ['батон', 'масло', 'икра', 'банан', 'сода'],
    'опт': [500.0, 35.0, 35.0, 0.5, 3.0],
    'цена': [1000, 75, 75, 1, 5],
    'продажи': [100, 1000, 500, 200, 300]
}

df_warehouse = pd.DataFrame(warehouse_data)

print("\nСозданный датафрейм:")
print(df_warehouse)

# 1. Расчет общего дохода по всем товарам
# Доход = цена продажи * количество продаж
df_warehouse['доход'] = df_warehouse['цена'] * df_warehouse['продажи']

print("\nДатафрейм с рассчитанным доходом:")
print(df_warehouse)

total_revenue = df_warehouse['доход'].sum()
print(f"\nОбщий доход по всем товарам: {total_revenue} руб.")

# Дополнительно: расчет прибыли (доход - себестоимость)
df_warehouse['себестоимость'] = df_warehouse['опт'] * df_warehouse['продажи']
df_warehouse['прибыль'] = df_warehouse['доход'] - df_warehouse['себестоимость']

print("\nДатафрейм с полным расчетом:")
print(df_warehouse)
print(f"\nОбщая прибыль: {df_warehouse['прибыль'].sum()} руб.")

https://gist.github.com/reuven/a0bded849e5925f46ff44686d6f7383e

https://gist.github.com/reuven/5d0523fb7a18abcde6f3efcb0bc26f17
