from db_connection import connect_db
#create 
def add_Employee():
    conn = connect_db()
    cursor = conn.cursor()
    emp_id = input("Enter employee ID: ")
    emp_first_name = input("Enter first name: ")
    emp_last_name = input("Enter last name: ")
    address = input("Enter address: ")
    department = input("Enter department: ")
    project = input("Enter project: ")

    query = """INSERT INTO Employee (emp_id, emp_first_name, emp_last_name, address, department, project) VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (emp_id,
              emp_first_name,
              emp_last_name,
              address,
              department,
              project
              )
    
    cursor.execute(query, values)
    conn.commit()
    print("Employee added successfully!")
    cursor.close()  
    conn.close()

#read
def view_Employees():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM Employee"
    cursor.execute(query)
    employees = cursor.fetchall()
    for emp in employees:
        print(emp)
    cursor.close()  
    conn.close()

#delete
def delete_Employee():
    conn = connect_db()
    cursor = conn.cursor()
    emp_id = input("Enter employee ID to delete: ")
    query = "DELETE FROM Employee WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")
    cursor.close()
    conn.close()

#update
def update_Employee():
    conn = connect_db()
    cursor = conn.cursor()
    emp_id = input("Enter employee ID to update: ")
    email = input("Enter email: ")
    query = """UPDATE Employee SET  email=%s WHERE emp_id=%s"""
    values = (email,
              emp_id
              )
    cursor.execute(query, values)
    conn.commit()
    print("Employee updated successfully!")
    cursor.close()
    conn.close()
while True:
    print('\n Employee Management System')
    print('1. Add Employee')
    print('2. View Employees')
    print('3. Delete Employee')
    print('4. Update Employee')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_Employee()
    elif choice == '2':
        view_Employees()
    elif choice == '3':
        delete_Employee()
    elif choice == '4':
        update_Employee()
    elif choice == '5':     
        print('Thank You')
        break
    else:
        print('Invalid choice. Please try again.')