"""Quadratic Identities
Write a menu-driven program using modules to calculate algebraic identities"""

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

# OUTPUT#
'''
    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 1
Enter value of A: 5
Enter value of B: 7
---------------
Answer is 144
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 2
Enter value of A: 10
Enter value of B: 8
---------------
Answer is 4
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 3
Enter value of A: 20
Enter value of B: 13
---------------
Answer is 231
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 4
Enter value of A: 20
Enter value of B: 21
---------------
Answer is 841
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 5
Enter value of A: 3
Enter value of B: 7
---------------
Answer is 1000
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 6
Enter value of A: 9
Enter value of B: 5
---------------
Answer is 64
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 6
Enter value of A: 9
Enter value of B: 4
---------------
Answer is 125
---------------

    --------------------
         Identities     
    --------------------
    | 1. (A+B)**2      |
    | 2. (A-B)**2      |
    | 3. A**2-B**2     |
    | 4. A**2+B**2     |
    | 5. (A+B)**3      |
    | 6. (A-B)**3      |
    | 7. EXIT          |
    --------------------
    
Enter Choice: 7
GOODBYE !
>>> '''
