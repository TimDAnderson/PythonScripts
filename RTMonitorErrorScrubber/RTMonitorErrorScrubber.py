import os
import sys
import subprocess


# need to get inputs to script
# Current RTMLog directory
rtmLogDir = sys.argv[1]
print("The current RTMLog dir is {}".format(rtmLogDir))
# new RTMLog directory for 'scrubbed' results
newRtmLogDir = sys.argv[2]
print("The scrubbed errors will be moved to {}".format(newRtmLogDir))
if not os.path.exists(newRtmLogDir):
    os.makedirs(newRtmLogDir)


# empty dmos array
dmosFileArray = []
# empty psnr array
psnrFileArray = []


def syscmd(cmdline):
    stderr = subprocess.DEVNULL
    # output = subprocess.check_output(cmdline, timeout=10, stderr=stderr)
    output = subprocess.check_output(cmdline, stderr=stderr)
    return output.decode()


# Build a cv command line.
# Return 0 if 'Success' found in the response; else return -1
def cv(cmd):
    cmdline = 'cv ' + cmd
    # cmdline = 'cv /c 127.0.0.1 /t 5 /w 5 ' + cmd
    resp = syscmd(cmdline)
    print(resp)
    global cvOutputVariable
    cvOutputVariable = resp
    hdr = 'Received: Success'
    if hdr not in resp:
        return -1
    else:
        return 0


# Function for CV commands
def servercommand(cmd):
    # cmd = 'boardtemp'
    if cv(cmd) < 0:
        print('{} failed'.format(cmd))


"""

logPath = "F:\RTM1\RTMLog\__FR029615__00_08_14_05___2020_07_21_14_18_22.dmos"
yThreshold = "3"
midFrame = "40"
midMinus5 = "35"
midPlus5 = "45"
lastFrame = "80"
aSequence = "Ref_2020_07_21_14_18_22"
bSequence = "Test_2020_07_21_14_18_22"
#rtmLogDir
#newRtmLogDir
"""

