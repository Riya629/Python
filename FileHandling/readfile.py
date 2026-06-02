#Reading file
file=open('student1.txt', 'r')
content=file.readlines()
for line in content:
    print(line.strip())