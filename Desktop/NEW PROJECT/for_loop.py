# finding the sum of first "n" whole numbers using for loop
endpoint = int(input("Enter the value of n: "))
sum_of_numbers = 0
for i in range(endpoint):
    print("sum of numbers value is :",sum_of_numbers)
    print("index i value is :",i)
    sum_of_numbers = sum_of_numbers + i
print("The sum of first {} Whole numbers is {}".format(endpoint, sum_of_numbers))

#finding the sum of numbers between a given range (start point, endpoint)
start_point = int(input("Enter the start point :"))
endpoint = int(input("Enter the endpoint :"))
sum_of_numbers = 0
for i in range(start_point, endpoint,):
    sum_of_numbers = sum_of_numbers + i
print("The sum of numbers between {} and {} is {}".format(start_point, endpoint, sum_of_numbers))

