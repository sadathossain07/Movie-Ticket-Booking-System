name = input("Enter student name: ")

marks = []
passed_courses = 0

for i in range(5):
    mark = float(input(f"Enter mark of course {i + 1}: "))sadar
    marks.append(mark)


total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)


for mark in marks:
    if mark >= 50:
        passed_courses += 1


if average_marks >= 80:
    performance = "Excellent"
elif average_marks >= 70:
    performance = "Good"
elif average_marks >= 60:
    performance = "Average"
elif average_marks >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"


print("\n--- Student Result ---")
print(f"Name: {name}")
print(f"Total: {total_marks}")
print(f"Average: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Courses: {passed_courses}")
print(f"Performance: {performance} ")