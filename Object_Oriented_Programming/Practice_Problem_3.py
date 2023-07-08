#Create a class with a class attribute a; create a object from it and set a directly using object.a=0.Does that change the class attribute.

class Test:
        a=45


check=Test()
check.a=56
print(check.a)
print(Test.a)

#No.It won't change class attribute