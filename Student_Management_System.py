students = []
while True :
    print("Press 1 to ADD STUDENT")
    print("Press 2 to DELETE STUDENT")
    print("Press 3 to SEARCH STUDENT")
    print("Press 4 to EDIT STUDENT")
    print("Press 5 to EXIT STUDENT")
    print("Press 6 to PRINT ALL STUDENT")
    option = input("Enter 1-6 :")

    if option == '1' :
        roll_number = int(input("Enter rollno of student :"))
        students.append(roll_number)
        student  = {}
        student["name"] = input("enter student name")
        student["father name"] = input("enter Father Name ")
        student["age"] = input("enter students age")
        student["address"] = input("enter students address")

        students.append(student)

    elif option =='3' :

        your_rollno=int(input('Your no'))
        # roll no us say pahlay wala nuimber do jaisay first dict k liya us say pahla wala roll no 0 diya
        student_current_index = students.index(your_rollno) +1
        print( 'students curent index is:' , student_current_index )

        print(students[student_current_index])


    elif option == '2' :
        student_roll_number = int(input("Enter roll number of Student you want to Delete : "))
        del students[student_roll_number]

    elif option =='6' :
        print('\n\n')
        print(students)

    elif option =='5':
        break


    elif option == '4':

        student_rollnumber = int(input('Enter roll number of student :'))


        while True :
            print("Press 1 to Edit Name")
            print("Press 2 to Edit Father name")
            print("Press 3 to Edit age")
            print("Press 4 to Edit Address")
            print('Press 5 to exit')
            opt = input("Enter 1-5 :")

            if opt == '1':
                students[student_rollnumber]['name'] = input("enter new name :")
            if opt == '2':
                students[student_rollnumber]['father name'] = input("enter new father name :")
            if opt == '3':
                students[student_rollnumber]['age'] = input("enter new age :")
            if opt == '4':
                students[student_rollnumber]['address'] = input("enter new address :")
            if opt == '5':
                break
        break
    else :
        print('please Enter correct number')

