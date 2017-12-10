#to check if the passords match or not

password = 1234

def fun(pw):

    if (pw == password):
        print("Passwords match.")
    else:
        print("Wrong password.")

pw = (input("Enter a password:"))

fun(pw)