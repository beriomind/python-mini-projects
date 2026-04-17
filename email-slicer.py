# --------------------------------------
# - Email Slicer (email-slicer.py)
# - Version 1
# --------------------------------------

print(" ================ ")
print(" = Email Slicer = ")
print(" ================ ")

email = input("#~ Type an Email : ")

if '@' not in email:
    print("Email Address Does Not Exist!")
else:
    email = email.split('@')
    print(f"Email Username : {email[0]}")
    print(f"Email Domain : {email[1]}")
