#Write a class calculator capable of finding square,cube and square-root of a number and also show the example of staticmethod.

class calculator:

    def __init__(self,number):
        self.number=number

    def square(self):
        res=self.number*self.number
        print(f"The square of the {self.number} is {res}")

    def cube(self):
        cuberes = self.number * self.number * self.number
        print(f"The cube of the {self.number} is {cuberes}")

    def squareroot(self):
        sqrres=self.number ** 0.5
        print(f"The squareroot of the {self.number} is {sqrres}")

    @staticmethod
    def greet():
        print("Hello and welcome to the best calculator")


operations=calculator(int(input("Enter a number:")))

operations.square()
operations.cube()
operations.squareroot()
operations.greet()