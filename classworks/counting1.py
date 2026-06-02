#wap to count numbers of alphabet in string useing function
def countalpha(text):
    count=0
    for i in text:
        if i.isalpha():
            count=count+1
    return count
text=input("Enter word:")
print(f"The number of aplabhets is {countalpha(text)} ")