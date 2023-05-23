infile = open("/Users/mac/PycharmProjects/pythonProject/texts/grade.txt", "r", encoding="UTF8")

total_grade = 0
count = 0

for line in infile:
    name, grade = line.strip().split()
    if grade.isdigit():
        total_grade += int(grade)
        count += 1

if count:
    print("반 평균 점수 = " + str(total_grade / count))
else:
    print("No valid numeric grades were found in the file.")

infile.close()
