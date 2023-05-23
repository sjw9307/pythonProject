import os
cwd = os.getcwd()
files = os.listdir()

count_pyfiles = 0

for name in files:
    if os.path.isfile(name):
        if name.endswith(".py"):
            count_pyfiles = count_pyfiles + 1
            print(name)

print(count_pyfiles, ".py files has been detected")
