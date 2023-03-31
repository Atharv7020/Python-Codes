#write a program which finds out whether a given name is present in a list or not

names=["damon","stefan","klaus","elijah","marcel"]

name=input("Enter The name to search in list:")

if(name in names):
    print("yes it is in the list")

else:
    print("no it is not in the list")