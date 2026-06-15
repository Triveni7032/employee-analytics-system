employees = []

while True:
    print("\n===== Employee Analytics System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Salary Analytics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        department = input("Department: ")
        salary = float(input("Salary: "))

        employees.append({
            "ID": emp_id,
            "Name": name,
            "Department": department,
            "Salary": salary
        })

        print("Employee Added Successfully!")

    elif choice == "2":
        for emp in employees:
            print(emp)

    elif choice == "3":
        search_id = input("Enter Employee ID: ")

        found = False
        for emp in employees:
            if emp["ID"] == search_id:
                print(emp)
                found = True
                break

        if not found:
            print("Employee Not Found")

    elif choice == "4":
        if employees:
            salaries = [emp["Salary"] for emp in employees]
            print("Average Salary:", sum(salaries) / len(salaries))
            print("Highest Salary:", max(salaries))
            print("Lowest Salary:", min(salaries))
        else:
            print("No employee data available")

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")