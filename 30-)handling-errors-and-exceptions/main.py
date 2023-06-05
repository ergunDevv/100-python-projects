# FileNotFound

try:
    file = open(r"30-)handling-errors-and-exceptions\data.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open(r"30-)handling-errors-and-exceptions\data.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # raise KeyError
    file.close()
    print("File was closed.")
