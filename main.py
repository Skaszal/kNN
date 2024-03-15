from KNNSample import KNNSample
from KNNTrainingData import KNNTrainingData

k = 3
data = 0


def a():
    pass


def b():
    pass


def changeK():
    print("podaj nowa wartosc k")
    global k
    k = int(input("> "))


def init(path):
    datalist = []
    for x in open(path, 'r'):
        datalist.append(KNNSample(x))
    global data

    data = KNNTrainingData(datalist, k)


if __name__ == "__main__":
    path = input("Podaj path do pliku treningowego \n> ")
    init(path)

    while True:
        print(" Wybierz chuje muje")
        inp = input("> ").lower()

        if inp == "a":
            a()
        if inp == "b":
            b()
        if inp == "c":
            changeK()
        if inp == "d":
            break
