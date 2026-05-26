# WAP to count number of alphabets in a string using function
def alpha(word):
    count=0
    for char in word:
     if char.isalpha():
        count=count+1
    return count

text=input("Enter word:")
print(f"The number of alphabet is { alpha(text)}")

