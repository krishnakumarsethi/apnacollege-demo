''' krishna kumar ---> KrIsHnA KuMaR '''
user=input("Enter the string").split()
for i in user:
    i=i.capitalize()
    for j in range(len(i)):
        if j%2==0:
            j=i[j].upper()
        else:
            j=i[j].lower()
        print(j,end=" ")
