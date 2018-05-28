from random import randrange


def roll(sides, num_die=1):
    rolls = [randrange(1, sides) for die in range(num_die)]
    return rolls


def main():
    die = input("Which die and how many? E.g. 1d8\n>>>  ")
    num_die, sides = die.split("d")
    try:
        num_die = int(num_die)
        sides = int(sides)
    except:
        print("Error!")
    result = roll(num_die, sides)
    print("You rolled {} and got {}".format(die, result))


if __name__ == "__main__":
    while True:
        main()
