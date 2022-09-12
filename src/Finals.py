import cv2
import numpy as np
import Sonar_Trigger_Echo
from Motor_control_function import *
from Tool_function import tools
import time
from TCS34725 import TCS34725
import pickle
import threading

tcs34725 = TCS34725()
Motor = Motor_control(23, 24, 19, 15, 3)
tool = tools()

color_detect_mode = 'HSV'
green_intersection_x = 380
red_intersection_x = 100
k = 0
kernal = np.ones((4, 4), np.uint8)
run = True
line_count = 0
direction_angle = [0, 90, 180, 270]
color = 0
black_dodge_angle = 35
line_middle = 0
line_count = 0
color_direction_middle = 0
round_count = 0
reverse = True
direction_time = 0

def color_direction():
    global line_middle, color_direction_middle, white_color
    with open('/home/pi/Desktop/final/save_file/color_sensor.p', mode='rb') as f:
        file = pickle.load(f)
    blue_color = file['Blue']
    orange_color = file['Orange']
    white_color = file['white']
    color_direction_middle = (blue_color + orange_color) / 2 + 3
    line_middle = (white_color + orange_color) / 2 - 5
    print('orange:' + str(orange_color))
    print('blue:' + str(blue_color))
    print('white:' + str(white_color))
    print('direction_middle:', color_direction_middle)
    print('line middle:', line_middle)
    print('=======================')
    
def color_read():
    global color
    print('color start')
    while run:
        color = tcs34725.readluminance()['c']
        time.sleep(0.01)

    
def red_green_dodge(kp, kd, last_error):
    global reverse
    if green_x == -1 and red_x == -1:
        error = 0
        servo_angle = direction * -1
        servo_angle = tool.constrain(servo_angle, -50, 50)
    elif green_x > 0 and red_x > 0:
        if reverse == True:
            if green_x > red_x:
                error = green_x - green_intersection_x
                servo_angle = error * kp
                servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
            else:
                error = red_x - red_intersection_x
                servo_angle = error * kp
                servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
        else:
            if green_x < red_x:
                error = green_x - green_intersection_x
                servo_angle = error * kp + (error - last_error) * kd
                servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
            else:
                error = red_x - red_intersection_x
                servo_angle = error * kp + (error - last_error) * kd
                servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
    else:
        if green_y > red_y:
            if green_count >= 2 and green_x < 350:
                if green_y > 180:
                    error = green_x - green_intersection_x
                    servo_angle = error * kp + (error - last_error) * kd
                    servo_angle = tool.constrain(servo_angle, -20, 20)
                else:
                    error = 0
                    servo_angle = direction * -1
                    servo_angle = tool.constrain(servo_angle, -30, 30)
            else:
                if green_x > 380 and green_y > 200:
                    error = 0
                    servo_angle = direction * -1
                    servo_angle = tool.constrain(servo_angle, -30, 30)
                else:
                    error = green_x - green_intersection_x
                    servo_angle = error * kp + (error - last_error) * kd
                    servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
        else:
            if red_count >= 2 and red_x > 130:
                if red_y > 180:
                    error = red_x - red_intersection_x
                    servo_angle = error * kp + (error - last_error) * kd
                    servo_angle = tool.constrain(servo_angle, -25, 25)
                else:
                    error = 0
                    servo_angle = direction * -1
                    servo_angle = tool.constrain(servo_angle, -30, 30)
            else:
                if red_x < 100 and red_y > 200:
                    error = 0
                    servo_angle = direction * -1
                    servo_angle = tool.constrain(servo_angle, -30, 30)
                else:
                    error = red_x - red_intersection_x
                    servo_angle = error * kp + (error - last_error) * kd
                    servo_angle = tool.constrain(servo_angle, -black_dodge_angle, black_dodge_angle)
    control_power = -50 - abs(servo_angle) * 0.3
    control_power = tool.constrain(control_power, -55, 0)
    Motor.DC(control_power)
    Motor.Servo (servo_angle)
    return error

def read_file(mode):
    print('Mode:' + str(mode))
    if mode == 'HSV':
        Green_path = '/home/pi/Desktop/final/save_file/HSV_Green.p'
        Red_path = '/home/pi/Desktop/final/save_file/HSV_Red.p'
        image_to_color = cv2.COLOR_BGR2HSV
    elif mode == 'HLS':
        Green_path = '/home/pi/Desktop/final/save_file/HLS_Green.p'
        Red_path = '/home/pi/Desktop/final/save_file/HLS_Red.p'
        image_to_color = cv2.COLOR_BGR2HLS
    else:
        print("Detect Mode Error")
        exit()
    with open(Green_path, mode='rb') as f:
        file = pickle.load(f)
    G_Lower = file['Lower']
    G_Upper = file['Upper']
    with open(Red_path, mode='rb') as f:
        file = pickle.load(f)
    R_Lower = file['Lower']
    R_Upper = file['Upper']
    print('Green_Lower:' + str(G_Lower))
    print('Green_Upper:' + str(G_Upper))
    print('Red_Lower:' + str(R_Lower))
    print('Red_Uppwe:' + str(R_Upper))
    red_lower = np.array(R_Lower, np.uint8) 
    red_upper = np.array(R_Upper, np.uint8)
    green_lower = np.array(G_Lower, np.uint8)
    green_upper = np.array(G_Upper, np.uint8)
    return green_lower, green_upper, red_lower, red_upper, image_to_color

