#WAP to count number of Digits in an integer using function

def countdigit(number):
    return len(str(number))

number=int(input("Enter number:"))
print(f"The number of digit is{countdigit(number)}")

