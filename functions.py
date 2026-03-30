# list that keeps the student record
students_list =[]

#function that creates the student record 
def registered_students():
    try:

        print("="*50)
        print("welcome to register students")
        print("="*50)

        student_id = int(input("Enter to ID: "))
        print("-"*50)
        student_name = input("Enter to name: ")
        print("-"*50)
        student_age = int(input("Enter to age: "))
        print("-"*50)
        student_course = input("Enter to course: ")
        print("-"*50)
        student_status = bool(input("Ente tu status True/False: "))
        print("✅ student successfully registered")
        print("="*50)
    except Exception:
        print("error: valor inavlido ingrese el tipo de dato correcto")
        student = {
            "id": student_id,
            "name": student_name,
            "age": student_age,
            "course": student_course,
            "status": student_status
        }
        students_list.append(student)
        print("="*50)
        return student

# function that displays registered students
def student_consultation():
    print("="*50)
    print("welcome to consult student")
    print("="*50)

    if not students_list:
        print("There are no registered students")
    else:
        for student in students_list:
            print(f"id: {student['id']}, name: {student['name']}, age: {student['age']}, course: {student['course']}, status: {student['status']}")
            print("-"*50)

# Function that searches for students using their ID
def student_search():
    print("="*50)
    id_search = int(input("enter the id a search"))
    for student in students_list:
        if student["id"] == id_search:
            print("student found")
            print(f"id: {student['id']}, name: {student['name']}, age: {student['age']}, course: {student['course']}, status: {student['status']}")
        return student
    print("ERROR. Student not found")
    return None

# Function that updates the student record using the ID
def update_student():
    print("="*50)
    id_search = int(input("Enter the student ID to update"))
    for student in students_list:
        if student["id"] == id_search:
            print("Leave blank if you do not wish to change the data")
            student["id"] = input(f"new id ({student['id']}):") or student["id"]
            student["name"] = input(f"new name ({student['name']}):") or student["name"]
            student["age"] = input(f"new age ({student['age']}):") or student["age"]
            student["course"] = input(f"new course ({student['course']}):") or student["course"]
            student["status"] = input(f"new status ({student['status']}):") or student["status"]
            print("fully updated data")
        else:
            print("ERROR. Student ID not found")
            return False

# Function that deletes the student record using the ID
def delete_student():
    print("="*50)
    id_search = int(input("Enter the ID of the student to be deleted: "))
    for student in students_list:
        if student["id"] == id_search:
            students_list.remove(student)
            print("student successfully eliminated")
            return True 
        else:
            print("It was not possible to delete the id, it does not exist")
            return False