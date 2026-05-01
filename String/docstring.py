# so basically docstring are written inside the triple """ or '''
#It is used as a documentation too  string is written inside triple """
#It help programmers to understand what code is doing
#It is simple way to describe what code does
#It can  be access using (.__doc__) double underscore at front and double undeerscore at back.

def add(a,b):
    """Return the sum of two  numbers""" # docstring is written just after the function declaration if is it written in orther place it will return non it will be comment no doctring
    return a+b
sum=add(2,3)
print(sum)
# help(add) not operable it doesnot works here
print((add.__doc__))# it return the Doctring we write