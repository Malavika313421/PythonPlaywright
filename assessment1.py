
def grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    sid = int(input("Student ID: "))
    name = input("Student Name: ")
    py = int(input("Python Marks: "))
    sql = int(input("SQL Marks: "))
    ai = int(input("AI Marks: "))

    total = py + sql + ai
    avg = total / 3

    student = {
        "id": sid,
        "name": name,
        "total": total,
        "avg": avg,
        "grade": grade(avg),
        "result": "PASS" if avg >= 40 else "FAIL"
    }

    students.append(student)

print("\n===== Student Result =====")

for s in students:
    print("\nStudent ID:", s["id"])
    print("Name:", s["name"])
    print("Total:", s["total"])
    print("Average:", round(s["avg"], 2))
    print("Grade:", s["grade"])
    print("Result:", s["result"])


highest = max(students, key=lambda x: x["avg"])
print("\nHighest Scoring Student:", highest["name"])
top_students = [s["name"] for s in students if s["avg"] > 75]
print("Students above 75:", ", ".join(top_students))