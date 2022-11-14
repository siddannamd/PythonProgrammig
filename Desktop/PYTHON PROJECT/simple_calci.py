operation = input("sum,difference,multiply,divide : ")
if operation == "sum" :
    a=int(input("first value : "))
    b=int(input("second value : "))
    res=a+b
    print("\n",res)
elif operation =="divide" :
    a = int(input("first value : "))
    b = int(input("second value :"))
    res = a/b
    print("\n", res)
elif operation == "multiply":
    a=int(input("First value : "))
    b=int(input("Second value : "))
    res=a*b
    print("\n",res)
elif operation == "difference":
    a=int(input("First value : "))
    b=int(input("Second value : "))
    res=a-b
    print("\n",res)
