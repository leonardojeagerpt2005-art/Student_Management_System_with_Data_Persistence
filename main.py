#File import is used in main and * is used to call all functions that are in the file
from functions import *
option = None

#cycle that is maintained while the user does not insert 6
while option != 6:
    print("*"*50)
    print("WELCOME TO SYSTEM")
    print("*"*50)

    print("""

    ____________________________________________
    |        WELCOME CHOOSE OPTION             |
    |__________________________________________|
    |[1] registered student                    |
    |[2] check student list                    |
    |[3] Search for a student by some criterion|  
    |[4] Update a student's information.       |
    |[5] Delete students.                      |
    |[6] EXIT.                                 |
    |__________________________________________|
""")
    option = input("Enter the option you wish to perform: ")
    if option == "1":
        registered_students()
    elif option == "2":
        student_consultation()
    elif option == "3":
        student_search()
    elif option == "4":
        update_student()
    elif option == "5":
        delete_student()
    else:
        print("finally system")
        break