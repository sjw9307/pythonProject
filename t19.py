infile = open("/Users/mac/PycharmProjects/pythonProject/texts/proverbs.txt", "r", encoding="UTF8")
ch = infile.read(1)

while ch != "":
    print(ch)
    ch = infile.read(1)
infile.close()