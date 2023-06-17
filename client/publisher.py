import time
import paho.mqtt.client as mqtt
import util
import sensor_api as sapi
# import smbus
import smbus2 as smbus
from collections import deque
import numpy as np
import statistics

def timer(f):
    def wrapper(*args, **kw): # To decorate a function with input arguments
        t_start = time.time() # Start timer
        result = f(*args, **kw) # Call function
        t_end = time.time() # End timer
        return result, t_end-t_start # Return the result AND the execution time
    return wrapper

@timer
def new_corr(x_in, autocorr_thre, rounding):
    x_in_l = list(x_in)
    var = np.var(x_in_l)
    if var == 0:
        return int(len(x_in_l)/2)
    ndata = x_in_l - np.mean(x_in_l)
    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:]

    acorr = acorr / var / len(ndata)

    acorr = acorr/max(acorr)
    # print("ndata", ndata)
    print(">>>>acorr: ", acorr)
    for kk in range(int(len(acorr))):
        if acorr[kk] < autocorr_thre:
            idx = kk + 1
            break

    return idx




def autocorrelation(x_in, autocorr_thre, rounding):
    # Subtract the mean from the array
    x = list(x_in)
    x = np.array(x)
    x_mean = x - np.mean(x)

    # Compute the autocorrelation using numpy.correlate
    autocorr = np.correlate(x_mean, x_mean, mode='full')

    # Normalize the autocorrelation values
    autocorr /= np.max(autocorr)
    # print(20*"*")
    # print(autocorr)
    for kk in range(int(len(autocorr))):
        if autocorr[kk] < autocorr_thre:
            idx = kk + 1
            break

    return idx


def auto_corr(arr, autocorr_thre, rounding):
    temp_checking = list(arr)
    # print(20*"*")
    # print("max: ", max(temp_check))
    # print("min: ", min(temp_check))
    # if rounding:
    #     temp_checking = list(map(round, temp_check))
    # else:
    #     temp_checking = temp_check
    
    # print("raw_data: ", temp_checking)
    lags = np.arange(int(len(arr)/2))
    acorr = len(lags) * [0]

    temp_mean = np.mean(temp_checking)
    temp_var = np.var(temp_checking)
    # print("var temp check stat: ", statistics.variance(temp_checking))
    # print("var temp check numpy: ", temp_var)
    if temp_var == 0:
        print("<><><><> var was ZERO!")
        return int(len(temp_checking)/2)
    
    temp_checking_mean = [x - temp_mean for x in temp_checking]

    for l in lags:

        c = 1  # Self correlation

        if (l > 0):
            tmp = [temp_checking_mean[l:][i] * temp_checking_mean[:-l][i]

                for i in range(len(temp_checking) - l)]
            c = (sum(tmp) / len(temp_checking)) / temp_var

        acorr[l] = c
    
    # print("------->>>>> corr : ", acorr)
    for kk in range(int(len(acorr))):
        if acorr[kk] < autocorr_thre:
            idx = kk + 1
            break

    return idx

# The callback for when the client receives a CONNACK response from the server.


client = mqtt.Client()
client.on_connect = util.on_connect
client.on_message = util.on_message


print(util.server)
client.connect(util.server,1883,60)



# intialize sensors, so we can get data out 
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
sensor = sapi.BH1750(bus)
bme680_sensor = sapi.sensor_bme680()  # Temperature, and Humidity sensor
sgp30_sensor = sapi.sensor_sgp30() # Air quality sensor

######################### Logic for furter programming #######################
total_processing_time = 0
counter = 0
arr_size = 5
sleep_time = 5
check_time = 20
light_indx = 1
temp_indx = 1
quality_indx = 1
autocorr_temp_thre = 0.5
autocorr_light_thre = 0.5
autocorr_quality_thre = 0.5
raw_deque_light = deque(maxlen=int(check_time))
raw_deque_quality = deque(maxlen=int(check_time))
raw_deque_temp = deque(maxlen=int(check_time))
raw_deque_light_ts = deque(maxlen=int(check_time))
raw_deque_quality_ts = deque(maxlen=int(check_time))
raw_deque_temp_ts = deque(maxlen=int(check_time))
# raw_deque_light = deque(maxlen=int((60*60)/sleep_time))
# raw_deque_quality = deque(maxlen=int((60*60)/sleep_time))
# raw_deque_temp = deque(maxlen=int((60*60)/sleep_time))
# raw_deque_light_ts = deque(maxlen=int((60*60)/sleep_time))
# raw_deque_quality_ts = deque(maxlen=int((60*60)/sleep_time))
# raw_deque_temp_ts = deque(maxlen=int((60*60)/sleep_time))

userid=util.userid

# Temperature, pressure and humidty - BME680
data_temp = []
timestamps_temp = []

