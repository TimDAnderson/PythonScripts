import os
import sys
import json
import operator
import traceback
import subprocess

# path to config.json file
#CWD = os.getcwd()  <- old but don't remove
CWD = "F:/Dropbox/jobs/ready/"
JSON_FILE = sys.argv[1]

#remove .json extension
JSON_FILE.partition('.')
FILENAME, Seperator, EXTENSION = JSON_FILE.partition('.')
print(FILENAME)
LIBPATH = "F:\\{}".format(FILENAME)

#create library
if not os.path.exists(LIBPATH):
    os.makedirs(LIBPATH)
    SequencesFile = open("{}\\sequences".format(LIBPATH), "w+")
    SequencesFile.close()

    

def work():
    # Dictionary holding config.json
    path = '%s/%s' % (CWD, JSON_FILE)
    with open(path) as f:
        props = json.load(f)

    # Get and store user's email
    USER_EMAIL = (props['report_owner'])
    print(USER_EMAIL)
	
	
    # Get first file name
    #print (props['purchase_units'][0]['items'][0]['name'])
    
    #Create output text file for probe information
    ProbeInput = open("F:\\{}.txt".format(USER_EMAIL), "w+")
    ProbeInput.write("{}\n".format(USER_EMAIL))	
    ProbeInput.write("{}\n".format(FILENAME))
    
    
    #Create output text file for CV\Blake's script (library, seq1, seq2, ...)
    ClearViewInput = open("F:\\{}.txt".format(FILENAME), "w+")
    ClearViewInput.write("F:\{}".format(FILENAME))
    
    
    
    #create dictionary to sort name and file size
    jsondict = {}
    
    
    
    
    # Dictionary is built
    
    for item in props['purchase_units'][0]['items']:
        name = item['name']
        print(name)

        
        #get file size
        filesize = os.path.getsize("F:/Dropbox/home/{}/video/{}".format(USER_EMAIL, name))
        
        print(filesize)
        
        jsondict[name]=filesize
        

    # Dictionary is sorted 
    print(jsondict)
    sorted_d = sorted(jsondict.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_d)
    
    
    #import/probe all items in dictionary
    for components in sorted_d:
        print(components)
        
        name, filesize = components 
        print(name)
        
        name.partition('.')
        VIDEOFILE, Seperator2, VidExtension = name.partition('.')
        print(VIDEOFILE)
        
        
        #imports the file
        command = "cvi.exe -source F:\\Dropbox\\home\\{}\\video\\{} -library F:\\{} -sequence {}".format(USER_EMAIL, name, FILENAME, VIDEOFILE)
        os.system(command)       
        
  

        #Write to output text file for CV\Blake's script
        ClearViewInput = open("F:\\{}.txt".format(FILENAME), "a")
        ClearViewInput.write(" {}".format(VIDEOFILE))  
        
        #prints probe info
        ProbeCommand = "cvi.exe -source F:\\Dropbox\\home\\{}\\video\\{} -probe 1".format(USER_EMAIL, name)
        ProbeOutput = subprocess.check_output(ProbeCommand, shell=True, universal_newlines=True)
        ProbeInput = open("F:\\{}.txt".format(USER_EMAIL), "a")
        ProbeInput.write("\n\n\n{}".format(ProbeOutput))        
        
    

    
def main():
    try:
        work()
    except Exception as e:
        traceback.print_exc()
        print(e)

if __name__ == '__main__':
    main()


