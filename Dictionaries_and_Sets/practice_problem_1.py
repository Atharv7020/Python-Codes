#write a program to create a dictionary of hindi words with values as their english translation.Porovides users with options to look up

mydict={"main":"I",
        "tum":"You",
        "hum":"we"}

print("Select from following options:",mydict.keys())
a=input("Enter from above mentioned keys:")
print("Translation is:",mydict.get(a))