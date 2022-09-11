import random


def wuerfel():
    zahl = random.randint(1, 6)
    print(zahl)
    retry()


def retry():
    answer = input("Would you like to try again? (Y/n): ")
    if answer.lower() == "n":
        return
    else:
        wuerfel()


wuerfel()
