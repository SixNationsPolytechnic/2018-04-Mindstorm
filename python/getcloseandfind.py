# mvk@ca.ibm.com - program to control a lego mindstorm rover 20180526
# Follow an object
import ev3,lego
print ("Rover move comand example program")
lego.init()

print ("Using MAC = "+lego.ev3host)
lego.stop()
lego.playsound()
lego.time.sleep(1)
print (" follow and object ... get closer")
#print ("moving forward")
#lego.move(30,0)      #slow forward speed 30 no turn
#print ("sleep")
#lego.time.sleep(3)      #In Seconds
print ("moving backward")
lego.move(-30,0)
#print ("sleep")
#lego.time.sleep(3)
#print ("turn and move left")
#lego.move(30,90)     #turn left with speed 30
#lego.time.sleep(3)
#print ("turn and move right")
#lego.move(30,-100)
#lego.time.sleep(3)

#print ("turn /circle on the spot")
#lego.move(30,-200)
#lego.time.sleep(3)
speed_ctrl = ev3.PID(0, 2, half_life=0.1, gain_der=0.2)
lego.stop()
while (True):
#for i in range(3):
   lego.time.sleep(3)
   dist = lego.distance(0)
   print ("distance in mm ",dist)
   lego.stop()
   if(dist < 1000 and dist > 100):
        print(" I see object - getting closer")
#        print ("dirtance in cm ",dist/10)
#        dist = lego.distance(1)
        #print ("touch ",dist)
#        lego.time.sleep(1)
        #turn = 200
        #speed = round(speed_ctrl.control_signal(dist))
        #print("speed =",speed)
        #speed = max(-100, min(100, speed))
        #print("speed max range " ,speed)
        #lego.move(speed, turn)
        lego.move(10,0)
        lego.time.sleep(1)
        lego.stop()
   if(dist <100):
        print("I am close to object")
   if(dist > 1000):
       print(" I lost object")
       print(" Turing trying to fing it")
       lego.move(30, 100)
       lego.time.sleep(0.15)
       lego.stop()
         



lego.ledgreenflash()
lego.time.sleep(3)
lego.ledoff()
lego.stop()
print ("program done")
