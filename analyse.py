from utils import *
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return result
    return wrapper

@timer
def go_man_go():
    temp = get_value("temp")
    quality = get_value("quality")
    light = get_value("light")

    # print(light)

    # print("temp max: ", get_max(temp))
    # print("quality max: ", get_max(quality))
    # print("light max: ", get_max(light))

    # # print("temp min: ", get_min(temp))
    # # print("quality min: ", get_min(quality))
    # # print("light min: ", get_min(light))

    # print("temp mean: ", get_mean(temp, datetime.now() - timedelta(hours=21), datetime.now()))
    # print("quality mean: ", get_mean(quality, datetime.now() - timedelta(hours=21), datetime.now()))
    # print("light mean: ", get_mean(light))

    # print("temp max in last hour: ", get_max(temp, datetime.now()-timedelta(hours=1), datetime.now()))
    # print("temp min in last hour: ", get_min(temp, datetime.now()-timedelta(hours=1), datetime.now()))
    # print("temp avg in last hour: ", get_mean(temp, datetime.now()-timedelta(hours=1), datetime.now()))

    # print("quality max in last hour: ", get_max(quality, datetime.now()-timedelta(hours=1), datetime.now()))
    # print("quality min in last hour: ", get_min(quality, datetime.now()-timedelta(hours=1), datetime.now()))
    # print("quality avg in last hour: ", get_mean(quality, datetime.now()-timedelta(hours=1), datetime.now()))

    # print("light max in last hour: ", get_max(light, datetime.now()-timedelta(days=1), datetime.now()))
    # print("light min in last hour: ", get_min(light, datetime.now()-timedelta(days=1), datetime.now()))
    # print("light avg in last hour: ", get_mean(light, datetime.now()-timedelta(days=1), datetime.now()))

    # print("light ci in last hour: ", get_ci(light, datetime.now()-timedelta(days=1), datetime.now()))

    # print("temperature changes: ", temp_changes(temp))

    # print("light changes: ", light_changes(light))

    # print("temp var: ", get_var(temp))
    # print("quality var: ", get_var(quality))
    # print("light var: ", get_var(light))

    # plot(temp, "Temperature")
    # plot(quality, "Quality")
    # plot(light, "light")

    # plot_series(temp, "Temperature")
    # plot_series(light, "Light")
    # plot_series(quality, "Quality")

    start_date = datetime(2023, 6, 16, 10, 0)
    first_hour = datetime(2023, 6, 16, 11, 0)
    second_hour = datetime(2023, 6, 16, 12, 0)

    print("TASK 1:")
    print("   Temperature 1st hour")
    print("      Mean ", round(get_mean(temp, start_date, first_hour), 3))
    print(f"      CI [{round(get_ci(temp, start_date, first_hour)[0], 3)}, {round(get_ci(temp, start_date, first_hour)[1], 3)}]")
    print("   Temperature 2nd hour")
    print("      Mean ", round(get_mean(temp, first_hour, second_hour), 3))
    print(f"      CI [{round(get_ci(temp, first_hour, second_hour)[0], 3)}, {round(get_ci(temp, first_hour, second_hour)[1], 3)}]")

    print("TASK 2: Maximum Temperature = ", get_max(temp, start_date, second_hour))

    print("TASK 4: Air quality:")
    print("      Mean ", round(get_mean(quality, start_date, second_hour), 3))
    print(f"      CI [{round(get_ci(quality, start_date, second_hour)[0], 3)}, {round(get_ci(quality, start_date, first_hour)[1], 3)}]")

    print("TASK 5: Worst air quality ", get_max(quality, start_date, second_hour)) # TODO

    print("TASK 6: Light ")
    print("      Mean ", round(get_mean(light, start_date, second_hour), 3))
    print(f"      CI [{round(get_ci(light, start_date, second_hour)[0], 3)}, {round(get_ci(light, start_date, first_hour)[1], 3)}]")

    print(f"Total amoun of transmitted data is {round(get_data_size(start_date, second_hour), 2)} bytes")
    # print(f"Total execution time of additional algorithms is {100} bytes")

    print("\n\n")
    print("light changes: ", light_changes(light))
    print("\n\n")

    print("quality changes: ", quality_changes(quality))

    # plot_series(quality, "Quality")
    # filtered = apply_filter(quality)
    # plt.plot([k for k in range(len(filtered))],filtered)
    # plt.show()

    # classified = classify_quality(filtered)
    # plt.plot([k for k in range(len(classified))],classified)
    # plt.show()

go_man_go()