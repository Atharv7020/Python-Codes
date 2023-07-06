#Write a program to read a text from given file 'poem.txt' and find if the word twinkle is there or not.

f=open('poem.txt','r')
data=f.read()
print(data)
if 'twinkle' in data:
    print("Yes the word is present")
else:
    print("The word is not here")
f.close()
