infile = open("/texts/sales.txt", "r", encoding ="UTF8")
outfile = open("/texts/result.txt", "w", encoding ="UTF8")

sum = 0
count = 0

line = infile.readline()
while line != "":
    line = int(line)
    sum += line
    count += 1
    line = infile.readline()

# print("총 매출 = " + str(sum) + "\n")
# print("평균 매출 = " + str(sum/count))

outfile.write("총 매출 = " + str(sum) + "\n")
outfile.write("평균 매출 = " + str(sum/count))

infile.close()