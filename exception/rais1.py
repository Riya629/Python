# try:
#      age=int(input("Enter your age:"))
#      if(age<16 or age>75):
#       raise ValueError("Not a suitable age")
#      else:
#         print("Its suitable age")
# except ValueError as e:
#     print(e)
try:
   a=int(input("Enter a number:"))
   if(a<5 or a>9):
      raise ValueError("Number should be between 5 and 9")
   else:
      print("you eneterd the correct age")
except ValueError as e:
   print(e)