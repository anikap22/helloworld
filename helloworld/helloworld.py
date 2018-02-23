import random
import datetime


def helloworld(name=None, howlong=None, countdown=None, cny=None, fortune=None):
    """
    return hello world, or hello {name}
    """

    # print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))

    # print days til Darwin's birthday
    if howlong:
        dday = datetime.datetime(2019, 2, 12)
        diff = dday - datetime.datetime.now()
        print("{} days until Darwin's birthday".format(diff.days))

    # print countdown to armageddon
    if countdown:
        end = random.randint(0, 100)
        print("the world will end in {} days... maybe".format(end))

    # print chinese new year animal
    if cny:
        yr = int(cny)
        base = yr - 1920
        rem = base % 12
        if rem == 0:
            print("you are a monkey")
        elif rem == 1:
            print("you are a rooster")
        elif rem == 2:
            print("you are a dog")
        elif rem == 3:
            print("you are a pig")
        elif rem == 4:
            print("you are a rat")
        elif rem == 5:
            print("you are an ox")
        elif rem == 6:
            print("you are a tiger")
        elif rem == 7:
            print("you are a rabbit")
        elif rem == 8:
            print("you are a dragon!")
        elif rem == 9:
            print("you are a snake")
        elif rem == 10:
            print("you are a horse")
        elif rem == 11:
            print("you are a sheep")

    # print a fortune
    if fortune:
        kids = random.randint(0, 10)
        live = random.randint(0, 100)
        print("you will have {} kids and live for {} years".format(kids, live))
