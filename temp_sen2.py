import dht
import machine
import utime

# except case 전까지 무한 반복
try:
    while True:
        utime.sleep(1)
        # 내,외부 온도센서와 LED, 팬에 핀 할당
        sen_IN = dht.DHT11(machine.Pin(16, machine.Pin.IN))
        sen_OUT = dht.DHT11(machine.Pin(17, machine.Pin.IN))
        fan = machine.Pin(15, machine.Pin.OUT)
        
        indicator_LED = machine.Pin(25, machine.Pin.OUT)
        
        # 온도 센서가 값을 측정
        sen_IN.measure()
        sen_OUT.measure()
    
        
        temp_diff = sen_IN.temperature() - sen_OUT.temperature()
    
    

        print(f"Inside temperature : {sen_IN.temperature()}")
        print(f"Outside temperature : {sen_OUT.temperature()}")
    
        print(f"temperature difference is {temp_diff}")
        
        # 임의의 온도차(2도)를 팬의 작동 조건으로 설정
        if temp_diff < 2:
            fan.value(0)
            indicator_LED.value(0)
        
        elif temp_diff > 2:
            fan.value(1)
            indicator_LED.value(1)
            
        utime.sleep(10)
        
# ctrl+c 입력으로 프로그램 종
except KeyboardInterrupt:
    print(f'System will be stopped')
    