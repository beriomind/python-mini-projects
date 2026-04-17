import random

print(" ====================== ")
print(" = Password Generator = ")
print(" ====================== ")

data = "QWERTYUIOPASDFGJKLZXCVBNMqwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
print("qwertyuiopasdfgjklzxcvbnm".upper())
try:
    password_len = int(input("#~ Type the password length : "))
    password = ''.join(random.sample(data, password_len))
    print(f"Password : {password}")
except ValueError:
    print("Password length must be an integer")

