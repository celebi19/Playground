def fun():
    S = 0
      
    for i in range(4):
        S += i
        yield S
  
for i in fun():
    print(i)
