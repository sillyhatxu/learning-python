employee_file = open("writing_files.txt", "a")  # a : append to the file
employee_file.write("\nCookie is software engineer.")
employee_file.close()
print("----------")


employee_file = open("writing_files.txt", "w")  # w : write;It will be clear this file.
employee_file.write("Cookie is software engineer.")
employee_file.write("\n<p>This is HTML</p>")
employee_file.close()
print("----------")