def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode="w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode="a") as f:
        f.write(append_content)

def read_file(file_name):
    # text_file = open(f'{file_name}.txt', mode="r")
    # print(text_file.read())
    with open(f'{file_name}.txt', mode="r") as f:
        return f.read()