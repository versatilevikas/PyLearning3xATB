#1. Leap Year Checker:
year= int(input("input ="))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap year")
    elif year%4==0:
        print("Leap year")
else:
    print("Not a leap year")

#2.. Triangle Classifier
s1=float(input("Side 1"))
s2=float(input("Side 2"))
s3=float(input("Side 3"))

if s1==s2==s3:
    print("eq")
elif s1==s2 or s2==s3 or s1==s3:
    print("Iso")
else:
    print("Scalene")

#Task - Fibonacci series and Factorial

no=int(input("enter the number: "))
val=1
for i in range(1,no+1):
    val=val*i
print(val)




