import dht
import machine
import utime

try:
    while True:
        utime.sleep(1)
        sen_IN = dht.DHT11(machine.Pin(16, machine.Pin.IN))
        sen_OUT = dht.DHT11(machine.Pin(17, machine.Pin.IN))
        fan = machine.Pin(15, machine.Pin.OUT)
        
        indicator_LED = machine.Pin(25, machine.Pin.OUT)
    
        sen_IN.measure()
        sen_OUT.measure()
    
        temp_diff = sen_IN.temperature() - sen_OUT.temperature()
    
    

        print(f"Inside temperature : {sen_IN.temperature()}")
        print(f"Outside temperature : {sen_OUT.temperature()}")
    
        print(f"temperature difference is {temp_diff}")
    
        if temp_diff < 2:
            fan.value(0)
            indicator_LED.value(0)
        
        elif temp_diff > 2:
            fan.value(1)
            indicator_LED.value(1)
            
        utime.sleep(10)
        
except KeyboardInterrupt:
    print(f'System will be stopped')
    