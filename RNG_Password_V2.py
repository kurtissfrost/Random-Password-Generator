import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
symbols = "!@#$%^&*()"

length = 0
while length < 8 or length  > 16:
    string = lower + upper + numbers + symbols
    length = int(input("How many characters would you like to use? "))
    print ("\n")
    if length >= 8 and  length <= 16:
        password = "".join(random.sample(string,length))
    else:
        print ("Choose a number between 8 & 16.")

    

data = input ("Input the website you would like to generate a password for: ")
print (" ")
print ("You new password is:" + password + "\n")

try:
    f=open('master.txt','a')
    f.write(data)
    f.write(" ")
    f.write(password)
    f.write("\n")
except Exception as e:
    print ("Error:", str(e))
finally:
    
    f.close()