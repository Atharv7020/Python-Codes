#Write a program to print multiplication table of given number using for loop.

num=int(input("Enter any number:"))

for i in range(1,11):
    multiplication=num*i
    print(str(num)+"x"+str(i)+"="+str(multiplication))