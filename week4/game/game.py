import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            num = random.randint(1, level)
            guess(num)
        except ValueError:
            pass


def guess(n):
    while True:
        try:
            guessNum = int(input("Guess: "))
            if guessNum > n:
                print("Too large!")
                raise ValueError
            elif guessNum < n:
                print("Too small!")
                raise ValueError
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


main()
