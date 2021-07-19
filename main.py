import os

#os.system("tree")
get = input("what is text-- ")

f= open("test.txt","w+")
f.write(get)

f.close() 

os.system("python -m texttohtml.convert test.txt -o test.html")

