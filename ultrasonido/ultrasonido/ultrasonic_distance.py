import os
import stat
from gpiozero import DistanceSensor
from time import sleep

#                  (echo,trigger) 
sensor1=DistanceSensor(26,19,queue_len=1)
sensor2=DistanceSensor(6,5,queue_len=1)
sensor3=DistanceSensor(21,20,queue_len=1)
os.chmod('test.txt', stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
def distance():
    distance=sensor1.distance*100
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f m" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()