name="riya devkota "
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
