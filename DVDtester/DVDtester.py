#!/usr/bin/python
# python 3.4+

import subprocess
import traceback
import time


# Execute cv.
# If the server is not running, expect a general exception.
def syscmd(cmdline):
    stderr = subprocess.STDOUT
    output = subprocess.check_output(cmdline, shell=True, timeout=100, stderr=stderr)
    return output.decode()


# Build a cv command line.
# Return 0 if 'Success' found in the response; else return -1
def cv(cmd):
    cmdline = 'cv /c 127.0.0.1 /t 5 /w 5 ' + cmd
    resp = syscmd(cmdline)
    print(resp)
    hdr = 'Received: Success: '
    if hdr not in resp:
        return 1
    else:
        return 0


# Run a sequence of commands
def work():
    cmd = 'reset'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))
		
    cmd = 'libraryactivate F:\STB_Test'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))		

#    cmd = 'seqdelete F:\STB_Test\ STB_Cap'
#    if cv(cmd) < 0:
#       print('{} failed'.format(cmd))	

    result = syscmd('irclient localhost dvd2 p2')  
    print(result)  	
		
    time.sleep(30)	
		
    result = syscmd('irclient localhost dvd2 a')  
    print(result)  	

    time.sleep(3)
	
    result = syscmd('irclient localhost dvd2 down')  
    print(result)  
	
    time.sleep(3)
	
    result = syscmd('irclient localhost dvd2 enter')  
    print(result)  
	
    time.sleep(3)
	
    result = syscmd('irclient localhost dvd2 right')  
    print(result)  
	
    time.sleep(3)
	
    result = syscmd('irclient localhost dvd2 enter')  
    print(result) 

    time.sleep(3)
	
    result = syscmd('irclient localhost dvd2 down')  
    print(result) 

    time.sleep(3)

#Get rec ready

#    cmd = 'videoinput broadcast single 0 0 SDI SDI SDI'
#    if cv(cmd) < 0:
#        print('{} failed'.format(cmd))



    result = syscmd('irclient localhost dvd2 enter')  
    print(result)  

    time.sleep(3)	
	
    result = syscmd('irclient localhost dvd2 pause')  
    print(result) 
	
    result = syscmd('cv videoinput broadcast single 0 0 SDI SDI SDI')  
    print(result)  

#start rec	

#    cmd = 'cv record F:\STB_Test\ STB_Cap 600 0 0'
#    if cv(cmd) < 0:
#        print('{} failed'.format(cmd))

    time.sleep(5)
	
    result = syscmd('irclient localhost dvd2 play')  
    print(result) 
	
    result = syscmd('cv record F:\\STB_Test\\ STB_Cap 600 0 0')  
    print(result) 

    time.sleep(3)

#compare

    cmd = 'mapa Ref 0 476'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))

    cmd = 'mapb STB_Cap'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))
		
    cmd = 'autoalign 1 0'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))

#    cmd = 'psnr C:\\Users\\user\\Desktop\\STBTest_Results\\STB.psnr 40 40 40'
#    if cv(cmd) < 0:
#        print('{} failed'.format(cmd))		

    result = syscmd('cv psnr C:\\Users\\user\\Desktop\\STBTest_Results\\STB.psnr 40 40 40')  
    print(result) 


    result = syscmd('echo Test Over, Powering Down STB now')  # new <<<<<
    print(result)  # new <<<<<
	
	
	
    result = syscmd('irclient localhost dvd2 p2')  # new <<<<<
    print(result)  # new <<<<<



def main():
    try:
        work()
    except Exception:
        # Print a trackback of a coding error
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
