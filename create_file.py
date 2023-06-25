import os
from tabulate import tabulate
import csv
from datetime import datetime
from validate_date import is_valid_date
def create_task_file(file_name):
    file_path = file_name + ".csv"
    if not file_path.endswith(".csv"):
        file_path += ".csv"
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["Task ID", "Task", "Date", "Priority", "Due_Date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        counter = int(input("Enter the number of tasks you want to add: "))
        task_id = 1

        for i in range(counter):
            task = input("Task name: ")
            date = datetime.today().date()
            priority = input("Priority (0 for very important & urgent, 1 for important but not urgent): ")

            while not priority.isnumeric():
                print("Priority is not a number. Please try again.")
                priority = input("Priority (0 for very important & urgent, 1 for important but not urgent): ")

            due_date = input("Due date: ")
            is_valid_date(due_date)


            task_data = {
                "Task ID": task_id,
                "Task": task,
                "Date": date,
                "Priority": priority,
                "Due_Date": due_date
            }

            writer.writerow(task_data)
            task_id += 1

    print("Here are the tasks you added:")
    with open(file_path, "r") as csvfile:
        options = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(
                {"Task ID": row["Task ID"], "Task": row["Task"], "Date": row["Date"], "Priority": row["Priority"],
                 "Due_Date": row["Due_Date"]})
        print(tabulate(options, headers="keys", tablefmt="grid"))
