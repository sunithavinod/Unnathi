day=input("Enter Which day would you like to check in the week?1,2,3,4,5,6,7:")
match day:
    case"1":
        print("Result of the day is Sunday") 
    case"2":
        print("Result of the day is Monday") 
    case"3":
        print("Result of the day is Tuesday") 
    case"4":
        print("Result of the day is Wednesday") 
    case"5":
        print("Result of the day is Thursday") 
    case"6":
        print("Result of the day is Friday") 
    case"7":
        print("Result of the day is saturday")
    case _:
        print("Invalid input")
