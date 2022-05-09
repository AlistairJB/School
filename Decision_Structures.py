#place a hashtag in front of the line will make it not execute 
#this is referred to as as "comment"

'''
line 1 of comment
line 2 of comment
line 3 of comment
'''

"""
line 1 of comment
line 2 of comment
line 3 of comment
"""

"""
Comparison

> Greater than
< Less than
>= Greater or equal to
<= Less or equal to
== Equal to
!= Not equal to
"""

Mark=int(input("Enter your test mark: "))
print(Mark)

if Mark >= 90:
    print("You aced it!")
    
elif Mark >= 70:
    print("You got a B")
    
elif Mark >= 60:
    print("You got a C")
    
elif Mark >= 50:
    print("You got a D")
    
elif Mark < 50 and Mark >0:
    print("You Failed!")
    
if Mark < 0 and Mark <100:
    print("That mark is invalid")
    