def color_detect(img, hsv, lower, upper, kernal, color):
    red_mask = cv2.inRange(hsv, lower, upper)  
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x1 = -1
    y1 = -1
    intersection_x = -1
    max_y = 0
    count = 0
    _area = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        x = int(x + w / 2)
        y = int(y + h / 2)
        if area > 200:
            count += 1
        if y > max_y and area > 200:
            _area = area
            max_y = y
            x1 = x
            y1 = y
    cv2.circle(img, (x1, y1), 5, (0, 0, 0), -1)
    return x1, y1, _area, count

def block_detect():
    global green_x, green_y, green_count, green_intersection_x, red_intersection_x, red_x, red_y, red_count, run
    print('blcok start')
    while run:
        img = read_img.copy()
        img[0:150, 0:480] = [0, 0, 0]
        hsv = cv2.cvtColor(img, to_color)
        red_x, red_y, red_area, red_count = color_detect(img , hsv, red_lower, red_upper, kernal, (0, 0, 255))
        green_x, green_y, green_area, green_count = color_detect(img , hsv, green_lower, green_upper, kernal, (0, 255, 0))
        cv2.line(img, (red_intersection_x, 0), (red_intersection_x, 360), (0, 0, 255),2)
        cv2.line(img, (green_intersection_x, 0), (green_intersection_x, 360), (0, 255, 0),2)
        cv2.imshow('face_detect', img)
    
    cv2.destroyAllWindows()
    
def get_camera():
    global read_img, k
    print('cmaera start')
    while run:
        _, read_img = imcap.read()
        k = cv2.waitKey(25) & 0xFF
    imcap.release()
    
def DC_control():
    global k
    while run:
        if k == 82:
            Motor.DC(power)
        elif k == 84:
            Motor.DC(0)
        time.sleep(0.01)

def line_detect():
    global line_count, color, line_middle, color_direction_middle, round_count, direction_angle, reverse, direction
    time.sleep(0.01)
    in_line = False
    while color > line_middle:
        time.sleep(0.001)
    low = 100
    while color < line_middle:
        if color < low:
            low = color
    if low > color_direction_middle:
        reverse = False
        print('orange line')
        print('color_low',low)
        direction_angle = [0, -93, -183, -273]
    else:
        print('blue line')
        print('color_low',low)
    line_count = 1
    print('round:', round_count, 'line:', line_count)
    time.sleep(0.001)
    if reverse == True:
        while run:
            while color > line_middle:
                time.sleep(0.001)
            low = 100
            while color < line_middle:
                if color < low:
                    low = color
            if low < color_direction_middle:
                print('blue line')
                print('color_low',low)
                if line_count + 1 == 4:
                    line_count = 0
                    round_count += 1
                else:
                    line_count += 1
                time.sleep(0.5)
                print('round:', round_count, 'line:', line_count)
    else:
        while run:
            while color > line_middle:
                time.sleep(0.001)
            low = 100
            while color < line_middle:
                if color < low:
                    low = color
            if low > color_direction_middle:
                print('orange line')
                if line_count + 1 == 4:
                    line_count = 0
                    round_count += 1
                else:
                    line_count += 1
                time.sleep(0.5)
                print('round:', round_count, 'line:', line_count)
#main==============================================================
pi.set_mode(20, pigpio.OUTPUT)
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(14, pigpio.INPUT)
pi.write(21, 0)
pi.write(20, 0)

if bno.begin() is not True:
    print("Error initializing device")
    exit()
time.sleep(1)
bno.setExternalCrystalUse(True)

Motor.DC(0)
Motor.Servo(0)
imcap = cv2.VideoCapture(0)
imcap.set(3, 480) # set width as 640 480
imcap.set(4, 360) # set height as 480 360
imcap.set(cv2.CAP_PROP_FPS, 40)
imcap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
imcap.set(cv2.CAP_PROP_BRIGHTNESS, 55)
imcap.set(cv2.CAP_PROP_EXPOSURE, 0)
if not imcap.isOpened():
    print("Cannot open camera")
    exit()
_, read_img = imcap.read()


thread_0 = threading.Thread(target = block_detect)
thread_1 = threading.Thread(target = line_detect)
thread_2 = threading.Thread(target = color_read)
thread_4 = threading.Thread(target = DC_control)
thread_5 = threading.Thread(target = get_camera)

green_lower, green_upper, red_lower, red_upper, to_color = read_file(color_detect_mode)

print('Threading============')
thread_5.start()
thread_0.start()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

time.sleep(0.5)

print('waiting start============')
color_direction()
button = 0
direction_check = False
to_quick = False
kd = -400
kp = 0.3
led_state = False
flash_reset = time.time()
while button == 0 and k != ord('w') and k != 27:
    button = pi.read(14)
    if time.time() - flash_reset > 0.5:
        flash_reset = time.time()
        if led_state == True:
            pi.write(21, 0)
            led_state = False
        else:
            pi.write(21, 1)
            led_state = True
    time.sleep(0.01)
pi.write(21, 1)
button = 1
while button == 1:
    button = pi.read(14)
    time.sleep(0.01)
    
try:
    error = 0
    button = 0
    while True:
        button = pi.read(14)
        error = red_green_dodge(kp, kd, error)
        if k == 27 or (line_count == 0 and round_count == 3) or button == 1:
            break
    if k != 27 and button != 1:
        finish = time.time()
        while time.time() - finish < 2:
            error = red_green_dodge(kp, kd, error)
            
finally:
    run = False
    pi.write(21, 0)
    pi.write(20, 0)
    pi.write(16, 0)
    Motor.DC(0)
