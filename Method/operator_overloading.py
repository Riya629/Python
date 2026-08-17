#Example of operator overloading



class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return (f"{self.i}i+{self.j}j+{self.k}k")
    def __add__(self,a):
        return vector (self.i+a.i, self.j+a.j, self.k+a.k)
        # return (f"{self.i+a.i}i+{self.j+a.j}j+{self.k+a.k}k") this return string value we must convert it in vector
v=vector(1,2,3)
print(v)
v2=vector(4,5,6)
print(v2)
print(v+v2)
print(type(v+v2)) # string so we must convert it in vector