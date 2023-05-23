import os

directory = "/Users/mac/PycharmProjects/pythonProject/texts/"
files = os.listdir(directory)

cnt = 0

for name in files:
    full_path = os.path.join(directory, name)
    if os.path.isfile(full_path):
        with open(full_path, 'r', encoding="UTF8") as f:
            for line in f:
                if 'Python' in line:
                    cnt = cnt + 1
                    print(f"File: {name}\nLine: {line}")

print(cnt)
