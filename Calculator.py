def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def divide(x,y):
    return (x//y)

print("Select Operation")
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")

selected_op = input()
print("Enter first numbers")
num_1=int(input())
print("enter second number")
num_2=int(input())

if selected_op=="a":
    print(num_1 + num_2)
#prints answer for addition
    
if selected_op=="b":
    print(num_1-num_2)
#prints answer for subtraction
    
if selected_op=="c":
    print(num_1*num_2)
#prints answer for multiplication

if selected_op=="d":
    print(num_1//num_2)
#prints answer for division
