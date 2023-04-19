#Write a program to check the entered number is prime or not

num=int(input("Enter the number:"))
Prime=True

for i in range(2,num):
    if(num%i==0):
      Prime=False
      break

if Prime:
    print("Number is prime")

else:print("Number is not prime")
