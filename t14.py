infile = open("/Users/mac/PycharmProjects/pythonProject/texts/test.txt", "r", encoding = "UTF8")
line = infile.readline()
outfile = open("/Users/mac/PycharmProjects/pythonProject/texts/test.txt", "w", encoding = "UTF8")
outfile.write("this line has been addad at 05 / 16 / 16:48\n")

while line != "":
    print(line)
    line = infile.readline()
