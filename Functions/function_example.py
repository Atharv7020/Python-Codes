#Percentage calculator using function

def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5])/600)*100
    return p

marks1=[80,91,93,88,77,97]
percentage1=percent(marks1)

marks2=[90,91,92,89,93,97]
percentage2=percent(marks2)

marks3=[90,91,92,79,88,67]
percentage3=percent(marks3)

print(percentage1,percentage2,percentage3)
