import csv

f = open("/Users/mac/PycharmProjects/pythonProject/texts/weather.csv", "r", encoding="UTF8")
# CSV 파일을 열어서 f에 저장.
data = csv.reader(f)
header = next(data) #헤더부분 패스
temp = -999

for d in data:
    if temp < float(d[4]):
        temp = float(d[4])
print('가장 더웠던 날은', temp, '입니다')

f.close()
