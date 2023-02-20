the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  
BMI = the_weight / (the_height/100)**2  
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("Eee! You are overweight.")  
else:  
    print("Seesh! You are obese.")  
