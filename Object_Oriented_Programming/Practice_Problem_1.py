#Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:

    company="Microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInformation(self):
        print(f"The name of the company is{self.company} and {self.name} is working for the product {self.product}.")



atharv= Programmer("Atharv","Edge")
omkar= Programmer("Omkar","Teams")

atharv.getInformation()
omkar.getInformation()
