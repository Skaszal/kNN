from KNNSample import KNNSample
from KNNTrainingData import KNNTrainingData

k = 3
data = KNNTrainingData


def a():
    path = input("Podaj path do pliku testowego \n> ")
    if path == "":
        path = "data/test.txt"

    file = open(path, 'r')
    successes = 0
    total = 0
    for x in file:
        tmp = data.assign(x)
        tmp02 = KNNSample(x)
        print("Guessed: " + tmp, end="")
        print("Observed: " + tmp02.__str__())
        if tmp == tmp02.key:
            successes += 1
        total += 1

    print("Total success percent: " + str(successes / total * 100) + "%")


def b():
    print("podaj współrzędne punktu")
    tmp = input("> ") + ",key"
    print(data.assign(tmp))


def changeK():
    print("podaj nowa wartosc k")
    global k
    k = int(input("> "))
    data.k = k


def init(path):
    datalist = []
    for x in open(path, 'r'):
        datalist.append(KNNSample(x))
    global data

    data = KNNTrainingData(datalist, k)


if __name__ == "__main__":
    path = input("Podaj path do pliku treningowego \n> ")
    if path == "":
        path = "data/train.txt"
    init(path)

    while True:
        print('''
        Wybierz opcje:
        a) klasyfikuj z oddzielnego pliku
        b) klasyfikuj z konsoli
        c) zmien K
        d) wyjdz''')
        inp = input("> ").lower()

        if inp == "a":
            a()
        if inp == "b":
            b()
        if inp == "c":
            changeK()
        if inp == "d":
            break
