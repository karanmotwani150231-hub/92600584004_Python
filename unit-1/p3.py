num1=int(input("enter the numbers"))
num2=int(input("enter the numbers"))

#arithmetic operations
print("addition :",num1+num2)
print("subtraction :",num1-num2)
print("multiplication :",num1*num2)
print("division :",num1/num2)
print("modulo :",num1%num2)

#relational operations
if (num1>num2):
    print("num1 is greater than num2")

if (num1<num2):
    print("num1 is less than num2")

if (num1>=num2):
    print("num1 is greater than equal to num2")
    
if (num1<=num2):
    print("num1 is less than equal to num2")

if(num1!=num2):
    print("num 1 is not equal to num2")

if(num1==num2):
    print("num 1 is equal to num2")

#logical operations

print("num1>5 and num2<10:",num1>5 and num2<10)
print("num1>5 and num2<10:",num1>5 or num2<10)
print("not(num1>5)",not(num1>5))

