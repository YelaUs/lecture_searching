import json
import os
from dataclasses import field
from itertools import count

from numpy.ma.core import indices

from lecture_searching.generators import dna_sequence

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

def linear_search(seq, number):
    indices =[]
    count = 0
    idx = 0
    while idx < len(seq):
        if seq[idx] == number:
            indices.append(idx)
            count += 1
        idx +=1
    return {
        'positions': indices,
        'count': count,
    }

def pattern_search(seq, pattern):
    indices = set()
    pattern_size=len(pattern)
    left_idx=0
    right_idx=pattern_size
    while right_idx < len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq[left_idx + idx]:
                break
        else:
            indices.add(left_idx + pattern_size // 2)
            left_idx +=1
            right_idx +=1
            return indices

#def binary_search(search_number, number):


def main():
    file_name= 'sequential.json'
    seq=read_data(file_name, field='unordered_numbers')
    results = linear_search(seq, 0)
    print(results)
    seq=read_data(file_name, field='dna_sequence')
    pattern = 'ATA'
    matches=pattern_search(seq, pattern)

if __name__ == '__main__':
    main()