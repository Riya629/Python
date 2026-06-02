with open("student2.txt", "w") as file:
    number = int(input("How many records:: "))
    for i in range(number):
        name = input("Enter name:: ")
        age = int(input("Enter age:: "))
        address = input("Enter address:: ")
        file.write(f"NAME:{name}\n AGE:{str(age)}\n ADDRESS:{address}\n")
print("Records entered sucessfully")
