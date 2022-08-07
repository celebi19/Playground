
""""
Assertion is a programming concept used while writing a 
code where the user declares a condition to be true using 
assert statement prior to running the module. If the
condition is True, the control simply moves to the next 
line of code.
"""
# initializing list of foods temperatures
batch = [ 40, 26, 39, 30, 25, 21]
 
# initializing cut temperature
cut = 26
 
# using assert to check for temperature greater than cut
for i in batch:
    assert i <= 26, "Batch is Rejected"
    print (str(i) + " is O.K" )