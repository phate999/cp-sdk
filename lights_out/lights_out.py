# lights out - turn off E-Series light bar
from csclient import EventingCSClient
import time
cp = EventingCSClient('lights_out')
cp.log('Starting...')
lights_out = {"LED_BAR_0": 0, "LED_BAR_1": 0, "LED_BAR_2": 0, "LED_BAR_3": 0,
              "LED_BAR_4": 0, "LED_BAR_5": 0, "LED_BAR_6": 0, "LED_BAR_7": 0,
              "LED_BAR_8": 0, "LED_BAR_9": 0, "LED_BAR_10": 0, "LED_BAR_11": 0,
              "LED_BAR_12": 0, "LED_BAR_13": 0, "LED_BAR_14": 0}
while True:
    cp.put('control/gpio', lights_out)
    time.sleep(1)
