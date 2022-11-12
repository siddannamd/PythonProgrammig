marks1 = int(input("Enter the first marks: "))
marks2 = int(input("Enter the second marks: "))
marks3 = int(input("Enter the third marks: "))
if marks1<marks2 and marks1<marks3:
    print("Average of best 2 marks: ",(marks2+marks3)/2)
elif marks2<marks1 and marks2<marks3:
    print("Average of best 2 marks: ",(marks1+marks3)/2)
else:
    print("Average of best 2 marks: ",(marks1+marks2)/2)
