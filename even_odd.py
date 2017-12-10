#to determine if the input given y the user is an even num or an odd num

def fun(num):
    if (num % 2) ==0:
        print("{} is an even number." .format(num))
    else:
        print("{} is a odd number." .format(num))
num= int(input("Enter an integer:"))
fun(num)
