#=====importing libraries===========
from datetime import date, datetime
import os

#====Funtions====
# reg_user function - an if/else statement is used, if input_name == "admin", to allow only the admin to register a user
# Else an error message is displayed and the user is returned to the main menu
# If the admin is logged in, a while True look initiated
# User asked to enter the new_name, user.txt is read and file_name and file_pass saved into 2 lists. If new_name in name_list, user prompted to enter a different name
# Else the new_name is successfully registered and the loop is broken
# While true loop initiated - user prompted to input new_pass, confirm_pass - all assigned to variables
# If statement used to check if the new_pass == the confirmed_pass
# If the passwords match the user name and password are written to the user.txt file using a whith block and the append "a"
# F string used to add the two variables in the correct order, separated by ", "
# While loop is broken, Else error message is displayed and user will have to re-enter the details
def reg_user():
    """
    reg_user function - registers a new user and appends the new user to the user.txt file
    """
    if input_name == "admin":
            
            while True:
                
                name_list = []
                pass_list= []
                
                new_name = input("\nPlease enter a new username: ").lower()
                with open("user.txt", "r") as user_file:
                    for user in user_file:
                        file_name, file_pass = user.strip().split(", ")
                        name_list.append(file_name)
                        pass_list.append(file_pass)
                if new_name in name_list:
                    print("\nThat username has been taken, please try again!")
                else:    
                    print("\nYour username has been sucessfully registered!")
                    break
                                
            while True:
                new_pass = input("Please enter a new password: ")
                confirm_pass = input("Please confirm the password: ")
                if new_pass == confirm_pass:
                    with open("user.txt", "a") as new_user:
                        new_user.write(f"\n{new_name}, {new_pass}")
                    print("\nYour new user registration was successful!\n")
                    break
                else:
                    print("\nYour passwords did not match, please try again!\n")
    else:
        print("\nOnly admins are authorised to register users!")

# add_task() function - user prompted to enter a username, task title, task description, task due date - all assigned to variables
# Datetime library imported date.today() used to get today's date - formatted to string dd mmm yyyy and assigned to a variable, and to edit task due input
# task_complete set to "No"
# With block used to open and write to tasks.txt file as append "a"
# F string used, and variables added in correct order separated bt ", "
# Success message printed    
def add_task():
    """
    add_task function - takes in task details and appends the new user to the tasks.txt file
    """   
    task_user = input("\nPlease enter the username of the person the task is assigned to: ").lower()
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please enter a description of the task: ")
    while True:
        try:
            year_due = int(input("Please enter the year the task is due, as YYYY: "))
            break
        except ValueError:
            print("You did not enter a valid number for the year as YYYY, please try again!")
    while True:
        try:
            month_due = int(input("Please enter the month the task is due, as a number MM: "))
            break
        except ValueError:
            print("You did not enter a valid number for the month as MM, please try again!")
    while True:
        try:
            day_due = int(input("Please enter the day the task is due, as DD: "))
            break
        except ValueError:
            print("You did not enter a valid number for the day as DD, please try again!")
    task_due = date(year_due, month_due, day_due)
    due_string_date = task_due.strftime("%d %b %Y")
    current_date = date.today()
    current_string_date = current_date.strftime("%d %b %Y")
    task_complete = "No"
        
    with open("tasks.txt", "a") as new_task:
        new_task.write(f"\n{task_user}, {task_title}, {task_description}, {current_string_date}, {due_string_date}, {task_complete}")
    print("\nYour new task has been assigned!\n")

# View_all function - With block used to open and read "r", from tasks.txt, readlines() used to store data in a task_list variable
# Each line .strip() to remove \n and split by ", ", then printed in an easy to read format
# Each piece of data given a title, \t used to align content displayed, and index of list used to get the correct data
def view_all():
    """
    view_all function - reads from the tasks.txt file and prints the data
    """ 
    with open("tasks.txt", "r") as task_file:
        task_list = task_file.readlines()
            
    for line in task_list:
        split_task = line.strip().split(", ")
        print(f'''
Task: \t\t{split_task[1]}
Assigned to: \t{split_task[0]}
Date Assigned: \t{split_task[4]}
Date due: \t{split_task[3]}
Task complete? \t{split_task[5]}
Task description: \n{split_task[2]}''')

