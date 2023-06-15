import datetime

def find_dramatic_changes(data):
    dramatic_changes = []
    for i in range(1, len(data)):
        current_datetime, current_temp = data[i]
        prev_datetime, prev_temp = data[i-1]
        temp_difference = abs(current_temp - prev_temp)
        if temp_difference >= 1.0:
            dramatic_changes.append(current_datetime)
    return dramatic_changes

# Sample data
data = [
    (datetime.datetime(2023, 6, 13, 16, 23, 11), 24.25),
    (datetime.datetime(2023, 6, 13, 16, 24, 13), 24.2),
    (datetime.datetime(2023, 6, 13, 16, 25, 16), 24.3),
    (datetime.datetime(2023, 6, 13, 16, 26, 18), 24.4),
    (datetime.datetime(2023, 6, 13, 16, 27, 21), 25.5),
    (datetime.datetime(2023, 6, 13, 16, 28, 23), 25.5),
    (datetime.datetime(2023, 6, 13, 16, 28, 23), 25.5),
    (datetime.datetime(2023, 6, 13, 16, 28, 23), 24.1),
    (datetime.datetime(2023, 6, 13, 16, 28, 23), 24.0),
]

dramatic_changes = find_dramatic_changes(data)
for dt in dramatic_changes:
    print(dt)