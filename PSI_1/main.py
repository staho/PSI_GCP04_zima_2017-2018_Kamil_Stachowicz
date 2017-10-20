from perceptron import Perceptron
from testpoint import TestPoint

points = []

for i in range(70):
    points.append(TestPoint())

fo = open("wyniki.txt", "a")
learningRate = 10
iloscEpok = 1
iloscNaEpoke = 20

percept = Perceptron(learningRate)
for s in range(5):
    fo.write("==============================\nUczenie perceptronu\n==============================\n")

    for z in range(s+1):
        stringToWrite = "Epoka nr " + str(z + 1) + "\n"
        fo.write(stringToWrite)
        iloscBledow = 0
        iloscBledow += percept.wrong

        for i in range(iloscNaEpoke):
            percept.train(points[i].x, points[i].y, points[i].match)

        stringToWrite = "\tIlosc bledow w epoce " + str(percept.wrong - iloscBledow) + "/" + str(iloscNaEpoke) + "\n"
        fo.write(stringToWrite)

    stringToWrite2 = "\n\tIlosc bledow podczas uczenia " + str(percept.wrong) + "\n"
    fo.write(stringToWrite2)

    print("=========Bez uczenia=========")
    percept.wrong = 0
    for i in range(20):
        percept.guess(points[i+50].x, points[i+50].y)
    stringToWrite = "==============================\nIlosc bledow bez uczenia (20 prob): " + str(percept.wrong) + "\nLearningRate = " + str(percept.learningRate) +"\n\n\n"
    fo.write(stringToWrite)
fo.close()
