# idIoTagent Project

In the Oulu Ubicomp Summer School 2023 project, we successfully developed an innovative and compact IoT module based on the Raspberry Pi platform. This module is designed to efficiently capture and transmit crucial environmental data, including light intensity, air quality, and temperature.

Our team dedicated significant effort to ensure the data compactness while maintaining high performance. By leveraging the capabilities of the Raspberry Pi 3, we achieved a remarkably slim design, making it ideal for various applications where resources are limited.

The IoT module excels at collecting accurate and real-time information about the surrounding environment. Its integrated sensors provide precise measurements of light levels, allowing users to monitor and analyze ambient lighting conditions. Additionally, the module gauges air quality parameters, enabling insights into pollutant levels and overall air health. Furthermore, temperature sensing capabilities offer valuable data for monitoring and controlling thermal conditions.

For running the code, and analyse the data captured from the sensors, you need to run `analyse.py` file

```
python3 analyse.py
```

## Methodologies

### Savitzky Filter
The apply_filter method implemented in this project applies a data smoothing technique known as the Savitzky-Golay filter to the air quality data. Data smoothing plays a vital role in removing noise and capturing underlying trends and patterns in time series data.

The Savitzky-Golay filter, is a widely used digital filter that provides effective smoothing by fitting a local polynomial regression model to the data. Next, the Savitzky-Golay filter is applied to the data using the savgol_filter function. The function takes parameters window_length and polyorder, which determine the characteristics of the filter. The window_length parameter specifies the size of the window or the number of data points considered for each local regression. A larger window length allows capturing broader trends but may smooth out rapid changes. A higher polynomial order captures more complex trends but may introduce artifacts.

![alt text](/resources/air-quality.png)

After applyting the filter the data will be in this shape.

![filteration](/resources/filteration.png)