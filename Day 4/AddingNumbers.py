class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
obj = Addition(num1, num2)
print(obj.add())
