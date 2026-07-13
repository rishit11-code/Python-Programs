i=int(input("Enter 1 for long term investment, 2 for short term investment and 3 for FD: "))
if i==1:
   j=int(input("Press 1 Nifty 50, 2 for others: "))
   if j==1:
      f=int(input("Enter Monthly Deduction: "))
      t=int(input("Enter the time period in years (Greater than 12 years): "))
      s=int(input("Enter step up percentage: "))
      p=f*12

      if t<12:
         print("Please enter a time period greater than 12 years")
      else:
         for k in range(1,t+1):
            p=p+p*0.12
            p=p+(f+f*s/100)*12
            f=f+f*s/100
         print("Amount invested is: ",f*12*t)
         print("Retirement corpus after ",t," years is: ",p)
         print("Current value of retirement corpus is: ",p/(1+0.04)**t)
   
   elif j==2:
      f=int(input("Enter Monthly Deduction: "))
      t=int(input("Enter the time period in years (Greater than 12 years): "))
      r=float(input("Enter the estimated rate of interest: "))  
      s=int(input("Enter step up percentage: "))
      if t<12:
         print("Please enter a time period greater than 12 years")
      else:
         for k in range(t):
            p=(p)+(p)*r/100
            p=p+(f+f*s/100)*12
            f=f+f*s/100
         print("Amount invested is: ",f*12*t)
         print("Retirement corpus after ",t," years is: ",p)
         print("Current value of retirement corpus is: ",p/(1+0.04)**t)

elif i==3:
   f=int(input("Amount in FD: "))
   t=int(input("Enter the time period in years: "))
   r=float(input("Enter the rate of interest by Bank: "))
   for k in range(t):
      f=f+f*r/100
   print("Retirement corpus after ",t," years is: ",f)
   print("Current value of retirement corpus is: ",f/(1+0.04)**t)
elif i==2:
   f=int(input("Enter Monthly Deduction: "))
   t=int(input("Enter the time period in years (Less than 12 years): "))
   r=float(input("Enter the estimated rate of interest: "))  
   s=int(input("Enter step up percentage: "))
   p=f*12
   if t>12:
      print("Please enter a time period less than 12 years")
   else:
      for k in range(t):
         p=(p)+(p)*r/100
         p=p+(f+f*s/100)*12
         f=f+f*s/100
      print("Amount invested is: ",f*12*t)
      print("Total Money after ",t," years is: ",p)
      print("Current value of the money is: ",p/(1+0.04)**t)  