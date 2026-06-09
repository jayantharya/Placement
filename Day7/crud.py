from db_connection import connect_db
def add_student():
    conn = connect_db()
    cursor = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")  
    course = input("Enter course: ")
    department = input("Enter department: ")
    admission_date = input("Enter admission date (YYYY-MM-DD): ")
    address = input("Enter address: ")

    query = """INSERT INTO students (first_name, last_name, gender, dob, email, phone, course, department, admission_date, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (first_name,
               last_name,
               gender,
                dob,
                email,
                phone,
                course,
                department,
                admission_date,
                address
                )
    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully!")
    cursor.close()  
    conn.close()



#read
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    print(students)
    #for student in students:
       # print(student)
    cursor.close()
    conn.close()


#delete
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()
    student_id = input("Enter student ID to delete: ")
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted successfully!")
    cursor.close()
    conn.close()


#update
def update_student():
    conn = connect_db()
    cursor = conn.cursor()
    student_id = input("Enter student ID to update: ")
    email = input("Enter email: ")
    query = """UPDATE students SET  email=%s WHERE id=%s"""
    values = (email,
              student_id
              )
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")
    cursor.close()
    conn.close()

while True:
    print('\n Student Management System')
    print('1. Add Student')
    print('2. View Students')
    print('3. Delete Student')
    print('4. Update Student')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        print('Thank You')
        break
    else:
        print('Invalid choice. Please try again.')