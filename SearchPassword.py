import pyvariable

data = pyvariable.LocalVariable()
name = input("Enter the name of your password : ")
if data.exists(str(name)):
    print("\nThe password is :  "+data.read(str(name)))
else:
    print("\nThe password couldn't be found")
