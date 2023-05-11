path = "text.txt"
word = "cat"

try:
    with open(path, "r", encoding="UTF-8") as f:
        text = f.read()
        counts = text.count(word)
        print(f"Number of words present {word} in file {path} is {counts}.")
except FileNotFoundError:
    print(f"File not found")
except PermissionError:
    print(f"Insufficient permissions to open the file")