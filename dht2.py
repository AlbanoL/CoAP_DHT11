 # **********************************************************************
 # ORGANIZATION  :  UFRJ / COPPE / PESC
 # PROJECT       :  CPS731 :: IoT Lab
 # FILENAME      :  dht.py
 #
 # This file is an implementation work, part of a postgraduate course.
 # Course website (PT-BR):  https://sites.google.com/cos.ufrj.br/lab-iot
 # **********************************************************************
 # 
 # This code was written based on the Adafruit_Python_DHT project
 # examples (https://github.com/adafruit/Adafruit_Python_DHT).

import sys
import Adafruit_DHT

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./dht.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./dht.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('{'+'"temperature":{0:0.0f},"humidity":{1:0.1f}'.format(temperature, humidity)+'}')
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
