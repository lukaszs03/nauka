def file_open(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found, please insert correct file name")

file_name = input("Please insert the name of file which you want to open: ")

file_content = file_open(file_name)
    