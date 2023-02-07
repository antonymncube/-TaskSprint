from datetime import date, datetime

# declaring variables
list_username = []
list_task = []
users_list = []

# i have created a optional function that will give me month index so that i can be able to calculate the overdue
def getMonthIndex(val):

    if(val == 'january'):
        return f"0{1}"
    elif(val == 'february'):
        return f"0{2}"
    elif(val == 'march'):
        return f"0{3}"
    elif(val == 'april'):
        return f"0{4}"
    elif(val == 'may'):
        return f"0{5}"
    elif(val == 'june'):
        return f"0{6}"
    elif(val == 'july'):
        return f"0{7}"
    elif(val == 'august'):
        return f"0{8}"
    elif(val == 'september'):
        return f"0{9}"
    elif(val == 'october'):
        return 10
    elif(val == 'november'):
        return 11
    elif(val == 'december'):
        return 12

# creating a file to get users
def getUsers():

    # opening the file user
    with open('user.txt') as file:

        #looping through the user file and splitting
        users = [user.split(",")[0].strip() for user in file.readlines()]
        file.close()
    return users

# function to get the task
def getTasks():

    #opening the task file and solitting
    with open('tasks.txt') as file:
        tasks = []
        for tline in file.readlines():
            tasks.append([task.strip() for task in tline.split(",")])
        file.close()
    return tasks

#  function to get the date in a formatted form
def convert2Date(due):
    dueDate = due.split(" ")
    reformat = f"{dueDate[0]}-{getMonthIndex(dueDate[1])}-{dueDate[2]}"
    return datetime.strptime(reformat, "%d-%m-%Y").date()

# functinon to get the user tasks and report
def getReportDetailsuser():

    # declaring local variables
    reportDetails = []
    userList = getUsers()
    taskList = getTasks()

    # checking the user
    for user in userList:

        # declaring the counters
        complete, incomplete, overdue, totTasks = 0, 0, 0, 0
        for task in taskList:
            if user == task[0]:
                totTasks += 1

                if task[-1] == "yes":
                    complete += 1
                else:
                    if date.today() > convert2Date(task[-2]):
                        overdue += 1
                    else:
                        incomplete += 1

        # storing the data on a dictinary
        reportDetails.append(dict({
            "user": user,
            "complete": complete,
            "incomplete": incomplete,
            "overdue": overdue,
            "total": totTasks
        }))

    return reportDetails

# function to calculate the percentage
def getPercentage(value, total):
    if total == 0:
        return f"{0}%"
    return f"{float(int(value)/int(total))*100}%"

# report function that calculate the stats for task and user than write them to a file
def report():
    #declaring varibales
    total_generated_task = 0
    completed_task = 0
    uncomplete_task = 0
    uncomplete_task_percentage = 0
    total_user_task = 0
    dueDate = 0
    reformatted_due_date = ""
    total_uncomplete_overdue = 0

    # opening the task file and splitting
    with open('tasks.txt', 'r') as report:
        for content in report.readlines():
            content = task_name, title_task, desrciption, assigned_date, due_date, state_task = content.strip().split(
                ", ")
            total_generated_task += 1

            # getting the due data
            due_Date = content[-2].split(" ")

            # refomatting the data
            reformatted_due_date = f"{due_Date[0]}-{getMonthIndex(due_Date[1])}-{due_Date[2]}"

            reformatted_due_date = datetime.strptime(
                reformatted_due_date, "%d-%m-%Y")

            # condition statement to get the condtions than increment
            if content[-1] == "yes":
                completed_task += 1

            elif content[-1] == "no":
                uncomplete_task += 1

            if content[-1] == "no" and reformatted_due_date.date() < date.today():
                total_uncomplete_overdue += 1

    # calculating the percentages
    uncomplete_task_percentage = (uncomplete_task / total_generated_task) * 100
    uncomplete_overdue_task_perc = (
        total_uncomplete_overdue / total_generated_task) * 100

    # opening the task-overview file for writing
    with open('task_overview.txt', 'w') as task_overview:
        task_overview.write(
            f" The total number of tasks that have been generated: {total_generated_task} \n The total number of completed tasks: {completed_task} \n The total number of uncompleted tasks: {uncomplete_task} \n The total number of tasks that haven’t been completed and that are overdue: {total_uncomplete_overdue} \n The percentage of tasks that are incomplete: {round(uncomplete_task_percentage,2)}% \n The percentage of tasks that are overdue: {round(uncomplete_overdue_task_perc,2)}%")

    print(" TASK OVERVIEW")
    # reading from the file
    with open('task_overview.txt', 'r') as task_overview:
         for overview in task_overview.readlines():
             print(overview)

    # adding a new  line between the task overview and user overview
    print("\n")

    # saving the necessary functions to varibales
    reportSum = getReportDetailsuser()
    reportStats = []

    # storing the data from the function into and list and dictinary
    for item in reportSum:
        reportStats.append(dict({
            "user": item["user"],
            "complete": getPercentage(item["complete"], item["total"]),
            "incomplete": getPercentage(item["incomplete"], item["total"]),
            "overdue": getPercentage(item["overdue"], item["total"])
        }))

    # opening the file for reading and writing the data in the list
    with open('userReport.txt', 'w+') as file:
        for task in reportStats:
            print(task)
            file.write(str(task)+'\n')
        file.close()


