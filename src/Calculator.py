def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

class Calculator:
    result = 0




    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self,a, b):
        self.result = a - b
        return self.result

    def multiply(self,a, b):
        self.result = a * b
        return self.result

    def divide(self,a, b):
        self.result = a / b
        return self.result