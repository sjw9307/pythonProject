infile = open("/Users/mac/PycharmProjects/pythonProject/texts/proverbs.txt", "r", encoding="UTF8")

for line in infile:
    line = line.rstrip()  # 오른쪽 공백 문자를 없앤다.
    word_list = line.split()  # 단어들로 분리한다.
    print(word_list)
    for word in word_list:  # 리스트에 들어 있는 단어들을 출력한Ek
        print(word)

infile.close()
