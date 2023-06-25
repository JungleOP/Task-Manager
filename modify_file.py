from tabulate import tabulate
import csv
from datetime import datetime
from validate_date import is_valid_date
def modify_task_file(file_name):
    file_path = file_name + ".csv"
    if not file_path.endswith(".csv"):
        file_path += ".csv"
    options = input("Press [1] to delete tasks or [2] to modify a task: ")
    if options == "1":
        try:
            with open(file_path, "r") as csvfile:
                print("Here are the tasks you have. Enter the task ID you want to delete: ")
                options = []
                reader = csv.DictReader(csvfile)
                for row in reader:
                    options.append(
                        {"Task ID": row["Task ID"], "Task": row["Task"], "Date": row["Date"], "Priority": row["Priority"],
                         "Due_Date": row["Due_Date"]})
                print(tabulate(options, headers="keys", tablefmt="grid"))
                ID = int(input("ID: "))
                if 1 <= ID <= len(options):
                    deleted_task = options.pop(ID - 1)
                    print("Task deleted successfully:", deleted_task["Task"])

                    with open(file_path, "w", newline="") as csvfile:
                        fieldnames = ["Task ID", "Task", "Date", "Priority", "Due_Date"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(options)

                    print("Task file updated.")
                else:
                    print("Invalid task ID.")
        except FileNotFoundError:
            print("File not found: " + file_path)
        except PermissionError:
            print("Permission denied: " + file_path)
        except IOError:
            print("An error occurred while opening the file: " + file_path)


    elif options == "2":

        try:
            with open(file_path, "r") as csvfile:
                print("Here are the tasks you have. Enter the task ID to modify the task: ")
                options = []
                reader = csv.DictReader(csvfile)
                for row in reader:
                    options.append(
                        {"Task ID": row["Task ID"], "Task": row["Task"], "Date": row["Date"],
                         "Priority": row["Priority"],
                         "Due_Date": row["Due_Date"]})
                print(tabulate(options, headers="keys", tablefmt="grid"))
                ID = int(input("ID: "))
                if 1 <= ID <= len(options):
                    tasks_to_keep = [task for task in options if task["Task ID"] != str(ID)]
                    with open(file_path, "w", newline="") as csvfile:
                        fieldnames = ["Task ID", "Task", "Date", "Priority", "Due_Date"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(tasks_to_keep)
                    with open(file_path, "a", newline="") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        task = input("Task name: ")
                        date = datetime.today().date()
                        priority = input("Priority (0 for very important & urgent, 1 for important but not urgent): ")

                        while not priority.isnumeric():
                            print("Priority is not a number. Please try again.")

                            priority = input(
                                "Priority (0 for very important & urgent, 1 for important but not urgent): ")
                        due_date = input("Due date: ")
                        is_valid_date(due_date)

                        task_data = {

                            "Task ID": ID,

                            "Task": task,

                            "Date": date,

                            "Priority": priority,

                            "Due_Date": due_date

                        }
                        writer.writerow(task_data)

                        print(f"Task {ID} modified successfully")
                else:
                    print("Invalid task ID.")
        except FileNotFoundError:

            print("Invalid File name")