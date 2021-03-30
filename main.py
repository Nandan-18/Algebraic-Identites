
import identities

while True:
    print("""
    --------------------
    |    Identities    | 
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    """)
    ch = int(input("Enter Choice: "))
    if ch == 7:
        print("GOODBYE !")
        break
    a = eval(input("Enter value of A: "))
    b = eval(input("Enter value of B: "))
    if ch == 1:
        print("---------------")
        print("Answer is", identities.exp1(a, b))
        print("---------------")
    elif ch == 2:
        print("---------------")
        print("Answer is", identities.exp2(a, b))
        print("---------------")
    elif ch == 3:
        print("---------------")
        print("Answer is", identities.exp3(a, b))
        print("---------------")
    elif ch == 4:
        print("---------------")
        print("Answer is", identities.exp4(a, b))
        print("---------------")
    elif ch == 5:
        print("---------------")
        print("Answer is", identities.exp5(a, b))
        print("---------------")
    elif ch == 6:
        print("---------------")
        print("Answer is", identities.exp6(a, b))
        print("---------------")
    else:
        print("WRONG CHOICE !!!")

################################################################################



