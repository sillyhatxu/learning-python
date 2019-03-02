#Jim - Salesman
#Dwight - Salesman
#Pam - Receptionist
#Michael - Manager
#Oscar - Accountant
employee_file = open("reading_files.txt", "r")
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()
print("----------")

employee_file = open("reading_files.txt", "r")  # r is read ; w is write ; a is append to the file
print(employee_file.readable())
print(employee_file.readlines()[2])
employee_file.close()
print("----------")

employee_file = open("reading_files.txt", "r")  # r is read ; w is write
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
print("----------")

employee_file = open("reading_files.txt", "r")  # r is read ; w is write
print(employee_file.read())
employee_file.close()
print("----------")
# employee_file = open("reading_files.txt", "w")  # r is read ; w is write, if w then clear file
#
# print(employee_file.readable())
#
# employee_file.close()