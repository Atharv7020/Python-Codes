#Write a program to calculate the grade of a student from his marks from the following scheme

marks=int(input("Enter your marks:"))

if(marks>=90 and marks<=100):
    Grade="Excellent"

elif(marks>=80 and marks<90):
    Grade="A"

elif(marks>=70 and marks<80):
    Grade="B"

elif(marks>=60 and marks<70):
    Grade="C"

elif(marks>=50 and marks<60):
    Grade="D"

elif(marks<50):
    Grade="Fail"

print("Your Grade Is:",Grade)