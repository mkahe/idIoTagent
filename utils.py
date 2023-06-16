import csv
from datetime import datetime, timedelta
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.signal import savgol_filter

def read_file():
    with open('data_samples/idIoTagent_4.csv', 'r') as file:
        result = []
        csvreader = csv.reader(file)
        for row in csvreader:
            result.append(row)
            # print(row)
    return result


def get_row(data, param):
    result = []
    for row in data:
        if len(row) > 0:
            if row[2].strip() == param:
                result.append((convert_to_date(row[5].strip(), row[7]), float(row[3].strip())))    
    return result


def get_data_size(from_date=None, to_date=None):
    data = read_file()
    result = []
    for row in data:
        if len(row) > 0:
            result.append((convert_to_date(row[5].strip(), row[7]), float(row[9].strip())))
    values = filter_data(result, from_date, to_date)
    if len(values) == 0: return 0
    return sum(values)


def get_value(param):
    result = read_file()
    temp = get_row(result, param)
    return temp


def get_max(data, from_date=None, to_date=None):
    values = filter_data(data, from_date, to_date)
    if len(values) == 0: return 0
    res = max(values)
    return res


def get_min(data, from_date=None, to_date=None):
    values = filter_data(data, from_date, to_date)
    if len(values) == 0: return 0
    res = min(values)
    return res


def get_mean(data, from_date=None, to_date=None):
    values = filter_data(data, from_date, to_date)
    if len(values) == 0: return 0
    return np.mean(values)


def get_ci(data, from_date=None, to_date=None):
    values = filter_data(data, from_date, to_date)
    return st.t.interval(alpha=0.95, df=len(values)-1, loc=np.mean(values), scale=st.sem(values)) 


def get_var(data, from_date=None, to_date=None):
    values = filter_data(data, from_date, to_date)
    if len(values) == 0: return 0
    return np.var(values)


def filter_data(data, from_date, to_date):
    if from_date and to_date:
        filtered_values = [value for dt, value in data if from_date <= dt <= to_date]
        return filtered_values
    return [value for _, value in data]


def convert_to_date(time_string, date_part):
    time_format = "%Y-%m-%dT%H:%M:%S"
    complete_date = f"2023-06-{date_part.split('/')[0].strip()}T{time_string}"
    datetime_object = datetime.strptime(complete_date, time_format)
    return datetime_object


def plot(data, param):
    values = [temp for _, temp in data]
    plt.hist(values, bins=10)
    plt.xlabel(param)
    plt.ylabel("Frequency")
    plt.title(f"{param} Histogram")
    plt.show()
    
def plot_series(data, param):
    values = [temp for _, temp in data]
    plt.title(param)
    plt.plot([k for k in range(len(values))],values)
    plt.show()

def temp_changes(data):
    return get_changes(data, 0.4)

def light_changes(data):
    return get_changes(data, 500)

def quality_changes(data):
    return get_changes(data, 100)

def get_changes(data, thresh):
    dramatic_changes = []
    for i in range(1, len(data)):
        current_datetime, current_value = data[i]
        prev_datetime, prev_value = data[i-1]
        temp_difference = abs(current_value - prev_value)
        if temp_difference >= thresh:
            dramatic_changes.append(current_datetime)
    return dramatic_changes

def apply_filter(data):
    values = [value for _, value in data]
    y_filtered = savgol_filter(values, window_length = 200, polyorder = 2)
    return y_filtered

def classify_quality(data, from_date=None, to_date=None):
    new = []
    thresh = np.mean(data)
    max = np.max(data)
    min = np.min(data)
    for row in data:
        if row < thresh:
            new.append(min)
        if row >= thresh:
            new.append(max)
    return new

def quality_changes(data):
    filtered = apply_filter(data)
    classified = classify_quality(filtered)
    result = []
    for i in range(len(data)):
        result.append((data[i][0], classified[i]))
    return get_changes(result, 100)
    