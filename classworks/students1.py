Students={}
for i in range(0,2):
    name=input("Enter name of  students:")
    Students[name]={
    "web":input("Enter grade of web:"),
    "DSA":input("Enter grade of dsa:"),
    "OS":input("Enter grade of os:"),
    "SAD":input("Enter grade of sad:"),
    "JAVA":input("Enter grade of java:")
    }
def calculategpa(grade):
    if grade=="A":
        return 4.0
    elif grade=="A-":
        return 3.7
    elif grade=="B":
        return 3.2
    elif grade=="B-":
        return 2.9
    else:
        return False