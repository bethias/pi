import time
import pi2go

pi2go.init()

speed = 40
fast = 60

dist = pi2go.getDistance()

def dance():
	for i in range(5):
		pi2go.forward(fast)
		time.sleep(1.5)
		pi2go.spinLeft(speed)
		time.sleep(1)
		pi2go.reverse(fast)
		time.sleep(1.5)
		pi2go.spinRight(speed)
		time.sleep(1)

def lights():
	for j in range(10):
		pi2go.setAllLEDs(0, 255, 0)
		time.sleep(0.5)
		pi2go.setAllLEDs(255, 0 , 0)
		time.sleep(0.5)
		pi2go.setAllLEDs(0, 0, 255)
		time.sleep(0.5)
		
if dist	> 5: 	
	dance()		
else: 
	lights()
	pi2go.spinLeft(speed)

pi2go.cleanup()
