import yaml
import argparse


class Config:
    def __init__(self, path):
        self.path = path
        self.config = self.read_config()

    def read_config(self):
        with open(self.path) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config


def parse() -> list:
    """Gets arg parameters"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", type=str, help="Set a tag")
    parser.add_argument("-t", type=str, help="Set a title")
    parser.add_argument("-d", type=str, help="Set a description")
    parser.add_argument("-s", action='store_true')
    args = parser.parse_args()
    return args