data_pressure = []
timestamps_pressure = []


data_humidity = []
timestamps_humidity = []

# Air quality - SGP30
data_airquality = []
timestamps_airquality = []

# Light - BH1750
data_lowres = []
timestamps_lowres = []

data_highres = []
timestamps_highres = []
data_highres2 = []
timestamps_highres2 = []

while(1):
    time.sleep(sleep_time)
    counter += 1

    #Temperature sample in celcius
    bme680_sensor = sapi.sensor_bme680()
    temp_sample, ts_temp = bme680_sensor.get_temp()
    #print(temp_sample, ts_temp)
    raw_deque_temp.append(temp_sample)
    raw_deque_temp_ts.append(ts_temp)
    if counter%temp_indx == 0:
        data_temp.append(temp_sample)
        timestamps_temp.append(ts_temp)

    #Humidity sample
    humidity_sample, ts_humid = bme680_sensor.get_humidity()
    data_humidity.append(humidity_sample)
    timestamps_humidity.append(ts_humid)
    #Pressure sample
    pressure_sample, ts_pressure = bme680_sensor.get_pressure()
    data_pressure.append(pressure_sample)
    timestamps_pressure.append(ts_pressure)

    #airquality (CO2)
    airqual_sample, ts_qual = sgp30_sensor.get_sample()
    raw_deque_quality.append(airqual_sample)
    raw_deque_quality_ts.append(ts_qual)
    if counter%quality_indx == 0:
        data_airquality.append(airqual_sample)
        timestamps_airquality.append(ts_qual)

    #Light samples Lx
    sample,ts = sensor.measure_low_res()
    data_lowres.append(sample)
    timestamps_lowres.append(ts)

    sample, ts = sensor.measure_high_res()
    raw_deque_light.append(sample)
    raw_deque_light_ts.append(ts)
    if counter%light_indx == 0:
        data_highres.append(sample)
        timestamps_highres.append(ts)

    sample, ts = sensor.measure_high_res2()
    data_highres2.append(sample)
    timestamps_highres2.append(ts)
    sensor.set_sensitivity((sensor.mtreg + 10) % 255)
    if max(len(data_temp), len(data_airquality), len(data_highres)) >= arr_size:
        parameters_output_list_names = []
        parameters_output_list_values = []
        parameters_output_list_ts = []

        if data_temp:
            parameters_output_list_names.append("temp")
            parameters_output_list_values.append(data_temp)
            parameters_output_list_ts.append(timestamps_temp)

        if data_airquality:
            parameters_output_list_names.append("quality")
            parameters_output_list_values.append(data_airquality)
            parameters_output_list_ts.append(timestamps_airquality)

        if data_highres:
            parameters_output_list_names.append("light")
            parameters_output_list_values.append(data_highres)
            parameters_output_list_ts.append(timestamps_highres)

        data=util.prepare_payload(parameters_output_list_names, parameters_output_list_values, parameters_output_list_ts)
        util.send_topics(data,userid,client)
        data_light = []
        timestamps_light = []

        data_temp = []
        timestamps_temp = []

        data_pressure = []
        timestamps_pressure = []

        data_airquality = []
        timestamps_airquality = []

        data_humidity = []
        timestamps_humidity = []

        data_highres = []
        timestamps_highres = []

    if counter%check_time == 0:
        print("raw_data: ", raw_deque_light)
        # light_indx = auto_corr(raw_deque_light, autocorr_light_thre, 1)
        # temp_indx = auto_corr(raw_deque_temp, autocorr_temp_thre, 0)
        # quality_indx = auto_corr(raw_deque_quality, autocorr_quality_thre, 0)
        # light_indx = autocorrelation(raw_deque_light, autocorr_light_thre, 1)
        # temp_indx = autocorrelation(raw_deque_temp, autocorr_temp_thre, 0)
        # quality_indx = autocorrelation(raw_deque_quality, autocorr_quality_thre, 0)

        light_indx, time1 = new_corr(raw_deque_light, autocorr_light_thre, 1)
        temp_indx, time2 = new_corr(raw_deque_temp, autocorr_temp_thre, 0)
        quality_indx, time3 = new_corr(raw_deque_quality, autocorr_quality_thre, 0)
        total_processing_time = total_processing_time + time1 + time2 + time3
        print("Total time: ", total_processing_time)
        
        err_indx = int(check_time/2)
        if quality_indx == err_indx:
            quality_indx += 1
        
        if temp_indx == err_indx:
            temp_indx += 1

        if light_indx == err_indx:
            light_indx += 1

        print(">>>> new light index: ", light_indx)
        print(">>>> new temp index: ", temp_indx)
        print(">>>> new quality index: ", quality_indx)       

 
