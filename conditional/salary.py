salary=int(input("Enter your salary: "))
salary=salary*12
insurance=int(input("Enter insurance"))
pf=salary*0.1
Taxable_salary=salary-pf-insurance
if(Taxable_salary<=600000):
    Tax=Taxable_salary*0.01
elif(Taxable_salary<=800000):
    Tax=6000+(Taxable_salary-600000)*0.1
elif(Taxable_salary<=1100000):
    Tax=6000+20000+(Taxable_salary-800000)*0.2
else:
    Tax=6000+20000+60000+(Taxable_salary-1100000)*0.3
print("The tax you have to pay is",Tax)