# view_mine() function - Same code used as above view_all() function to display the user tasks in an easy to read format
# However, a check put in place if input_name in split_task, to only print the tasks assinged to the user logged in
# Options added to enumerate the tasks, select by task number and to mark as complete or edit the tasks
# Task counter used to check that the input task_number is within the number of tasks and greater than -1 wiht a While True loop
# The correct index for the task is found by subtracting 1 from the input task_num to avoid indexErrors
def view_mine():
    """
    view_mine function - reads from the tasks.txt file and prints the data for the logged in user allowing it to be edited if necessary
    """ 
    task_counter = 0
    with open("tasks.txt", "r") as task_file:
            task_list = task_file.readlines()
                    
    for value, task in enumerate(task_list, start=1):
        split_task = task.strip().split(", ")
        if input_name in split_task:
            task_counter += 1
            print(f'''
Task Number: \t{value}
Task: \t\t{split_task[1]}
Assigned to: \t{split_task[0]}
Date Assigned: \t{split_task[4]}
Date due: \t{split_task[3]}
Task complete? \t{split_task[5]}
Task description: \n{split_task[2]}''')

    while True:
     
            task_num = int(input("\nPlease select the task number you wish to edit, or enter -1 to return to the main menu: "))
            if task_num <= task_counter and task_num >= -1:
                break
            else:
                print("Oops that is not a valid task number! Please try again!")

    if task_num == -1:
        print("\nYou have been returned to the main menu!")
    
    else:
        index_task = task_num - 1
        split_data = task_list[index_task].split(", ")

        task_option = int(input("""\nPlease choose an option:
        1 - Mark the task as complete
        2 - Edit the task
        Enter the number of the option you would like to edit: """))

        if task_option == 1:
            split_data[5] = 'Yes\n'
            print("\nYour task has been marked as complete!")
        
        elif task_option == 2:
            edit_option = int(input("""\nPlease choose an option:
        1 - Edit the username of who the task is assigned to
        2 - Edit the due date
        Enter the number of the option you would like to edit: """))
            if edit_option == 1:
                name_edit = input("\nPlease enter the new username of who the task is assigned to: ")
                split_data[0] = name_edit
                print("\nThe username of who the task is assigned to has been edited!")
            elif edit_option == 2:
                year_due = int(input("Please enter the year the task is due: "))
                month_due = int(input("Please enter the month the task is due, as a number: "))
                day_due = int(input("Please enter the day the task is due: "))
                new_due = date(year_due, month_due, day_due)
                new_string_date = new_due.strftime("%d %b %Y")
                split_data[3] = new_string_date
                print("\nThe due date has been edited!")
            else:
                print("\nYou have not made a valid selection, please try again!")
            
        else:
            print("\nYou have not made a valid selection, please try again!")

        join_data = ", ".join(split_data)
        task_list[task_num] = join_data
        with open('tasks.txt', 'w') as task_file:
            for line in task_list:
                task_file.write(line)

