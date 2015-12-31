import time
import pi2go

pi2go.init()

speed = 30 

dist = pi2go.getDistance() 

if dist > 5 :
	pi2go.forward(speed)
elif dist < 5 :
	pi2go.stop()
else : 
	print ( dist )

		