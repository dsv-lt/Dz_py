def strange_translate(word):
    vowels = "аеёиоуыэюя"
    if word[0].lower() in vowels:
        return word + "хей"
    else:
        return word[1:] + word[0] + "ей"

# Чтение исходного файла
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()

# Разделение на слова
words = text.split()

# Преобразование слов
translated = [strange_translate(word) for word in words]

# Проверка: вывод в консоль
print("Исходные слова: ", words)
print("Переведённые слова:", translated)

# Запись результата в output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(translated))

print("\n✅ Перевод записан в output.txt")
