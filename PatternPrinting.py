n=int(input("How many times you want to print pattern"))
Boolean=int(input("Type 1 to print from top to bottom and 0 for printing bottom to top"))
if Boolean==1:
    Boolean=bool(Boolean)
else:
    Boolean=bool(Boolean)
if Boolean==True:
    for i in range(1,n+1):
        print(i*"*")
else:
    for i in range(n,0,-1):
        print(i*"*")


