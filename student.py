#create a database
student_database = []
#adding new student and store 
def add_student():
    full_name = input("your name:")
    age = input("your age:")
    academic_year = input("academic year:")
    no_of_courses = input("number of courses:")
    student_list = {
        'full_name': full_name,
        'age' : age,
        'academic_year' : academic_year,
        'no_of_courses' : no_of_courses
    }
    student_database.append(student_list)
    print("student added successfully")
#add_student()
#display all student info
def display() : 
    print('Student Information')
    for student_list in student_database:
        print(f"Name: {student_list['full_name']}")
        print(f"Age: {student_list['age']}")
        print(f"Academic year : {student_list['academic_year']}")
        print(f"no of courses : {student_list['no_of_courses']}")
#display a student info
def search():
    search_name = input('enter a student name you want to search')
    for student_list in student_database:
        if student_list['full_name'] = search_name:
        print(f"Name: {student_list['full_name']}")
        print(f"Age: {student_list['age']}")
        print(f"Academic year : {student_list['academic_year']}")
        print(f"no of courses : {student_list['no_of_courses']}")
# update student data
def update():
    search_name = input('enter a student name you want to update')
    for student_list in student_database:
        if student_list['full_name'] = search_name:
            new_name = input('your name')
            student_list['full_name'] = new_name
            new_age = input("your age:")
            student_list['age'] = new_age
            new_academic_year = input("academic year:")
            student_list['academic_year'] = new_academic_year
            new_no_of_courses = input("number of courses:")
            student_list['no_of_courses'] = new_no_of_courses
#delete student information
def delete():
    search_name = input('enter a student name you want to delete')
    for student_list in student_database:
        if student_list['full_name'] = search_name:
           student_database.remove(student_list)
def main():
    while True:
        print("Student Database")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
student_database = []
main()
