# Problem 2

# Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []

student1 = int(input("Enter Student1 marks: "))
marks.append(student1)
student2 = int(input("Enter Student2 marks: "))
marks.append(student2)
student3 = int(input("Enter Student3 marks: "))
marks.append(student3)
student4 = int(input("Enter Student4 marks: "))
marks.append(student4)
student5 = int(input("Enter Student5 marks: "))
marks.append(student5)
student6 = int(input("Enter Student6 marks: "))
marks.append(student6)

marks.sort()
print(marks)
