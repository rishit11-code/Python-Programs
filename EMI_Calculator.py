c=int(input("Press 1 for Credit Cards/Monthly rate and 2 for Loans/Yearly rate: "))
if c==1:
    p=int(input("Enter the principal amount: "))
    r=float(input("Enter the rate of interest: "))
    t=int(input("Enter the time period in months: "))
    emi=(p*r*(1+r)**t)/((1+r)**t-1)
    print("The EMI is: ",emi)
elif c==2:
    p=int(input("Enter the principal amount: "))
    r=float(input("Enter the rate of interest: "))
    t=int(input("Enter the time period in years: "))
    emi=(p*r*(1+r)**t)/((1+r)**t-1)
    print("The EMI is: ",emi)