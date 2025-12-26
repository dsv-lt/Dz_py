import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

so_df = pd.read_csv('so_2021_survey_results.csv')
print("2. Info:")
so_df.info()
print("Describe:", so_df.describe())
# 3. Удаление дубликатов и константных столбцов
so_df = so_df.drop_duplicates()
for col in so_df.columns:
    if so_df[col].nunique() <= 1:
        so_df = so_df.drop(col, axis=1)
print(f"3. Дубликаты удалены. Текущий размер: {so_df.shape}")
# 4. Разделение на df_1 (числа) и df_2 (категории)
df_1 = so_df.select_dtypes(include=[np.number])
df_2 = so_df.select_dtypes(exclude=[np.number])
print(f"4. df_1 (числа): {df_1.columns.tolist()}")
print(f"   df_2 (объекты): {df_2.columns.tolist()}")
# 5. Очистка df_1
# 5a. Удалить колонки, где > 50% пропусков
limit = len(df_1) * 0.5
df_1 = df_1.dropna(thresh=limit, axis=1)
# 5b. Удалить строки с пустыми значениями (ВНИМАНИЕ: это может удалить много данных)
df_1 = df_1.dropna()
# 6. Восстановление пропусков (SimpleImputer)
imputer = SimpleImputer(strategy='mean')  # или 'median'
df_1_imputed = pd.DataFrame(imputer.fit_transform(df_1), columns=df_1.columns)
print("6. Пропуски в df_1 заполнены средним значением.")
# 7. One-Hot Encoding для ВСЕГО df_2
print("7. Категоризация всего df_2 (One-Hot Encoding)...")
df_2_filled = df_2.fillna('Unknown')
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_data = encoder.fit_transform(df_2_filled)
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(df_2.columns))
print(f"Размер df_2 до кодирования: {df_2.shape}")
print(f"Размер df_2 после кодирования: {encoded_df.shape}")
print(encoded_df.iloc[:, :5].head())
# 8. Проверка на коллинеарность (на примере df_1)
print("8. Проверка на коллинеарность (df_1)...")
# a. Матрица корреляции
corr_matrix = df_1_imputed.corr().abs()
# b. Определяем сильно коррелирующие (>0.9)
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
# Находим колонки, которые нужно удалить
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
print("Сильно коррелирующие признаки для удаления:", to_drop)
# c. Создание DF без них
df_1_reduced = df_1_imputed.drop(columns=to_drop)
print(f"Итоговый размер df_1: {df_1_reduced.shape}")
