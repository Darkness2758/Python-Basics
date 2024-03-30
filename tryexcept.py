#Try and Except Basic (error handleing)
try:
    a = int(input("Enter your number: "))
    print(a + 3)
except:
    print("some error occured")


#Basic Error output print
try:
    a = int(input("Enter your number: "))
    print(a + 3)
except Exception as e:
    print("some error occured", e)