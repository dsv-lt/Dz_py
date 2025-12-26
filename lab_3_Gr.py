import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from ydata_profiling import ProfileReport

df = pd.read_csv("StudentsPerformance.csv")
rows, cols = df.shape
print(f"Строк: {rows}, столбцов: {cols}")
missing_per_column = df.isna().sum()
print("\nПропусков по столбцам:")
print(missing_per_column)
total_missing = missing_per_column.sum()
print(f"\nОбщее число пропусков: {total_missing}")
# 3. Вопрос 1: Сколько студентов набрали по математике выше среднего, а по письму ниже среднего?
math_mean = df["math score"].mean()
writing_mean = df["writing score"].mean()
condition = (df["math score"] > math_mean) & (df["writing score"] < writing_mean)
count_students = condition.sum()
print(f"\nСтудентов, у которых math > среднего ({math_mean:.2f}) "
      f"и writing < среднего ({writing_mean:.2f}): {count_students}")
df["math>avg & writing<avg"] = np.where(condition, "Да", "Нет")
sns.countplot(data=df, x="math>avg & writing<avg")
plt.title("Студенты с math > среднего и writing < среднего")
plt.xlabel("Условие выполняется?")
plt.ylabel("Количество студентов")
plt.show()
# Вопрос 2: Как распределены баллы по математике в зависимости от пола?
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="gender", y="math score")
plt.title("Распределение баллов по математике в зависимости от пола")
plt.xlabel("Пол")
plt.ylabel("Math score")
plt.show()
# Вопрос 3: Есть ли связь между баллами по математике и чтению?
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="math score", y="reading score", hue="gender")
plt.title("Связь между баллами по математике и чтению")
plt.xlabel("Math score")
plt.ylabel("Reading score")
plt.legend(title="Пол")
plt.show()
# Вопрос 4: У какой группы race/ethnicity наибольший средний суммарный балл?
df["total score"] = df["math score"] + df["reading score"] + df["writing score"]
group_means = df.groupby("race/ethnicity")["total score"].mean().sort_values(ascending=False)
print("\nСредний суммарный балл по группам race/ethnicity:")
print(group_means)
plt.figure(figsize=(6, 4))
sns.barplot(x=group_means.index, y=group_means.values)
plt.title("Средний суммарный балл по race/ethnicity")
plt.xlabel("race/ethnicity")
plt.ylabel("Средний total score")
plt.xticks(rotation=45)
plt.show()
# 4. Отчёт profile_report
profile = ProfileReport(df, title="Students Performance Report", explorative=True)
profile.to_notebook_iframe()
# 5. Визуализация пропусков
plt.figure(figsize=(8, 4))
msno.matrix(df)
plt.title("Матрица пропусков в данных")
plt.show()
