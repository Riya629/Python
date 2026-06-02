#writing into file
file=open('student1.txt','w')
# content=file.write("Hello BCA")
# file.close()
for i in range(2):
    name=input("Enter name::")
    age=int(input("Enter age::"))
    address=input("Enter address::")
    # file.write(name+"\n")
    # file.write(str(age)+"\n")  #write only accept string text
    # file.write(address+"\n")
    file.write(f"NAME:{name}\n AGE:{age}\n ADDRESS:{address}\n")
file.close()