# The generate_reports() function - an if statement is used to check that the input_name is equal to "admin", else an error message is displayed and the user is taken to the main menu
# Generate task_overview - a with block reads through the task file and saves it to a variable task_list - total_tasks is found from the len() task_list
# Two variables contain the current date and the date as a string
# Three variables are assigned with the value 0 as counters
# A for loop iterates over the task_list and strip().split() at comma - if index 5 is equal to "yes", the completed_tasks variable increments by 1
# Else the incompleted_tasks variable increments by 1
# An if statement also checks if the current date is more than the index 4 which is the due date - if so, overdue_tasks increments by 1
# A variable stores the formual to find the incompleted percent and overdue percent
# A with block writes the task_overview.txt file, where an f string is used to write the data in an easy to read manner
def generate_reports():
    """
    generate_reports function - reads from the tasks.txt and user.txt files, uses the data then creates two new txt files:task_overview.txt and user_overview.txt
    """
    if input_name == "admin":
            current_date = date.today()
            current_string_date = current_date.strftime("%d %b %Y")
            completed_tasks = 0
            incompleted_tasks = 0
            overdue_tasks = 0
            with open("tasks.txt", "r") as task_file:
                task_list = task_file.readlines()
                total_tasks = len(task_list)
                for task in task_list:
                    split_task = task.strip().split(", ")
                    if split_task[5].lower() == "yes":
                        completed_tasks += 1
                    else:
                        incompleted_tasks += 1
                    if current_string_date < split_task[4]:
                        overdue_tasks += 1
            incompleted_percent = round(incompleted_tasks / total_tasks * 100)
            overdue_percent = round(overdue_tasks / total_tasks * 100)
            with open("task_overview.txt", "w") as task_file:
                task_file.write(f"""Task Overview
Total tasks: {total_tasks}
Complete tasks: {completed_tasks}
Incomplete tasks: {incompleted_tasks}
Percentage of incomplete tasks: {incompleted_percent}%
Incompleted tasks that are overdue: {overdue_tasks}
Percentage of overdue tasks: {overdue_percent}%
""")

# Generate user_overview reads from the user.txt file to generate the useer_overview report
# Several counter variables are assigned a 0 value
# A with block is used to read from the user.txt file, save as a list, and use len() to find the total users
# A with block is used to open and write to the user_overview.txt file the total_users and total_tasks
# A nested for loop iterates over the user_list and strip().split() each user, then iterate over the tasks in task_list - strip().split()
# If the index 0 of the split user (ie the name) is in split_task - then the varuable user_tasks is incremented by 1
# If index 5 of the split task is equal to "yes", then the completed_tasks increments by 1, else the incompleted_tasks increments by 1
# If the current string date is later than the index 4 then the over_due tasks incremenets by 1
# If the user_tasks variable is not equal to 1, the percentages are founds and a with block used to write the user data to the txt file
# Else, it is written that the user had no assigned tasks
            user_tasks = 0
            completed_tasks = 0
            incompleted_tasks = 0
            overdue_tasks = 0
            with open("user.txt", "r") as user_file:
                user_list = user_file.readlines()
                total_users = len(user_list)
            with open("user_overview.txt", "w") as user_file:
                user_file.write(f"""
                User Overview
Total users: {total_users}
Total tasks: {total_tasks}
""")
            for user in user_list:
                split_user = user.strip().split(", ")
                for task in task_list:
                    split_task = task.strip().split(", ")
                    if split_user[0] in split_task:
                        user_tasks += 1
                    else: 
                        user_tasks = 0
                    if split_task[5].lower() == "yes":
                        completed_tasks += 1
                    else:
                        incompleted_tasks += 1
                    if current_string_date < split_task[4]:
                        overdue_tasks += 1
                
                if user_tasks != 0:
                    percent_assigned = round(user_tasks / total_tasks * 100)
                    completed_percent = round(completed_tasks / user_tasks * 100)
                    incompleted_percent = round(incompleted_tasks / user_tasks * 100)
                    overdue_percent = round(overdue_tasks / user_tasks * 100)   
                    with open("user_overview.txt", "a") as user_file:
                        user_file.write(f"""
Statistics for: {split_user[0]} 
Total tasks assigned to {split_user[0]}: {user_tasks}
Percentage of total tasks assigned to {split_user[0]}: {percent_assigned}%
Percentage of completed tasks assigned to {split_user[0]}: {completed_percent}%
Percentage of incomplete tasks assigned to {split_user[0]}: {incompleted_percent}%
Percentage of overdue tasks assigned to {split_user[0]}: {overdue_percent}%
                    """)
                else:
                    with open("user_overview.txt", "a") as user_file:
                        user_file.write(f"""
Statistics for: {split_user[0]}
{split_user[0]} has no tasks assigned to them!""")
                
            print("\nYour report has been successfully generated!")

    else:
        print("\nOnly admins can generate reports!")

