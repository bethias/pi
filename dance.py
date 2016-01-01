import time
import pi2go

#struct = localtime(start_timer)

pi2go.init()

speed = 40
fast = 60

dist = pi2go.getDistance()

counter = 0

#def dance():
#	for i in range(5):
#		pi2go.forward(fast)
#		time.sleep(1.5)
#		pi2go.spinLeft(speed)
#		time.sleep(2)
#		pi2go.reverse(fast)
#		time.sleep(1.5)
#		pi2go.spinRight(speed)
#		time.sleep(2)

#def lights():
	#for j in range(10):
	#	pi2go.setAllLEDs(0, 255, 0)
	#	time.sleep(0.5)
	#	pi2go.setAllLEDs(255, 0 , 0)
	#	time.sleep(0.5)
	#	pi2go.setAllLEDs(0, 0, 255)
	#	time.sleep(0.5)

#print ("\nTime Now: " , strftime("%X" , struct))

while dist > 7:
	pi2go.forward(speed)
		if False:
			pi2go.spinLeft(speed)
			time.sleep(2)
			continue
		if counter > 50:
			pi2go.stop()
			break
	counter += 1
		
#if dist > 5: 	
#	dance()		
#else:
#	pi2go.stop()	

pi2go.cleanup()