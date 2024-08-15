import sys

def save_to_file(variable_value, file_path):
    with open(file_path, 'w') as file:
        file.write(variable_value)

if __name__ == "__main__":
    save_to_file(sys.argv[1], sys.argv[2])
