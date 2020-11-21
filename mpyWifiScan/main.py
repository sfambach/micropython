import machine
import time
import network


station = network.WLAN(network.STA_IF)
station.active(True)
n = station.scan()

print('Wifi networks around:')
for i in n:
    print(i[0])
   