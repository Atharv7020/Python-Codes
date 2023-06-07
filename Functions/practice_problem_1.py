#Write a program using function to find greatest of three numbers.

def greatest(value1,value2,value3):
    if(value1>value2):
        if(value1>value3):
            return value1
        else:
            return value3

    if(value2>value3):
        if(value2>value3):
            return value2
        else:
            return value3

greatest_number=greatest(109,120,115)
print(greatest_number)