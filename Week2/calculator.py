class Calculator:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def add(self):
        return self.val1+self.val2
    
    def subtract(self):
        return self.val1-self.val2
    
    def multiply(self):
        return self.val1*self.val2
    
    def divide(self):
         if self.val2!=0:
            return self.val1/self.val2
       
print("Welcome to Calculator")
print("Enter 2 numbers to perform opertion:")
x=int(input(" nums1: "))
y=int(input(" num2: "))
calc= Calculator(x,y)
op=input("Enter Operation:(+,-,*,/) : ")
if len(op)==1:
    if op=='+':
        print(calc.add())
    elif op=='-':
        print(calc.subtract())
    elif op=='*':
        print(calc.multiply())
    elif op=='/':
        print(calc.divide())

    