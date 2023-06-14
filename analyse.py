from utils import *

temp = get_value("temp")
quality = get_value("quality")
light = get_value("light")

print("temp max: ", get_max(temp))
print("quality max: ", get_max(quality))
print("light max: ", get_max(light))

# print("temp min: ", get_min(temp))
# print("quality min: ", get_min(quality))
# print("light min: ", get_min(light))

print("temp mean: ", get_mean(temp))
print("quality mean: ", get_mean(quality))
print("light mean: ", get_mean(light))

# print("temp var: ", get_var(temp))
# print("quality var: ", get_var(quality))
# print("light var: ", get_var(light))

plot(temp, "Temperature")
plot(quality, "Quality")
plot(light, "light")