# dispalay_statistics function uses an if statement to check if the input_name is admin before displaying statistics - or an error message is show
# The generate_reports() function is called to ensure that the task_overview and user_overview files are created and up to date
# Originalls I used an if statement if os.path.exists("task_overview.txt"): to check that the file existed, else call the generate_reports() function
# This works, however, if the txt files exist but are not up to date, the files that are not up to date will be displayed, so better to call the function every time
# A withblock reads the txt files and prints them to display
def display_statistics():
    """
    display statistics function - displays the task_overview.txt and user_overview.txt files in an easy to read manner
    """
    if input_name == "admin":
        generate_reports()
        with open("task_overview.txt", "r") as task_file:
            task_list = task_file.readlines()
        for line in task_list:
            print(line)
        with open("user_overview.txt", "r") as user_file:
            user_list = user_file.readlines()
        for line in user_list:
            print(line)

        print("\nYou are not authorised to view statistics!")

#====Login Section====
# While True loop initiated and break added with a boolean if logged_in == True, if user successsfully logs in
# Else user will be notified with an error message that they entered an incorrect username or password
# Use asked to input username and password - both assigend to variables
# logged_in boolean set to False
# With block used to open user.txt and read "r"
# For loop used to iterate through usernames and passwords assiged to variable.strip used to remove \n and split at comma
# If input_name and input_pass equal the username and password:
# a success message is printed, the for loop is broke, and the logged_in boolean is set to True to break out of the while loop
# Else the for loop will continue to iterate and if none match, the while loop will not be broken and the user will need to re-enter their details
while True:

    input_name = input("Please enter your user name: ").lower()
    input_pass = input("Please enter your password: ")
    logged__in = False

    with open("user.txt", "r") as user_file:
        
        for user in user_file:
            user_name, user_pass = user.strip().split(", ")
            if input_name == user_name and input_pass == user_pass:
                print("\nCongratuations, you have successfully logged in!")
                logged__in = True
                break
            else:
                continue

    if logged__in == True:
        break
    else:
        print("\nYour username or password is incorrect, please try again!")      

#====Main Menu====
# Menu - if/else statement used if input_name == "admin", to show a different menu to the admin that has a ds - display statistics option
while True:
    if input_name == "admin":

     menu = input('''\nSelect one of the following options below:
r   - Registering a user
a   - Adding a task
va  - View all tasks
vm  - View my task
gr  - Generate reports
ds  - Display statistics
e   - Exit
Type your option here: ''').lower()

    else:
         menu = input('''\nSelect one of the following options below:
r   - Registering a user
a   - Adding a task
va  - View all tasks
vm  - View my task
e   - Exit
Type your option here: ''').lower()

#====If User Selects "r"====
# If user selects "r" the reg_user() function is called
    if menu == 'r':
        pass
        reg_user()
       
#====If User Selects "a"====
# add_task() function called
    elif menu == 'a':
        pass  
        add_task()

#====If User Selects "va"====
# view_all() function called   
    elif menu == 'va':
        pass
        view_all()
            
#====If User Selects "vm"====
# view_mine() function called
    elif menu == 'vm':
        pass
        view_mine()

#====If User Selects "gr"====
# generate_reports() function is called
    elif menu == 'gr':
        pass
        generate_reports()

#====If User Selects "ds"====
# display_statistics() function called
    elif menu == 'ds':
        pass
        display_statistics()

#====If User Selects "e"====

    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again\n")
        