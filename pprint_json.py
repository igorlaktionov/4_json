import json
import os.path
import sys


def load_data(file_path):
    with open(file_path, 'r') as handler:
        return json.load(handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4))


def validate_file_path():
    if len(sys.argv) < 2:
        print("Please write argument file path")
        return False
    elif not os.path.isfile(sys.argv[1]):
        print("File not exist")
        return False
    elif not os.access(sys.argv[1], os.R_OK):
        print("File is not readable")
        return False
    else:
        return True


if __name__ == '__main__':
    try:
        if validate_file_path():
            json_data = load_data(sys.argv[1])
            pretty_print_json(json_data)
    except ValueError as error:
        print('Invalid json: %s' % error)

