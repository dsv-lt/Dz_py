""" Нейронная сеть определяет принадлежность точки к кластерам на плоскости
Нейронная сеть состоит из двух входных нейронов, двух нейронов скрытого слоя и одного выходного нейрона
Всего 5 нейронов, 6 весов
Кластеры задаются с помощью программы writeclaster.py и записваются в файл clasters.txt
Первый столбец - x
Второй столбец - y
Третий столбец - номер кластера (с учетом нормировки)
В файле clasters.txt первая строка характеризует центр первого кластера,
вторая строка характеризует центр второго кластера
"""
from math import e
from random import randint
import matplotlib.pyplot as plt
import numpy as np
# Считывание информации о кластерах из файла
# Считываем все строки из файла clasters.txt в data1
data1 = open('clasters.txt', 'r', encoding='utf-8').readlines()
# Количество строк
length = len(data1)
vcl = set()
# Убираем в строках пробелы и переходы на следущую строку
for i in range(length):
    data1[i] = data1[i].replace('\n', '').split()
# Определяем количество элементов в строке
numpar = len(data1[0])
# Создание нулевой матрицы, где хранится вся информация о кластерах: координаты и номер кластера
data = np.zeros((length, numpar))
# пробегаемся по строкам
for i in range(length):
    vcl.add(float(data1[i][2]))
    # Пробегаемся по строке
    for j in range(numpar):
        # Записываем в нулевую матрицу обработанную информацию из файла
        data[i][j] = float(data1[i][j])
vcl = list(vcl)
# Лучшая фитнес-функция
fitness = 10000000000
# Веса нейронов изменяются в диапазоне от -dw до dw
dw=5
# Количество точек на отрезке от -dw до dw
diap = 30000
# Диапазон изменения нейрона смещения от -diapb до diapb
diapb=2
# Количество точек на отрезке от -dw до dw
diapn=10000
# Точки x для вывода графика суммарной ошибки
xcord = []
# Массив суммарных ошибок
error = []
# Количество весов
numweight = 6
# Создание массива весов
weight = [0] * numweight
# Создание массива лучших весов
bestweight = [0] * numweight
# Создание массива для хранения значений нейронной сети для всех строк обучающего множества
outnet = [0] * length
# Лучшие коэффициенты смещения
b1best=0
b2best=0
# Коэффициенты смещения
b1=0
b2=0
# Коэффициент нормировки
knorm = 50
# Минимум диапазона для первого кластера
difmin1 = 10000
# Максимум диапазона для первого кластера
difmax1 = 0
# Минимум диапазона для второго кластера
difmin2 = 10000
# Максимум диапазона для второго кластера
difmax2 = 0
# Минимум лучшего диапазона для первого кластера
difmin1best = 10000
# Максимум лучшего диапазона для первого кластера
difmax1best = 0
# Минимум лучшего диапазона для второго кластера
difmin2best = 10000
# Максимум лучшего диапазона для второго кластера
difmax2best = 0
# Функция активации. Вид - сигмоид
def sigm(x):
    return 1 / (1 + e**(-x))
# Фитнес-функция
def fit():
    global difmin1, difmin2, difmax1, difmax2
    cl1p = outnet[0]  # Получение первого кластера из первой строки 
    cl2p = outnet[1]  # Получение второго кластера из второй строки
    # Объявление суммы отклонений
    summ = 0
    # Номер первого кластера
    numcl1 = int(data[0][2] * knorm)
    # Номер второго кластера
    numcl2 = int(data[1][2] * knorm)
    # Сброс диапазонов для кластеров
    difmin1 = 1000000
    difmin2 = 1000000
    difmax1 = 0
    difmax2 = 0
    # Ищем минимальное значение для первого и второго кластеров
    for i in range(length):
        nk = data[i][2]
        neti = outnet[i]
        # Первый кластер
        if nk == vcl[0]:
            # Максимум первого кластера
            if neti > difmax1:
                difmax1 = neti
            # Минимум первого кластера
            if neti < difmin1:
                difmin1 = neti
        # Второй кластер
        if nk == vcl[1]:
            # Максимум второго кластера
            if neti > difmax2:
                difmax2 = neti
            # Минимум второго кластера
            if neti < difmin2:
                difmin2 = neti
    for i in range(length):
        neti = outnet[i]  # Определение значения нейронной сети для текущего кластера
        clust = -1  # Определение индекса кластера. Если равен -1, значит кластер не определен
        col = 0  # Определение количества принадлежностей к кластерам
        # Если значение нейронной сети попало в диапазон первого кластера, то определяем первый кластер
        if difmin1 <= neti <= difmax1:
            clust = 0
            col += 1
        # Если значение нейронной сети попало в диапазон второго кластера, то определяем второй кластер
        if difmin2 <= neti <= difmax2:
            clust = 1
            col += 1
        # Если кластер не определен, или номер кластера определен неверно, или кластер определен более одного раза, то увеличиваем суммарную ошибку
        if clust == -1 or vcl[clust] != data[i][2] or col > 1:
            summ += 1
    return summ
