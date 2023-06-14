from utils import *

temp = get_temp()
quality = get_quality()

print(get_max(temp))
print(get_max(quality))
print(get_avg(temp))
print(get_avg(quality))
print(get_mean(temp))
print(get_mean(quality))
print(get_var(temp))
print(get_var(quality))
plot(temp)
plot(quality)