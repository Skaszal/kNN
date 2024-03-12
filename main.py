testFile = open("data/test.txt", "r")
dataSize = 0
k = 3



def a():
    print()


def b():
    print()


def changeK():
    print("podaj nowa wartosc k")
    global k
    k = input("> ")


def init(path):
    trainFile = open(path, "r")
    for line in trainFile:
        localData = line.split(",")
        dataSize = len(localData)


if __name__ == "__main__":
    path = input("Podaj path do pliku treningowego \n> ")
    init(path)

    while True:
        print(" Wybierz chuje muje")
        inp = input("> ")
        inp = inp.lower()
        if inp == "a":
            a()
        if inp == "b":
            b()
        if inp == "c":
            changeK()
        if inp == "d":
            break
