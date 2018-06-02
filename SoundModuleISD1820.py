# Need to access the hardware pins
import RPi.GPIO as GPIO

# Used to delay things
import time

#Declare the output pin
enablePin = 22

try:
    while True:
		#Set the pin numbering mode to BCM (not BOARD)
        GPIO.setmode(GPIO.BCM)
		
		# Output mode for that pin
        GPIO.setup(enablePin, GPIO.OUT)
		
		# Set it high
        GPIO.output(enablePin, 1)
		
		# Sleep for one second
        time.sleep(1)
		
		# Set the pin low
        GPIO.output(enablePin, 0)
		
		# Sleep for 15 seconds (see video for full description)
        for cnt in range(1, 30):
            time.sleep(0.5)

			# CTRL-C key handler        
except KeyboardInterrupt:
    print ("Program terminated")
	
	#Set the GPIO pins back to original state
    GPIO.cleanup()
