print("Hey, I am Mr. Cal-c \n What mathametical operation do you want me to perform")
operation=input("sum,difference,multiply,devide: ")
if operation == "sum":
    a=int(input("First value= "))
    b=int(input("Second value= "))
    res=a+b
    print("\n",res)
elif operation == "multiply":
    a=int(input("First value= "))
    b=int(input("Second value= "))
    res=a*b
    print("\n",res)
elif operation == "devide":
    a=int(input("First value= "))
    b=int(input("Second value= "))
    res=a/b
    print("\n",res)
elif operation == "difference":
    a=int(input("First value= "))
    b=int(input("Second value= "))
    res=a-b
    print("\n",res)