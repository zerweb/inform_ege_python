A,B,C=  True,False,True
result = (A and B) and (C or B) == (not C)
print(result)