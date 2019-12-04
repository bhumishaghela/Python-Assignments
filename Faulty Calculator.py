o=raw_input("Which operator do you want to use?")
n1=raw_input("Enter number 1")
n2=raw_input("Enter number 2")
if o=='+':
    r=int(n1)+int(n2)
    if int(n1)==56 and int(n2)==9:
        r=77
    print(r)
elif o=='-':
    r=int(n1)-int(n2)
    print(r)
elif o=='*':
    r=int(n1)*int(n2)
    if int(n1)==45 and int(n2)==3:
        r=555
    print(r)
elif o=='/':
    r=int(n1)/int(n2)
    if int(n1)==56 and int(n2)==6:
        r=4
    print(r)
    
