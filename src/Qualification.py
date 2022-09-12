import time
import pigpio
import Sonar_Trigger_Echo
from Motor_control_function import *
import threading
from Tool_Function import tools
from TCS34725 import TCS34725
import pickle

pi = pigpio.pi()
tool = tools()
sonar = Sonar_Trigger_Echo.ranger(pi, 8, 7)
Motor = Motor_control(23, 24, 19, 15, 3)
tcs34725 = TCS34725()


direction = 180
end = True
line_count = 0
count = 0
turn_dis = 50
middle_value = 0
start = pi.read(14)
button = False
dis = 1000
        
def color_read():
    global middle_value
    with open('/home/pi/Desktop/qualification/save_file/color_sensor.p', mode='rb') as f:
        file = pickle.load(f)
    blue_color = file['Blue']
    orange_color = file['Orange']
    middle_value = (blue_color + orange_color) / 2
    print('orange:' + str(orange_color))
    print('blue:' + str(blue_color))
    print('middle:' + str(middle_value))

def get_color():
    global direction, line_count, middle_color
    color = 100
    while color > 45:
        direction = direction_read(0)
        color = tcs34725.readluminance()['c']
        time.sleep(0.01)
    color = 0
    get_color = 100
    while color < 50:
        color = tcs34725.readluminance()['c']
        if get_color > color:
            get_color = color
        time.sleep(0.01)
#     print(get_color)
    if get_color < middle_value:
        print('left turn')#
        print('')
        turn_dis = 37
        angle = [0, 87, 177, 267]
    else:
        print('right turn')#
        turn_dis = 37
        angle = [0, -93, -183, -273]
    while end:
        direction = direction_read(angle[line_count])
        time.sleep(0.01)
        
def get_dis():
    global dis
    print('Dis_start')
    while end:
        dis = sonar.read()/58.2
        time.sleep(0.01)
    print(dis)

pi.set_mode(20, pigpio.OUTPUT)
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(16, pigpio.OUTPUT)
pi.set_mode(14, pigpio.INPUT)
pi.write(21, 0)
pi.write(20, 0)
pi.write(16, 0)

Motor.Servo(0)

if bno.begin() is not True:
    print("Error initializing device")
    exit()
time.sleep(1)
bno.setExternalCrystalUse(True)
color_read()
print('start')

thread_0 = threading.Thread(target = get_color)
thread_1 = threading.Thread(target = get_dis)
thread_0.start()
thread_1.start()

start = 0
led_reset = time.time()
led_state = False
while start == 0:
    start = pi.read(14)
    if time.time() - led_reset > 0.7:
        if led_state == True:
            pi.write(21, 0)
            led_state = False
            led_reset = time.time()
        else:
            pi.write(21, 1)
            led_state = True
            led_reset = time.time()
    time.sleep(0.01)

try:
    for count in range(12):
        Motor.DC(-55)
        print('count:' + str(line_count))
        start = time.time()
        while time.time() - start < 0.5:
            servo_angle = tool.constrain(-direction, -35, 35)
            Motor.Servo(servo_angle)
        while direction > 10 or direction < -10:
            servo_angle = tool.constrain(-direction, -35, 35)
            Motor.Servo(servo_angle)
        while dis > 50:
            servo_angle = tool.constrain(-direction, -35, 35)
            Motor.Servo(servo_angle)
            time.sleep(0.01)
        print('Turn Dis:', dis)
        line_count += 1
        if line_count == 4:
            count += 1
            line_count = 0
#         -----------------
    line_count = 0
    start = time.time()
    while time.time() - start < 0.5:
        servo_angle = tool.constrain(-direction, -35, 35)
        Motor.Servo(servo_angle)
    while direction > 10 or direction < -10:
        servo_angle = tool.constrain(-direction, -35, 35)
        Motor.Servo(servo_angle)
    start = time.time()
    while time.time() - start < 1:
        servo_angle = tool.constrain(-direction, -35, 35)
        Motor.Servo(servo_angle)
    
    end = False
    Motor.DC(0)
    
    
finally:
    pi.write(21, 0)
    pi.write(20, 0)
    pi.write(16, 0)
    Motor.DC(0)
    sonar.cancel()
    pi.stop()
