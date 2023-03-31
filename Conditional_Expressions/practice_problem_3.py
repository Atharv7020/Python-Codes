#A spam comment is defined as text containing following keyword:"Make a lot of money","buy now","Subscribe this".Write a program to detect spam.

text=input("Enter text:")

if(text=="make a lot of money"):
    print("Spam")

elif("buy now" in text):
    print("Spam")

elif("subscribe this" in text):
    print("Spam")

else:
    print("Not spam")