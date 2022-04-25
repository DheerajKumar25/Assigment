#Q1 Program to find average of three numbers entered by user

n1=int(input("Enter the number ="))
n2=int(input("Enter the number ="))
n3=int(input("Enter the number ="))
avg=(n1+n2+n3)/3
print("The average of three numbers =",avg)

#Q2 Program to compute a person's income tax

gi=int(input("enter gross income"))
dependent=int(input("number of dependent"))
taxincome=gi-10000-(dependent*3000)
tax=0.2*taxincome  #Tax rate is 20%
print("The person has to pay",tax)

#Q3 Program to store different data types values into a list

n1=int(input("Number of students"))
lts=["Sid","Name","Gender","CourseName","CGPA"]
for i in range(n1):
    nlst=[]
    Sid=int(input("Enter sid:"))
    Name=input("Enter name :")
    Gender=input("Enter the gender:")    #Gender should be F/M and U for unknown
    cname=input("Enter the Course Name:")
    cg=float(input("Enter CGPA:"))
    nlst.append(Sid)
    nlst.append(Name)
    nlst.append(Gender)
    nlst.append(cname)
    nlst.append(cg)
    print(lts)
    print(nlst)

#Q4 Program to enter marks of 5 students into a list and display them in sorted manner

m1=float(input("Enter marks of first student:"))
m2=float(input("Enter marks of second student:"))
m3=float(input("Enter marks of third student:"))
m4=float(input("Enter marks of fourth student:"))
m5=float(input("Enter marks of fifth student:"))
mlst=[m1,m2,m3,m4,m5]
mlst.sort()
print(slst)

#Q5
color=["Red","Green","White","Black","Pink","Yellow"]
color.pop(3)
print(color)
color[3]="Purple"
print(color)