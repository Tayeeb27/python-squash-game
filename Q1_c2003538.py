import random
import csv
import matplotlib.pyplot as plt
from fractions import Fraction


# Q1(a)
def game(ra, rb):
    scoreA = 0
    scoreB = 0
    p = ra / (ra + rb)
    while not scoreA >= 11 or scoreB >= 11:
        r = random.random()
        if r < p:
            scoreA += 1
        else:
            scoreB += 1
    return scoreA, scoreB


print(game(70, 30))


# Q1(b)


def win_probability(ra, rb, n):
    A_Wins = 0
    B_Wins = 0

    for i in range(n):

        scoreA, scoreB = game(ra, rb)

        if scoreA > scoreB:
            A_Wins += 1
        else:
            B_Wins += 1

        return round(A_Wins / A_Wins + B_Wins, 2)


print((win_probability(70, 30, 10)))


# Q1(c)


def csv_to_list():
    with open('game.csv', newline='') as g:
        reader = csv.reader(g)
        next(reader)
        data = [tuple(row) for row in reader]

    return data


print(csv_to_list())


# Q1(d)


def list_to_fraction():
    data = csv_to_list()
    my_fraction = []

    for i in data:
        fraction_ = Fraction(int(i[0]), int(i[1]))
        my_fraction.append(fraction_)
    return my_fraction


def func_to_list():
    data = csv_to_list()
    my_list = []
    for i in data:
        y = win_probability(int(i[0]), int(i[0]), 4)
        my_list.append(y)
    return my_list


def graph():
    plt.plot(list_to_fraction(), func_to_list(), "bx")
    plt.xlabel('ra/rb')
    plt.ylabel('p of a winning')
    plt.show()


graph()
