import random


def main():
    level = get_level()
    score = 10
    wrong = 0

    for _ in range(10):
        digit1 = generate_integer(level)
        digit2 = generate_integer(level)
        sum = digit1 + digit2
        passVal = 0
        while passVal < 3:
            try:
                ans = int(input(f"{digit1} + {digit2} = "))
                if ans == sum:
                    break
                else:
                    raise ValueError
            except ValueError:
                passVal += 1
                if passVal != 3:
                    print("EEE")
                elif passVal == 3:
                    print(f"{digit1} + {digit2} = {sum}")
                    wrong += 1
                    break
                pass

    # score
    score = score - wrong
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
