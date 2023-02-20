#11.    Write a program to intalize a 5 subjects marks and find there average based on the average display grades:
#If average > 75
  #  Distinction
#If average > 60 && average < 75
   # First Class
#If average > 50 && average < 60
  #  Second Class
#If average > 35 && average < 50
    # Third Class
#If average < 35
 #    Fail
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade:F")
    
    
    
    