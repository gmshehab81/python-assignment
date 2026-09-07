# -- Student Grade Calculator

name = input("enter your name:")
subject1 = float(input("enter your first subject marks:"))
subject2 = float(input("enter your second subject marks:"))
subject3 = float(input("enter your third subject marks:"))

total = subject1 + subject2 + subject3
average = total / 3

# Determines the grade using:

if average >= 80 and average <= 100:
    grade = "A+"
elif average >= 70 and average <= 79:
    grade = "A"
elif average >= 60 and average <= 69:
    grade = "B"
elif average >= 50 and average <= 59:
    grade = "C"
else:
    grade = "F"
    
print("-- student grade report --")
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")


