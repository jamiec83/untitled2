def addition(a, b):
    return a + b

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def sqr(a):
    return a * a

def sqrroot(a):
    return a ** .5

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self,a, b):
        self.result = a * b
        return self.result

    def divide(self,a,b):
        self.result = a / b
        return self.result

    def squareroot(self,a):
        self.result = a ** .5
        return self.result

    def square(self,a):
        self.result = a * a
        return self.result

