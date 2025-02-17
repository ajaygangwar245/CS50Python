def main():
    exp = input("Expression: ").strip()

    x, y, z = exp.split(" ")

    if y == "/" and z == "0":
        return 0

    match y:
        case "+":
            print(round(float(x) + float(z), 1))
        case "-":
            print(round(float(x) - float(z), 1))
        case "*":
            print(round(float(x) * float(z), 1))
        case "/":
            print(round(float(x) / float(z), 1))
        case _:
            print("Invalid")


main()
