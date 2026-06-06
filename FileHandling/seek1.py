with open('employee.txt','w') as file:
    file.write("Hillo world")
    file.seek(3)
    file.write("He")
    file.truncate()
    file.flush()

    # with open('employee.txt','r') as file:
    #     file.seek(3)
    #     Tell= file.tell()
    #     content=file.read()
    #
    #     print(content)
    #     print(Tell)