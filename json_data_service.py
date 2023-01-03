import json
import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


class JSONService:
    def __init__(self):
        return

    @staticmethod
    def create_data(filename: str, data):
        file = open('data/{0}.json'.format(filename), 'w')
        json_string = json.dumps(data, cls=NpEncoder)
        file.write(json_string)
        file.close()
        return

    @staticmethod
    def update_data():
        return

    @staticmethod
    def read_data(filename: str):
        file = open('data/{0}.json'.format(filename), 'r')
        return json.load(file)
