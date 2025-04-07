import json
import os
from dataclasses import field

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)
        return seq[field]

def main():
    pass

def linear_search()



if __name__ == '__main__':
    main()