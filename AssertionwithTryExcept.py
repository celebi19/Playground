

"""
   Assertion is a programming concept used while writing a code where 
   the user declares a condition to be true using assert statement prior to running the module. If the condition is True, the control simply moves to
   the next line of code.
"""

try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)
 
# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)