#Remove Bad Frames 1.2

# The user must first create the NoVideo reference clip prior to running this script
# for now there cannot be spaces in the library or clip names
# The library input SHOULD NOT include F:\

import os
import sys
import json
import time
import operator
import traceback
import subprocess


# Execute cv.
# If the server is not running, expect a general exception.
def syscmd(cmdline):
    stderr = subprocess.DEVNULL
    #output = subprocess.check_output(cmdline, timeout=10, stderr=stderr)
    output = subprocess.check_output(cmdline, stderr=stderr)
    return output.decode()


# Build a cv command line.
# Return 0 if 'Success' found in the response; else return -1
def cv(cmd):
    cmdline = 'cv ' + cmd
    #cmdline = 'cv /c 127.0.0.1 /t 5 /w 5 ' + cmd
    resp = syscmd(cmdline)
    print(resp)
    hdr = 'Received: Success: '
    if hdr not in resp:
        return -1
    else:
        return 0


# Function for CV commands
def servercommand(cmd):
    #cmd = 'boardtemp'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))

        
        
# Function to create .cvp file
def playlistcreator(path, COL_FAILY, TestClip, x):
    #f = open("C:/temp.cvp", "a")
    cvppath = "C:\\temp.cvp"
    if os.path.exists(cvppath):
        os.remove(cvppath)
    record = False
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if record:
                fields = line.split()
                faily = fields[10]  
                if faily == '000001':
                    frame = fields[0]
                    newcvpline = '{}\t{}\t{}\t{}\n'.format(TestClip, frame, frame, faily)
                    print(newcvpline)
                    x += 1
                    print (x)
                    f = open("C:/temp.cvp", "a")
                    f.write(newcvpline)
            elif line.startswith('Frame'):
                record = True
    return(x)
        
# Do work here
def work():
    # Get inputs
    library = sys.argv[1]
    TestClip = sys.argv[2]
    NoVideoRef = sys.argv[3]
    FailThreshold = sys.argv[4]
    COL_FAILY = 10  # zero based
    x = 0

    # Check to see that the file you want to test has less frames than the NoVideoRef sequence
    NoVideoRefSize = os.path.getsize("F:/{}/{}".format(library, NoVideoRef))
    #print(NoVideoRefSize)
    TestClipSize = os.path.getsize("F:/{}/{}".format(library, TestClip))
    #print(TestClipSize)
        
    if TestClipSize > NoVideoRefSize:
        print("The NoVideo Reference clip doesnt have enough frames.  It must have more frames than the test clip.")
        exit ()

    #commands to map clips then run PSNR test
    CVCommand = "libraryactivate F:\{}".format(library)
    servercommand(CVCommand)
    
    CVCommand = "mapa {} -1 -1 1".format(TestClip)
    servercommand(CVCommand)
    
    CVCommand = "mapb {} -1 -1 1".format(NoVideoRef)
    servercommand(CVCommand)

    CVCommand = "psnr C:\\temp.psnr {}".format(FailThreshold)
    servercommand(CVCommand)    

    #add command to delete ScrubbedSource if exists
    
    #calls function to convert .psnr to .cvp file
    path = "C:\\temp.psnr"
    x = playlistcreator(path, COL_FAILY, TestClip, x)

    servercommand("reset")
    servercommand("import C:\\temp.cvp")
    time.sleep(1)
    servercommand("mapa temp")
    time.sleep(1)
    servercommand("viewmode A")
    servercommand("videoinput ClearView 1")

    CVCommand = "record F:\{} {}_Scrubbed {} 1 0".format(library, TestClip, x)
    servercommand(CVCommand) 
    
    CVCommand = "seqdelete F:\{} temp".format(library)
    servercommand(CVCommand)
    
    print("Number of bad frames removed = {}".format(x))
    #cv delete temp command
 
 
 
 
def main():
    if len(sys.argv) != 5:
        print ("Incorrect number of arguments! \nThere should be 4")
        print ("Script.py (library without F:\) (SourceClip) (BadFrameRefClip) (PSNR Threshold)")
        return 1
    try:
        work()
        return 0
    except Exception:
        # Print a trackback of a coding error
        print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    main()
    
    