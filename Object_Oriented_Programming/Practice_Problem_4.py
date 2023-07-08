#Write a class Train which has methods tvo book a ticket,get status and get fare information of trains running under Indian railways.

class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"The name of the railway is {self.name}")
        print(f"The seats available in train are:{self.seats}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Congratulations your ticket has been booked.Your seat number is{self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry seats are not available.")

    def value(self):
        print(f"The price of the fare is Rs.{self.fare}")




control=Train("Bullet Train",400,200)
control.getStatus()
control.value()
control.bookTicket()
control.getStatus()
