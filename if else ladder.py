   
"""
    --- Here, a user can decide among multiple options. 
    The if statements are executed from the top down. 
    As soon as one of the conditions controlling the
    if is true, the statement associated with that if
    is executed, and the rest of the ladder is bypassed.
    If none of the conditions is true,
    then the final else statement will be executed---
"""
    


# Python program to illustrate if-elif-else ladder
#!/usr/bin/python
  
i = -20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")