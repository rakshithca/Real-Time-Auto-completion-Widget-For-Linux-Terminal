
import thread
import time
import gui2   # gui2.py contains UI code
import vfifo3  # vfifo3.py contains the code the read from fifo file
import os

# Create two threads
try:
	thread.start_new_thread( vfifo3.main, ( ) )
	thread.start_new_thread( gui2.main, ( ) )  
except:
   print ("Error: unable to start thread")


# To stop this script from closing
os.system("mkfifo d1 2> fifoerror.log")
fd = os.open('d1', os.O_RDONLY)
ch = os.read(fd,1) # No writer


