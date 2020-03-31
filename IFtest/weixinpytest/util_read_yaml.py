import yaml

import os


def read_yaml(filename):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    path_filename = os.path.join(cur_path, filename)
    with open(path_filename) as f1:
        data = yaml.load(f1)
    return data


def get_test_data():
    test_data = read_yaml("test_data.yaml")
    print(test_data['payload'])
    return test_data


get_test_data()