import serial
import time
import httplib
import urllib
ser = serial.Serial('/dev/ttyACM0', 9600)

data = []

while True:
    data = ser.readline().split()
    print data
    if len(data) == 3:
        a = float(data[2])
        params = urllib.urlencode({'field1': a, 'api_key': 'UVYJHTGOCMD1IGZT'})
        print params
        # headers = {"Content-type": "application/x-www-form-urlencoded",
                # "Accept": "text/plain"}
        # conn = httplib.HTTPConnection("api.thingspeak.com")
        # conn.request("GET", "/update", params)#, headers)
        # response = conn.getresponse()
        # print response.status, response.reason
        # data = response.read()
        # print data

        req = urllib.urlopen('https://api.thingspeak.com/update?' + params)
        print req.read()
        # conn.close()
        time.sleep(1)