# Запуск обученной нейронной сети. Выводит числовое значение
def runnet(x1, x2):
    i1 = x1
    i2 = x2
    input1h = i1 * bestweight[0] + i2 * bestweight[2]+b1best
    input2h = i1 * bestweight[1] + i2 * bestweight[3]+b1best
    output1h = sigm(input1h)
    output2h = sigm(input2h)
    inputo = output1h * bestweight[4] + output2h * bestweight[5]+b2best
    outputo = sigm(inputo)
    return outputo
ept = int(input('Количество эпох: '))
# пробегаемся по всем эпохам
for ep in range(ept):
    # Пробегаемся по всем весам и определяем значения весов в заданных диапазонах
    for g in range(numweight):
        weight[g] = dw-2*dw*randint(0, diap) / diap
    # Определяем значения нейронов смещения
    b1=diapb-2*diapb*randint(0, diapn) / diapn
    b2=diapb-2*diapb*randint(0, diapn) / diapn
    #b1 = diapb * randint(0, diapn) / diapn
    #b2 = diapb * randint(0, diapn) / diapn
    # Для всех строк обучающего множества находим значение нейронной сети и записываем его в массив outnet
    for i in range(length):
        i1 = data[i][0]
        i2 = data[i][1]
        input1h = i1 * weight[0] + i2 * weight[2] + b1
        input2h = i1 * weight[1] + i2 * weight[3] + b1
        output1h = sigm(input1h)
        output2h = sigm(input2h)
        inputo = output1h * weight[4] + output2h * weight[5]  + b2
        outputo = sigm(inputo)
        outnet[i] = outputo
    # Рассчет фитнес-функции (суммарная ошибка обучения нейронной сети)
    # Фитнес-функция работает с массивом outnet
    fitt = fit()
    # Если значение фитнес-функции уменьшилось, то перезаписываем лучшее решение
    if fitt < fitness:
        # Перезапись лучшего значения фитнес-функции
        fitness = fitt
        # Запись координаты x для вывода графика суммарной ошибки
        xcord.append(ep + 1)
        # Запись суммарной ошибки (фитнес-функции)
        error.append(fitt)
        print('Улучшение фитнес-функции:', fitt, 'Итерация:', ep + 1)
        # Пробегаемся по весам и записываем их в лучшие веса
        for g in range(numweight):
            bestweight[g] = weight[g]
        # Запись лучших значений нейронов смещения
        b1best=b1
        b2best=b2
        # Перезапись лучших диапазонов кластеров
        difmin1best = difmin1
        difmax1best = difmax1
        difmin2best = difmin2
        difmax2best = difmax2
# Построение графика динамики ошибки
maxerror = max(error)  # Получение максимума ошибки для нормировки графика
plt.plot(xcord, error, c='deeppink')
plt.show()
# Калибровка
cl1 = runnet(data[0][0], data[0][1])  # Получение первого кластера из первой строки 
cl2 = runnet(data[1][0], data[1][1])  # Получение второго кластера из второй строки
# Возврат номера кластера для обученной нейронной сети
def netr(x1, x2):
    net = runnet(x1, x2)  # Расчитываем нейронную сеть для заданной точки
    clust = -1  # Номер определенного кластера. Если равен -1, значит кластер не определен
    col = 0  # Количество определенных кластеров
    # Если значение нейронной сети в диапазоне первого кластера, то объявляем первый кластер
    if difmin1best <= net <= difmax1best:
        clust = 0  # Определение первого кластера (индекс 0)
        col += 1  # Увеличиваем количество определенных кластеров
    # Если значение нейронной сети в диапазоне второго кластера, то объявляем второй кластер
    if difmin2best <= net <= difmax2best:
        clust = 1  # Определение второго кластера (индекс 1)
        col += 1  # Увеличиваем количество определенных кластеров
    # Если количество определенных кластеров более одного, то возвращаем undefined (не определено)
    if col > 1:
        return 'undefined'
    # Если кластер не был определен (clust равен -1), то возвращаем -1
    if clust == -1:
        return -1
    # Если кластер был определен и количество определенных кластеров равно одному, то возвращаем номер определенного кластера
    return int(vcl[clust] * knorm)

