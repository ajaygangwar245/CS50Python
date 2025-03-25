class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "\U0001f36A" * self.size

    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError
        else:
            self.size = self.size + n

    def withdraw(self, n):
        print(f"Attempting to withdraw {n} size from {self.size} size")
        if n > self.size:
            raise ValueError
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        else:
            self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(4)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
