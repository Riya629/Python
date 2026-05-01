#Programs using string formatter

text="Hello my name is {} and Iam from  {} "
name="Riya"
country="Nepal"
print(text.format(name,country))


# but if we replace the order
text="Hello my name is {1} and Iam from  {0} "
name="Riya"
country="Nepal"
print(text.format(country,name)) #mismatched occured so we can give index value