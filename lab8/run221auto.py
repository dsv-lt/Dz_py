from math import e
# Функция сигмоида
def sigm(x):
    return 1 / (1 + e**(-x))
# Запуск лучшей нейронной сети
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
# Возврат номера кластера для обученной нейронной сети
def netr(x1, x2):
    net = runnet(x1, x2)  # Расчитываем нейронную сеть для заданной точки
    clust = -1
    col = 0
    if difmin1best <= net <= difmax1best:
        clust = 0
        col += 1
    if difmin2best <= net <= difmax2best:
        clust = 1
        col += 1
    if col > 1:
        return 'undefined'
    if clust == -1:
        return -1
    return int(vcl[clust] * knorm)
def readneuro():
    global knorm, cl1n, cl2n, difmin1best, difmax1best, difmin2best, difmax2best, vcl, b1best, b2best, bestweight
    # Считывание информации о записанной нейронной сети
    data = open('buildedneuro.txt', 'r', encoding='utf-8').read().split()
    # Первые семь элементов отданы под параметры (индексы от 0 до 6)
    knorm = int(data[0])  # Получение коэффициента нормировки
    cl1n = int(data[1])  # Получение номера первого кластера
    cl2n = int(data[2])  # Получение номера второго кластера
    difmin1best = float(data[3])
    difmax1best = float(data[4])
    difmin2best = float(data[5])
    difmax2best = float(data[6])
    cl1 = float(data[7])
    cl2 = float(data[8])
    vcl = [cl1, cl2]
    b1best = float(data[9])  # Получение параметра нейрона смещения для входного слоя
    b2best = float(data[10])  # Получение параметра нейрона смещения для скрытого слоя
    # Остальные элементы - веса (индексы от 11 до конца)
    bestweight = list(map(float, data[11:]))  # Получение весов
readneuro()
print(netr(0.1, 0.18))  # -> 1
print(netr(0.23, 0.84))  # -> 4
print(netr(0.22, 0.62))  # -> 4
print(netr(20, 20))  # -> 1
