from utils import *

temp = get_value("temp")
quality = get_value("quality")
light = get_value("light")

print(temp)

print("temp max: ", get_max(temp))
print("quality max: ", get_max(quality))
print("light max: ", get_max(light))

# print("temp min: ", get_min(temp))
# print("quality min: ", get_min(quality))
# print("light min: ", get_min(light))

print("temp mean: ", get_mean(temp, datetime.now() - timedelta(hours=21), datetime.now()))
print("quality mean: ", get_mean(temp, datetime.now() - timedelta(hours=21), datetime.now()))
print("light mean: ", get_mean(light))

print("temp max in last hour: ", get_max(temp, datetime.now()-timedelta(hours=1), datetime.now()))
print("temp min in last hour: ", get_min(temp, datetime.now()-timedelta(hours=1), datetime.now()))
print("temp avg in last hour: ", get_mean(temp, datetime.now()-timedelta(hours=1), datetime.now()))

print("quality max in last hour: ", get_max(quality, datetime.now()-timedelta(hours=1), datetime.now()))
print("quality min in last hour: ", get_min(quality, datetime.now()-timedelta(hours=1), datetime.now()))
print("quality avg in last hour: ", get_mean(quality, datetime.now()-timedelta(hours=1), datetime.now()))

print("light max in last hour: ", get_max(light, datetime.now()-timedelta(hours=1), datetime.now()))
print("light min in last hour: ", get_min(light, datetime.now()-timedelta(hours=1), datetime.now()))
print("light avg in last hour: ", get_mean(light, datetime.now()-timedelta(hours=1), datetime.now()))

# print("temp var: ", get_var(temp))
# print("quality var: ", get_var(quality))
# print("light var: ", get_var(light))

# plot(temp, "Temperature")
# plot(quality, "Quality")
# plot(light, "light")