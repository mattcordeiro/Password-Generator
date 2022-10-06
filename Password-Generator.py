import random

print("Welcome to your personal password maker.")
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+123456789,./?><|'

number = input("How many passwords are you looking to make today?")
number = int(number)

length = input("How long do these passwords have to be ?")
length = int(length)

for pwd in range(number):
   passwords = ''
   for c in range(length):
      passwords += random.choice(char)
   print("Your password is:")
   print(passwords)