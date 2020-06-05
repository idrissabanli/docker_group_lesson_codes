
class CustomInt(int):
    value = None

    def __init__(self, x):
        self.value = x

    def __add__(self, value):
        return self.value + value

    def __str__(self):
        return self.value + 1

a = CustomInt(1)

print(a + 1)

a = a + 1

print(a)
