#import pyserial module for connection
import serial
#import time module for waiting one second
import time


try:
    #create a connection to local virtual port. This can be like "COM3" for Win>
    conn = serial.Serial("/dev/tty_dgrp_a_0", 9600)
    #send the trigger command to receive temperature value
    conn.write(b'@03S000000000096\r\n')
    #wait for one second
    time.sleep(1)
    #Read 26 characters for raw result from connection
    result_raw = conn.read(26)
    #decode raw result to utf-8
    result_hex = result_raw.decode('utf-8')
    #omit first 14 and last 10 characters to get hex temperatur value
    result_hex  =  result_hex[14:-10]
    #convert hex string to integer and extract from 0
    result = 0 - (int(result_hex, 16))
    #print temperature result
    print(result)

except serial.SerialException as e:
    #print error message if occurs
    print(e)

except serial.serial.SerialTimeoutException as e:
    #print error message if occurs
    print(e)

finally:
    #close the connection 
    conn.close()
