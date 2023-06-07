#Write a program to convert temprature from celcius to farenhit using function.

def farenhit(celcius):
    conversion=(celcius*9/5)+32
    return conversion

celsious_input=int(input("Enter the celcius:"))
celsious=farenhit(celsious_input)

print("The conversion of",celsious_input,"°C into farenhit is",celsious,"°F")


