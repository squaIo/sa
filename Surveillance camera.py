#importするモジュール
import RPi.GPIO as GPIO
import cv2
import time
import sys
import requests
import datetime

#LINEmessagesendfunction
url = 'https://notify-api.line.me/api/notify'
token = ' 通知したいlineのアクセストークンを記入 '
    
#カメラ準備
camera = cv2.VideoCapture(cv2.CAP_V4L2)

# ポート番号の定義
Trig = 17  #ピン番号は11ピン
Echo = 15　#ピン番号10ピン

#GPIOの設定
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

#HC-SR04で距離を測定する関数
def read_distance():
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig, GPIO.LOW)
    
    while GPIO.input(Echo) == GPIO.LOW:
        sig_off = time.time()
    while GPIO.input(Echo) == GPIO.HIGH:
        sig_on = time.time()

    duration = sig_on - sig_off
    distance = duration * 34000 / 2
    return distance

# 連続した値を超音波センサの状態を読み取る
while True:
    try:
        cm = read_distance()
        print("distance=", int(cm), "cm")
        if (cm > 2) and (cm < 400):
            print("distance=", int(cm), "cm")
        time.sleep(1)
        
        if cm < 50:
            ret, frame = camera.read()
            
            #撮影した写真の保存先設定
            dt_now = datetime.datetime.now()
            file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
               
            result = cv2.imwrite("/home/pi/Desktop/images/" + file_name + ".jpg", frame)
            print(result)
            ms_date = "何かが映り込みました"
            image = '/home/pi/Desktop/images/' + file_name + '.jpg'

            send_data = {'message': ms_date}
            headers = {'Authorization': 'Bearer ' + token}
            files = {'imageFile': open(image, 'rb')}
            
            res = requests.post(url,
                    data=send_data,
                    headers=headers,
                    files=files)
            
            print(res)
            time.sleep(10)

    except KeyboardInterrupt:
        
        camera.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()
        sys.exit()
