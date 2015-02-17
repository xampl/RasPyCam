
#Python
#Xampl
#Script to detect GPIO change on PIN for PIR sensor and perform function. 

#Import libraries
import RPi.GPIO as GPIO
import time
import os
import smtplib
import base64
import ftplib

nameSuff=int(0)
GPIO.setmode(GPIO.BCM)
PIR_PIN=7
GPIO.setup(PIR_PIN, GPIO.IN)

#Main function for action on state change
def MOTION(PIR_PIN):
        #Print to console
        print"Motion detected! SMILE!"
        #iterate number for naming
        global nameSuff
        nameSuff +=1
        #Store name of image to variable for later use
        global Name
        Name=("MACIM-" + str(nameSuff) + ".jpg")
        #Take image using rapistill
        os.system("raspistill -o " + Name)
        #ftp
        session = ftplib.FTP('FTPSERVER','USER','PASSWORD')
        # file to send
        file = open(Name,'rb')
        # send the file                          
        session.storbinary("STOR %s" % Name, file) 
        # close file and FTP     
        file.close()
         # End session                                    
        session.quit()                                 
# Print message to indicate active
print"Motion Activated Camera started(CTRL+C to exit)"
# Wait
time.sleep(2)
# Indicate ready state
print "READY"
# Add evenht to detect motion and call MOTION function
try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while 1:
                time.sleep(300)
# Add exit interrupt
except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
