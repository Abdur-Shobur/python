# class method
class person:
    type = "Human"

    def __init__(self, name):
        self.type = name

    @classmethod
    def getType(arg):
        return arg.type

    @staticmethod
    def getSum(a, b):
        return a+b


print(person.getSum(2, 4))
