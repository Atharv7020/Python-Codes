#write a program to accept marks from six students and display them in sorted manner45

m1=int(input("Marks of student 1:"))
m2=int(input("Marks of student 2:"))
m3=int(input("Marks of student 3:"))
m4=int(input("Marks of student 4:"))
m5=int(input("Marks of student 5:"))
m6=int(input("Marks of student 6:"))

mark_list=[m1,m2,m3,m4,m5,m6]
mark_list.sort()

print(mark_list)
