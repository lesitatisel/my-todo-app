FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a list of to-do
    items.
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    :param filepath:
    :param todos_arg:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos(FILEPATH))