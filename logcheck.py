def check_log():
    filename = input("Enter log filename: ")
    try:
        with open(filename, "r") as f:
            for line in f:
                if "ERROR" in line:
                    print(line, end="")
    except FileNotFoundError:
        print(f"File not found: {filename}")
