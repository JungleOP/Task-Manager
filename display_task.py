from tabulate import tabulate
import csv

def display_task_file(file_name):
    file_path = file_name + ".csv"
    with open(file_path, "r") as csvfile:
        options = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(
                {"Task ID": row["Task ID"], "Task": row["Task"], "Date": row["Date"], "Priority": row["Priority"],
                 "Due_Date": row["Due_Date"]})
        print(tabulate(options, headers="keys", tablefmt="grid"))