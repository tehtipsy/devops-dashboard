from sysinfo import show_sysinfo
from logcheck import check_log
from tasklist import manage_tasks


def main():
    while True:
        print("\n===== DevOps Dashboard =====")
        print("[1] System Info")
        print("[2] Log Checker")
        print("[3] Task List")
        print("[0] Exit")

        choice = input("Select an option: ")

        if choice == "1":
            show_sysinfo()
        elif choice == "2":
            check_log()
        elif choice == "3":
            manage_tasks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
