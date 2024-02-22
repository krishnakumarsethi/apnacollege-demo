''' krishna kumar ---> KRIshna kuMAR '''
user=input("Enter the string")
st=user[:3].upper()
end=user[-3].upper()
letter=st+user[3:-3]+end
print(letter)