# function to register users
def reg_user():

   # opening the user and splitting the username and password
    with open('user.txt', 'r') as user:
        for line in user:
            usernamee, password = line.split(", ")
            list_username.append(usernamee)

    i = 0

    # using  a while loop to allow user admin to log inn
    while True:

        if username == "admin":

            # taking in user inputs
            new_username = input("please enter new username: ").lower()
            new_password = input("please enter new password: ").lower()
            confirmed_password = input(
                "please enter password new again: ").lower()

            # checking if the password match
            if new_password.lower() == confirmed_password.lower():

                with open('user.txt', 'r') as user:

                    # checking if the user exist in the list
                    if not new_username in list_username:

                        # writing the new user to the user file(register the user)
                        with open('user.txt', 'a') as user:
                            user.write(
                                f"\n{new_username.lower()}, {confirmed_password}")
                            message = "user successfully added in the system"
                        False
                        break
                    else:
                        i += 1
                        print(
                            "username already exist in the system enter a different username")

            else:
                message = "your password does not match"
        else:
            message = "Only admin can register users"
            False
            break

    print(message)

# function to add task
def add_task():

    #taking in user input
    title_taska = input("please enter the title of the task").lower()
    task_username = input(
        "please enbter the username of the person whom the task is assigned to").lower()
    current_date = input("[lease enter the current date").lower()
    task_due_date = input("please enter the task due date").lower()
    task_state = input("is the task complete").lower()
    task_description = input("please describe the task").lower()

    # opening the task file for writing additional content
    with open('tasks.txt', 'a') as task:
        # writing to the file
        task.write(
            f"\n{task_username}, {title_taska}, {task_description}, {current_date}, {task_due_date}, {task_state}")

        return

# function to view all task and edit them
def view_all(task_no, task_edit):
    i = 0
    with open('tasks.txt', 'r') as task:
        # print(task.readlines())
        for line in task.readlines():
            spl = task_name, title_task, desrciption, assigned_date, due_date, state_task = line.strip().split(", ")

            # displaying the output
            print(f"This is task NO:      {i+1}")
            print(f"Task:             {task_name}")
            print(f"Assigned to:      {title_task}")
            print(f"Date assigned to: {assigned_date}")
            print(f"Due date:          {due_date}")
            print(f"Task complete?    {state_task}")
            print(f"Task desrciption:\n{desrciption}")
            list_task.append(spl)
            i += 1

        print("\n")


        # checking the task to be edited
        if task_no <= len(list_task) and task_no >= 0:


            if task_edit == "complete":

                task_name = list_task[task_no][0]
                title_task = list_task[task_no][1]
                assigned_date = list_task[task_no][2]
                due_date = list_task[task_no][3]
                state_task = list_task[task_no][4] = "yes"
                desrciption = list_task[task_no][5]

                print(f"this is task number: {task_no+1}")
                print(f"Task:                {task_name}")
                print(f"Assigned to:        {title_task}")
                print(f"Date assigned to:   {assigned_date}")
                print(f"Due date:           {due_date}")
                print(f"Task complete?      {state_task}")
                print(f"Task desrciption:\n {desrciption}")

            # allowing the user to edit if they chose edit as their input
            elif task_edit == "edit":
                task_name = list_task[task_no][0] = input(
                    "please enter your edited username")
                due_date = list_task[task_no][3] = input(
                    "please enter the new due date")

                print(f"this is task number: {task_no + 1}")
                print(f"Task:                {task_name}")
                print(f"Assigned to:        {title_task}")
                print(f"Date assigned to:   {assigned_date}")
                print(f"Due date:           {due_date}")
                print(f"Task complete?      {state_task}")
                print(f"Task desrciption:\n {desrciption}")
        else:
            print("welcome back to the main menu")

# function to view the specific user tasks
def view_mine(username):

    with open('tasks.txt', 'r') as task:


        # looping through the task file per line and spliting the content
        for linee in task:

            # assing the splitted content to variables
            task_name, title_task, desrciption, assigned_date, due_date, state_task = linee.split(
                ", ")

            # using the if statement to verify the username
            if task_name == username:

                # displaying the output
                print(f"Task:             {task_name}")
                print(f"Assigned to:      {title_task}")
                print(f"Date assigned to: {assigned_date}")
                print(f"Due date:          {due_date}")
                print(f"Task complete?    {state_task}")
                print(f"Task desrciption: \n {desrciption}")

                message = "User granted access"

            else:
                message = "Enter correct login details"

    print(message)
    return


# opening a file for reading
file = open("user.txt", 'r+')
content = file.readlines()

# Declaring variables
list_ = []
list = []
list_task = []
dic_user_task = {}
entry = False

# using a while loop to check username and password if they are in the file(login)
while not entry:

    # taking in user input
    username = input("enter username: ").lower()
    password = input("entert password: ").lower()
    for line in content:
        if username in line and password in line:
            entry = True
            message = "you have been granted access"
            break
        else:
            message = "please enter correct login details"
    print(message)

while True:

    # taking in user input and converting the string to lower case
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
gr- generate reports
: ''').lower()

    if menu == 'r':
        pass

        # calling the function reg_user
        reg_user()

    elif menu == 'a':
        pass

        # callling the add task function
        add_task()

    elif menu == 'va':
        pass
        
        # taking user input
        task_no = int(input("please enter the task no "))
        task_complete = input(
            "Do you went to edit or the task is complete CHOOSE BETWEEN (COMPLETE/EDIT)").lower()
        # calling the function
        view_all(task_no-1, task_complete)

    elif menu == 'vm':
        pass

        # calling the view function
        view_mine(username)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    elif menu == 'gr':
        report()

    else:
        print("You have made a wrong choice, Please Try again")
