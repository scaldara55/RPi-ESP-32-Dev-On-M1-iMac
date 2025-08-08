from machine import Pin, I2C
from time import sleep, localtime
import si7021
import uos

# Initialize I2C interface on default pins (GPIO21=SDA, GPIO22=SCL)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Initialize Si7021 sensor
sensor = si7021.Si7021(i2c)

# Create filename with current date and time
current_time = localtime()
filename = "{:04d}{:02d}{:02d}_{:02d}{:02d}{:02d}.csv".format(
    current_time[0], current_time[1], current_time[2],
    current_time[3], current_time[4], current_time[5]
)

# Open file and write CSV header
with open(filename, 'w') as f:
    f.write("Date,Time,Temperature,Humidity\n")

# Collect data for 3 minutes (180 seconds)
start_time = current_time[5]
while (current_time[5] - start_time) < 180:
    # Read sensor data
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    
    # Get current date and time
    current_time = localtime()
    date_str = "{:04d}-{:02d}-{:02d}".format(current_time[0], current_time[1], current_time[2])
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    
    # Write to CSV file
    with open(filename, 'a') as f:
        f.write("{},{},{:.2f},{:.2f}\n".format(date_str, time_str, temperature, humidity))
    
    # Wait 15 seconds
    sleep(15)
    current_time = localtime()

# File is automatically closed when exiting the 'with' block
# Control returns to REPL