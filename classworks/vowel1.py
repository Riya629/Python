#WAP to count number of vowel in string using string
# def countvowel(text):
#     vowel="AEIOUaeiou"
#     count=0
#     for letter in text:
#         if letter in vowel:
#             count=count+1
#     return count
# text=input("Enter letter")
# print(f"The number of vowel in entered lettter is{countvowel(text)}")

# #WAP to search elements in list
# def search():
#     fruit=["APPLE","BANANA","mango"]
#     if "APPLE" in fruit:
#         print("yes there is APPLE in list")
#     else:
#         print("NO there is no APPLE in list")
# search()

def search(element):
    for i in list:
        if(element==i):
            return True

    return False

list=[2,3,4,5]
element=int(input("Enter the integer numbers:"))
if search(element):
    print("element is inside list")
else:
    print("elemnt is not inside list")