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
    k = int(input("> "))


def init(path):
    global trainFile
    trainFile = open(path, "r")

    tmp = trainFile.readline()
    global dataSize
    dataSize = len(tmp)


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

