#char frequency using dict
"""
s = input()
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print("Char frequency:",d)




"""
"""

#checking the  given username and password are matched or not

d={}
for i in range(3):
    username=input()
    password=int(input())
    d[username]=password
userlogin=input()
passwordlogin=int(input())
if userlogin in d:
    if d[userlogin]==passwordlogin:
        print("matched")
else:
    print("not matched")



"""
"""

#function

def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()
    
"""

#function with parameters with return type

"""
def add(a,b):             #parameters
    return a+b
x=add(3,4)                  #arguments
print(x)

"""

#function with parameters without return type
"""
def add(a,b):                       #parameters
    print(a+b)
add(5,6)    

"""


#function without parameters with return type

"""
def add():
    a=int(input())
    b=int(input())
    return a+b
x=add()
print(x)
"""


#function withoutparameters without retun type
"""
def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()

"""

"""



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
while True:
    print("1.Add,2.Sub,3.Mul,4.Div")
    i=int(input("Enter the choice:"))
    if i==1:
        n1=int(input())
        n2=int(input())
        x=add(n1,n2)
        print(x)
    elif i==2:
        n1=int(input())
        n2=int(input())
        x=sub(n1,n2)
        print(x)
    elif i==3:
        n1=int(input())
        n2=int(input())
        x=mul(n1,n2)
        print(x)
    elif i==4:
        n1=int(input())
        n2=int(input())
        x=div(n1,n2)
        print(x)
    else:
        print("invalid")
        break
        




"""









