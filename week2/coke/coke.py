def main():
    amount_due = 50
    coin = 0

    # check for due amount
    while amount_due > coin:
        amount_due = amount_due - coin

        # insert coins
        coin = insert_coin(amount_due)

        # check for coin clears the due amount or not
        if coin > amount_due:
            change_owed = coin - amount_due
        else:
            change_owed = 0

    # print change owed
    print(f"Change Owed: {change_owed}")


def insert_coin(due):
    # prompt user to insert correct coins
    while True:

        # print due amount
        print(f"Amount Due: {due}")

        # insert coins
        coins = int(input("Insert Coin: "))

        # check if inserted coins are correct
        if coins in [5, 10, 25]:
            return coins
        else:
            continue


main()
