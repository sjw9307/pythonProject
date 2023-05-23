infile = open("/Users/mac/PycharmProjects/pythonProject/texts/proverbs.txt", "r", encoding="UTF8")

lines = infile.readlines()
print(lines)

for line in lines:
    print(line)

infile.close()