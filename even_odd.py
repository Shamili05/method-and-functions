class MyClass:
    def __init__(self, num):
        self.num = num
        
    def even(self):
        if self.num % 2 == 0:
            return "The number {} is  even".format(self.num)
        else:
            return "The number is odd".format(self.num)

n = MyClass(int(input("Enter the number: ")))
print(n.even())
