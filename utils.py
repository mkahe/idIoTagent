import csv
from datetime import datetime
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def read_file():
    with open('data_samples/idIoTagent_2.csv', 'r') as file:
        result = []
        csvreader = csv.reader(file)
        for row in csvreader:
            result.append(row)
            # print(row)
    return result


def get_row(data, param):
    result = []
    for row in data:
        if row[2].strip() == param:
            result.append((convert_to_date(row[5].strip()), float(row[3].strip())))
    return result


def get_value(param):
    result = read_file()
    temp = get_row(result, param)
    return temp


def get_max(data):
    res = max(data, key=lambda x: x[1])[1]
    return res


def get_min(data):
    res = min(data, key=lambda x: x[1])[1]
    return res


def get_avg(data):
    values = [temp for _, temp in data]
    return sum(values) / len(values)


def get_mean(data):
    values = [temp for _, temp in data]
    return np.mean(values)


def get_var(data):
    values = [temp for _, temp in data]
    return np.var(values)


def convert_to_date(time_string):
    time_format = "%H:%M:%S"
    datetime_object = datetime.strptime(time_string, time_format)
    return datetime_object


def plot(data, param):
    values = [temp for _, temp in data]
    plt.hist(values, bins=10)
    plt.xlabel(param)
    plt.ylabel("Frequency")
    plt.title(f"{param} Histogram")
    plt.show()