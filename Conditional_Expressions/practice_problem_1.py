#Write a program to find greates of four numbers entered by user.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
d=int(input("Enter the forth number:"))

if(a>b and a>c and a>d):
    print(a,"is greater number")

elif(b>a and b>c and b>d):
    print(b,"is greater number")

elif(c>b and c>a and a>d):
    print(c,"is greater number")

elif(d>b and d>c and d>a):
    print(d,"is greater number")

