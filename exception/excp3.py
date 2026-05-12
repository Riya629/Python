
#example of index error
num=[2,4,6,7,9]
try:
    indx=int(input("Enter the index position:"))
    print(num[indx])
except IndexError:
    print("Index error")


