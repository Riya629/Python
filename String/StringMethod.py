name="riya devkotaH"
# print(name.upper())  throws error beacuse len is inbuilt function not an string methods
print("The length of the string is",len(name))
print("the upper case is",name.upper())
print("The lower case is",name.lower())
print("The replace name is",name.replace("riya","pabitra"))
print("The split of ",name.split())
print("The strip of name is",name.strip())
print("The index of name is", name.find("y"))
print("The capitalized of name is",name.capitalize())
print("The title of name is",name.title())
print("The number of repetation of a is", name.count("a"))
digit="123" #it doesnot check the datatype it chech content inside it
print(digit.isdigit())
alpha="yoyo"
print(alpha.isalpha())
mix="123yo"
print(mix.isalnum())
print(name.endswith("ta",10,12))
print(name.find("i"))
print(name.index("a"))
print(name.islower()) # IF one letter is also cappital it will return false
print(name.isupper())
print(name.swapcase()) # conert caiptal into small and vice versa
print(name.center(60,"*"))
nam='            '
print(nam.isspace()) #for space only not in space between text
print(name.isspace())
print(name.isprintable())