# Производим тест на тестовом файле test.txt
# Результаты теста записываются в resulttest.txt
# Сначала записываются координаты точки, потом значение обученной нейронной сети, зачем значение из теста,
# если значения совпали, то следующий столбец 1, иначе 0
def test():
    # Считывание информации о тестовых кластерах из файла
    # Считываем все строки из файла test.txt в data1
    data1 = open('test.txt', 'r', encoding='utf-8').readlines()
    # Количество строк
    length = len(data1)
    # Убираем в строках пробелы и переходы на следущую строку
    for i in range(length):
        data1[i] = data1[i].replace('\n', '').split()
    # Определяем количество элементов в строке
    numpar = len(data1[0])
    # Создание нулевой матрицы, где хранится вся информация о кластерах: координаты и номер кластера
    data = np.zeros((length, numpar))
    # пробегаемся по строкам
    for i in range(length):
        # Пробегаемся по строке
        for j in range(numpar):
            # Записываем в нулевую матрицу обработанную информацию из файла
            data[i][j] = float(data1[i][j])
    netout = []  # Массив для хранения вывода нейронной сети
    result = []  # Массив для хранения правильности определения номеров кластеров
    # Пробегаемся по всему тестовому множеству для записи вывода нейронной сети и правильности ответа
    for i in range(length):
        # Получение вывода нейронной сети
        net = netr(data[i][0], data[i][1])
        # Запись вывода нейронной сети в массив
        netout.append(net)
        # Запись правильности вывода
        if net == data[i][2] * knorm:
            result.append(1)
        else:
            result.append(0)
    # Запись результата тестирования
    with open('resulttest.txt', 'w', encoding='utf-8') as f:
        # Пробегаемся по всему тестовому множеству
        for i in range(length):
            # Запись первой координаты точки
            f.write(str(round(data[i][0], 4)))
            f.write(' ')
            # Запись второй координаты точки
            f.write(str(round(data[i][1], 4)))
            f.write(' ')
            # Запись вывода нейронной сети
            f.write(str(netout[i]))
            f.write(' ')
            # Запись номера кластера
            f.write(str(int(data[i][2] * knorm)))
            f.write(' ')
            # Запись правильности вывода нейронной сети
            f.write(str(result[i]))
            f.write('\n')
        # Определение процента правильных ответов
        correct = int(sum(result) / len(result) * 100)
        # Определение процента неправильных ответов
        wrong = 100 - correct
        print(f'Верно: {correct}%')
        print(f'Неверно: {wrong}%')
        # Запись процента правильных ответов
        f.write('Correct: ')
        f.write(str(correct))
        # Запись процента неправильных ответов
        f.write('%\nWrong: ')
        f.write(str(wrong))
        f.write('%')
    print('Тест завершен.')
# Запись нейронной сети в файл
def buildneuro(knorm, cl1n, cl2n, b1, b2, weight):
    # Открытие файла для записи нейронной сети
    with open('buildedneuro.txt', 'w', encoding='utf-8') as f:
        f.write(str(knorm))  # Запись нормировочного коэффициента
        f.write(' ')
        f.write(str(cl1n))  # Запись номера первого кластера
        f.write(' ')
        f.write(str(cl2n))  # Запись номера второго кластера
        f.write('\n')
        # Запись диапазонов кластеров
        f.write(str(difmin1best))
        f.write(' ')
        f.write(str(difmax1best))
        f.write(' ')
        f.write(str(difmin2best))
        f.write(' ')
        f.write(str(difmax2best))
        f.write('\n')
        # Запись номеров кластеров
        f.write(str(vcl[0]))
        f.write(' ')
        f.write(str(vcl[1]))
        f.write('\n')
        f.write(str(b1))  # Запись параметра нейрона смещения для входного слоя
        f.write(' ')
        f.write(str(b2))  # Запись параметра нейрона смещения для скрытого слоя
        f.write('\n')
        # Запись весов в файл в столбик
        for i in weight:
            f.write(str(i))
            f.write('\n')
    print('Нейронная сеть записана в файл buildedneuro.txt')
buildneuro(knorm, int(data[0][2] * knorm), int(data[1][2] * knorm), b1best, b2best, bestweight)  # Запись нейронной сети в файл
test()
print('Точка для первого кластера с координатами (0.1; 0.18):', netr(0.1, 0.18))  # -> 1
print('Точка для первого кластера с координатами (0.12; 0.72):', netr(0.12, 0.72))  # -> 20
print(bestweight)
