#Sum of the given numbers
num = int(input("Enter the total number do you want to enter : "))
sum = 0
for i in range(num):
    a = int(input("Enter the number : "))
    sum = sum + a
    average = sum/num
print("Sum of the given numbers",sum)