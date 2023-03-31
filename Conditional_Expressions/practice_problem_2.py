#Write a program to find out whether a student is pass or fail,if it requires total 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input from user.

sub1=int(input("Enter the number of marks in sub1:"))
sub2=int(input("Enter the number of marks in sub2:"))
sub3=int(input("Enter the number of marks in sub3:"))

Total=(sub1+sub2+sub3)/3

if(sub1>=33 and sub2>=33 and sub3>=33 and Total>=40):
    print("Passed")
else:
    print("Failed")
