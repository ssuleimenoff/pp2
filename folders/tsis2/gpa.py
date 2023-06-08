n = int(input())
a = 0
gpa = 0
curr = 0
acc = 0
while a < n:
    credit = int(input())
    points = float(input())
    curr += float(points * credit)
    a += 1
    acc += credit
total = float(curr / acc)
if total >= 95:
    gpa = 4.00
elif total >= 85:
    gpa = 3.67
elif total >= 80:
    gpa = 3.0
elif total >= 75:
    gpa = 2.67
elif total >= 70:
    gpa = 2.33
print(gpa)