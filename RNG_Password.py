import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
symbols = "!@#$%^&*()"

string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string,length))


data = input ("Input the website you would like to generate a password for: ")
print ("")
print ("You new password is:" + password)
print ("")

try:
    f=open('rng_password.txt','a')
    f.write(data)
    f.write(" ")
    f.write(password)
    f.write("\n")
except Exception as e:
    print ("Error:", str(e))
finally:
    f.close()