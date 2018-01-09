from random import randrange


def roll(num, sides):
    rolls = [randrange(sides) + 1 for die in range(num)]
    return rolls
