import random
print("-------------------")
print("PASSWORD GENERATOR")
print("--------------------------------------------------------")
print("**** Note Above (15) Is The Secure Length Of A Password ****")
print("--------------------------------------------------------")
print("Created By Aravind.G")
print("--------------------")
print("Find Me At https://instagram.com/aravind.ceh")
print("--------------------------------------------")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "{}[]()!@#$%^&*.,/';?><:_-=+"
length = int(input("Enter Your Password Length:"))
all = lower+upper+numbers+symbols
length = length
password = "".join(random.sample(all,length))
print("Your Password Is ->",password)
print("-----------------------------------------")
print("Thank You For Using My PASSWORD GENERATOR")
print("-----------------------------------------")
