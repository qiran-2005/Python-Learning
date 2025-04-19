# Problem 2
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subject1 = int(input("Enter subject1 marks: "))
subject2 = int(input("Enter subject2 marks: "))
subject3 = int(input("Enter subject3 marks: "))

avg1 = (subject1/100)*100
print("Subject1 Average: ", avg1)
avg2 = (subject2/100)*100
print("Subject2 Average: ", avg2)
avg3 = (subject3/100)*100
print("Subject3 Average: ", avg3)

totalavg = ((subject1+subject2+subject3)/300)*100
print("Total Average: ", totalavg)

if (avg1 >= 33 and avg2 >= 33 and avg3 >= 33 and totalavg >= 44):
    print("Student has passed in all subjects")
else:
    print("Student has failed")
