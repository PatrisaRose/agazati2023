import random


def szam():
    print("I/A:")
    vel = int(random.random()*50)+1
    print(f"\tA generált szám: {vel}")
    print("I/B:")
    if vel % 5 == 0:
        if vel % 3 == 0:
            print("\tA szám öttel és hárommal is osztható!")
        else:
            print("\tA szám öttel osztható!")
    elif vel % 3 == 0:
        print("\tA szám hárommal  osztható!")
