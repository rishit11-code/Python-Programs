p=int(input ("Press 1 for standard method and 2 for Heron's formula: "))
if p==1:
    i=int(input ("Enter the base of the triangle: "))
    h=int(input ("Enter the height of the triangle: "))
    a=0.5*i*h
else:
    a=int(input ("Enter the first side of the triangle: "))
    b=int(input ("Enter the second side of the triangle: "))
    c=int(input ("Enter the third side of the triangle: "))
    s=(a+b+c)/2
    a=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is: ",a)