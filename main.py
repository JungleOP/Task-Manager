
import sys
from create_file import create_task_file
from modify_file import modify_task_file
from display_task import display_task_file


def main():
    while True:
        try:
            options = input("Enter [1] to create a new task file or [2] to modify an existing task file or [3] to display the tasks you have:")
            print("(press ctrl+D to exit)")
            if options == "1":
                file_name = input("Please provide the file name: ")
                if file_name:
                    create_task_file(file_name)
                else:
                    print("Invalid file name.")
            elif options == "2":
                file_name = input("Please provide the file name you want to modify: ")
                if file_name:
                    modify_task_file(file_name)
                else:
                    print("Invalid file name.")
            elif options == "3":
                file_name = input("Please provide the file name you want to display: ")
                if file_name:
                    display_task_file(file_name)
                else:
                    print("Invalid file name.")
            else:
                print("Invalid option")
        except EOFError:
            sys.exit("Exited Successfully, Have A good day ")




if __name__ == '__main__':
    main()
