#Here we are using open fuction for opening a text file!

f=open("demo.txt",'r')
data=f.read()
print(data)
f.close()  