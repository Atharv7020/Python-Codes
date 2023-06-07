#Write a program to print a table of entered number using function.

def multi(value):
    for i in range(1,11):
        print(value,"*",i,"=",value*i)


number=int(input("Enter a number:"))
table=multi(number)






