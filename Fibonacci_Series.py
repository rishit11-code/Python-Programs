i=int(input("Enter the number of terms: "))
j=int(input("Enter the first term: "))
k=int(input("Enter the second term: "))
for l in range(i):
    print(j,end=" | ")
    j=k
    k=j+k