def errorScrubber(logPath, yThreshold, midFrame, midMinus5, midPlus5, lastFrame, aSequence, bSequence, rtmLogDir, newRtmLogDir, dmosErrors):
    CVCommand = "reset"
    servercommand(CVCommand)

    CVCommand = "import {}".format(logPath)
    servercommand(CVCommand)

    CVCommand = "inout 1 {} {}".format(midFrame, lastFrame)
    servercommand(CVCommand)

    CVCommand = "autoalign 1 0 0"
    servercommand(CVCommand)

    print(cvOutputVariable)
    newArray = cvOutputVariable.split(" ")
    print(newArray)
    print(newArray[12])

    # if offset hasn't changed then bail out of this
    # if (newArray[12] == "0"):
    #    print("bailing out, file is fine")
    #    return

    # rerun psnr
    CVCommand = "psnr C:\\temp.psnr"
    servercommand(CVCommand)

    # grab results  from C:\temp.psnr for mid, mid minus 5 and mid plus 5
    # logPath = "C:/temp.psnr"
    with open("C:/temp.psnr", 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            midpoint check
            if midFrame in line:
                print(line)
                y = line.split(" ")
                print(y[0])
                if midFrame in y[0]:
                    print("we found the mid point line")
                    newMidPointValue = y[1]
            if midMinus5 in line:
                print(line)
                y = line.split(" ")
                print(y[0])
                if midMinus5 in y[0]:
                    print("we found the mid minus 5 line")
                    newMidMinus5Value = y[1]
            if midPlus5 in line:
                print(line)
                y = line.split(" ")
                print(y[0])
                if midPlus5 in y[0]:
                    print("we found the mid plus 5 line")
                    newMidPlusValue = y[1]

    print("After realigning the score at the mid point is {}".format(newMidPointValue))
    print("After realigning the score 5 frames before the mid point is {}".format(newMidMinus5Value))
    print("After realigning the score 5 frames after the mid point is {}".format(newMidPlusValue))

    # if new results are below dmos threshold move the .dmos log to new directory
    # convert strings to numbers for comparisson tests
    yThresholdNum = float(yThreshold)
    newMidPointValueNum = float(newMidPointValue)
    newMidMinus5ValueNum = float(newMidMinus5Value)
    newMidPlusValueNum = float(newMidPlusValue)

    print(yThresholdNum)
    print(newMidPointValueNum)
    print(newMidMinus5ValueNum)
    print(newMidPlusValueNum)

    # if all three new values are below the threshold then move the .dmos log to new directory
    if (newMidPointValueNum > yThresholdNum):
        if (newMidMinus5ValueNum > yThresholdNum):
            if (newMidPlusValueNum > yThresholdNum):
                # move the file to new location
                newLogPath = "{}\\{}".format(newRtmLogDir, psnrErrors)
                os.rename(logPath, newLogPath)
                return

    return
	
	
	
	
	
#PSNR Version
def errorScrubberPSNR(logPath, yThreshold, midFrame, midMinus5, midPlus5, lastFrame, aSequence, bSequence, rtmLogDir, newRtmLogDir, psnrErrors):
    CVCommand = "reset"
    servercommand(CVCommand)

    CVCommand = "import {}".format(logPath)
    servercommand(CVCommand)

    CVCommand = "inout 1 {} {}".format(midFrame, lastFrame)
    servercommand(CVCommand)

    CVCommand = "autoalign 1 0 0"
    servercommand(CVCommand)

    print(cvOutputVariable)
    newArray = cvOutputVariable.split(" ")
    print(newArray)
    print(newArray[12])

    # if offset hasn't changed then bail out of this
    # if (newArray[12] == "0"):
    #    print("bailing out, file is fine")
    #    return

    # rerun dmos
    CVCommand = "dmos C:\\temp.dmos"
    servercommand(CVCommand)

    # grab results  from C:\temp.dmos for mid, mid minus 5 and mid plus 5
    # logPath = "C:/temp.dmos"
    with open("C:/temp.dmos", 'r') as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            # midpoint check
            if midFrame in line:
                # print(line)
                y = line.split(" ")
                # print(y[0])
                if midFrame in y[0]:
                    print("we found the mid point line")
                    newMidPointValue = y[1]
            if midMinus5 in line:
                # print(line)
                y = line.split(" ")
                # print(y[0])
                if midMinus5 in y[0]:
                    print("we found the mid minus 5 line")
                    newMidMinus5Value = y[1]
            if midPlus5 in line:
                # print(line)
                y = line.split(" ")
                # print(y[0])
                if midPlus5 in y[0]:
                    print("we found the mid plus 5 line")
                    newMidPlusValue = y[1]

    print("After realigning the score at the mid point is {}".format(newMidPointValue))
    print("After realigning the score 5 frames before the mid point is {}".format(newMidMinus5Value))
    print("After realigning the score 5 frames after the mid point is {}".format(newMidPlusValue))

    # if new results are below dmos threshold move the .dmos log to new directory
    # convert strings to numbers for comparisson tests
    yThresholdNum = float(yThreshold)
    newMidPointValueNum = float(newMidPointValue)
    newMidMinus5ValueNum = float(newMidMinus5Value)
    newMidPlusValueNum = float(newMidPlusValue)

    print(yThresholdNum)
    print(newMidPointValueNum)
    print(newMidMinus5ValueNum)
    print(newMidPlusValueNum)

    # if all three new values are below the threshold then move the .dmos log to new directory
    if (newMidPointValueNum < yThresholdNum):
        if (newMidMinus5ValueNum < yThresholdNum):
            if (newMidPlusValueNum < yThresholdNum):
                # move the file to new location
                newLogPath = "{}\\{}".format(newRtmLogDir, dmosErrors)
                os.rename(logPath, newLogPath)
                return

    return




# create a loop to iterate through all files in RTMLog directory
# add dmos files to a tempDmos array
# add psnr files to a tempPsnr array

for filename in os.listdir(rtmLogDir):
    if filename.endswith(".dmos"):
        print(filename)
        dmosFileArray.append(filename)
    elif filename.endswith(".psnr"):
        print(filename)
        psnrFileArray.append(filename)

print(dmosFileArray)
print(psnrFileArray)

# create two loops for dmos and psnr that do the following
'''
identify the following information from log file
Y threshold
first frame
last frame
middle frame
middle + 5 frames
middle - 5 frames
'''


for psnrErrors in psnrFileArray:
    #print(psnrErrors)
    # iterate through psnr file and pull out information we need
    #f = open({}\psnrErrors.forma
    #t(rtmLogDir), 'r')
    print("{}\{}".format(rtmLogDir, psnrErrors))
    logPath = "{}\{}".format(rtmLogDir, psnrErrors)
    with open(logPath, 'r') as f:
        runningDmos = False
        lines = f.readlines()
        for line in lines:
            #print(line)
            if line.startswith("Threshold Y:"):
                #print(line)
                x = line.split(": ")
                yThreshold = x[1]
                #print (yThreshold)
            elif line.startswith("First Frame A:"):
                #print(line)
                x = line.split(": ")
                firstFrame = x[1]
                #print (firstFrame)
            elif line.startswith("Last Frame A:"):
                #print(line)
                x = line.split(": ")
                lastFrame = x[1]
            elif line.startswith("Sequence A:"):
                #print(line)
                x = line.split(": ")
                aSequence = x[1]
            elif line.startswith("Sequence B:"):
                #print(line)
                x = line.split(": ")
                bSequence = x[1]

    print(aSequence)
    print(bSequence)
    print("The Y threshold is {}".format(yThreshold))
    print("The first frame is {}".format(firstFrame))
    print("The last frame is {}".format(lastFrame))
    midFrameInt = round(int(lastFrame) / 2)
    midMinus5Int = midFrameInt - 5
    midPlus5Int = midFrameInt + 5
    midFrame = str(midFrameInt)
    midMinus5 = str(midMinus5Int)
    midPlus5 = str(midPlus5Int)
    print(midFrame)
    print(midMinus5)
    print(midPlus5)
    #call the error scrubber function and give it lots of inputs
    errorScrubberPSNR(logPath, yThreshold, midFrame, midMinus5, midPlus5, lastFrame, aSequence, bSequence, rtmLogDir, newRtmLogDir, psnrErrors)



for dmosErrors in dmosFileArray:
    #print(dmosErrors)
    # iterate through dmos file and pull out information we need
    #f = open({}\dmosErrors.forma
    #t(rtmLogDir), 'r')
    print("{}\{}".format(rtmLogDir, dmosErrors))
    logPath = "{}\{}".format(rtmLogDir, dmosErrors)
    with open(logPath, 'r') as f:
        runningDmos = True
        lines = f.readlines()
        for line in lines:
            #print(line)
            if line.startswith("Threshold Y:"):
                #print(line)
                x = line.split(": ")
                yThreshold = x[1]
                #print (yThreshold)
            elif line.startswith("First Frame A:"):
                #print(line)
                x = line.split(": ")
                firstFrame = x[1]
                #print (firstFrame)
            elif line.startswith("Last Frame A:"):
                #print(line)
                x = line.split(": ")
                lastFrame = x[1]
            elif line.startswith("Sequence A:"):
                #print(line)
                x = line.split(": ")
                aSequence = x[1]
            elif line.startswith("Sequence B:"):
                #print(line)
                x = line.split(": ")
                bSequence = x[1]

    print(aSequence)
    print(bSequence)
    print("The Y threshold is {}".format(yThreshold))
    print("The first frame is {}".format(firstFrame))
    print("The last frame is {}".format(lastFrame))
    midFrameInt = round(int(lastFrame) / 2)
    midMinus5Int = midFrameInt - 5
    midPlus5Int = midFrameInt + 5
    midFrame = str(midFrameInt)
    midMinus5 = str(midMinus5Int)
    midPlus5 = str(midPlus5Int)
    print(midFrame)
    print(midMinus5)
    print(midPlus5)
    #call the error scrubber function and give it lots of inputs
    errorScrubber(logPath, yThreshold, midFrame, midMinus5, midPlus5, lastFrame, aSequence, bSequence, rtmLogDir, newRtmLogDir, dmosErrors)