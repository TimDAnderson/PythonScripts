#PFSPD Import Script
#Tim Anderson 07/30/19

import os
import sys
import subprocess

#The python script takes in 1 argument, the name of the yuv file
YUV_File = sys.argv[1]


#remove .yuv extension
YUV_File.partition('.')
FILENAME, Seperator, EXTENSION = YUV_File.partition('.')
print(FILENAME)

#store size of YUV file
CWD = os.getcwd()
print ('Current directory', CWD)
filesize = os.path.getsize("{}/{}".format(CWD, YUV_File))
print ('YUV byte total', filesize)

#Run Pfspd_Hdr.exe which outputs a string
proc = subprocess.Popen('Pfspd_Hdr.exe {}'.format(YUV_File), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
HdrOutput = proc.stdout.read()
output_str = HdrOutput.decode('utf-8')  # decode "bytes" to "string" 

#parse
var_list = output_str.split('=')  # list of the split: value should be 2nd in list
val = var_list[1]
n = val.split()  # split again to isolate number as the first element in the list
header_size = n[0].strip()  # number only (stored as a string, not an integer)
print('header_size', header_size)

#Run pts.exe
proc = subprocess.Popen('pts.exe header -full {}'.format(YUV_File), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
PTSOutput = proc.stdout.read()
output_str = PTSOutput.decode('utf-8') # decode "bytes" to "string" type 
lines = output_str.splitlines()
for line in lines:
    if 'active lines' in line:
        line_list = line.split(':')
        active_lines = line_list[1].strip()  # string without spaces, not an integer
    elif 'number of images' in line:
        line_list = line.split(':')
        number_of_images = line_list[1].strip() # string without spaces, not an integer
    elif 'active pixels' in line:
        line_list = line.split(':')
        active_pixels = line_list[1].strip() # string without spaces, not an integer

print('number of images', number_of_images)
print('active lines', active_lines)
print('active pixels', active_pixels)

#convert to integers
filesize_int = int(filesize)
number_of_images_int = int(number_of_images)
header_size_int = int(header_size)

#Figure out VideoAlignment for Drastic
# alignment = (filesize - header_size)/number_of_images
file_sieze_nohdr = filesize_int - header_size_int
print ('size without header', file_sieze_nohdr)
video_alignment = file_sieze_nohdr / number_of_images_int
video_alignment_int = int(video_alignment)
print ('video alignment is', video_alignment_int)

headername_file_name = ('{}.dhdr'.format(FILENAME))
print (headername_file_name)

LIBPATH = "{}\\{}".format(CWD, headername_file_name)
print (LIBPATH)

#delete header file if exists
if os.path.exists(LIBPATH):
    os.remove(LIBPATH)

#create new header
if not os.path.exists(LIBPATH):
    DHDR_Header = open("{}.dhdr".format(FILENAME), "w+")
    DHDR_Header.write("% Color Format\n")
    DHDR_Header.write("nv24\n")
    DHDR_Header.write("% Image Size (NbRows,NbCols)\n")
    DHDR_Header.write("{} {}\n".format(active_lines, active_pixels))
    DHDR_Header.write("% Video Offset\n")
    DHDR_Header.write("{}\n".format(header_size))
    DHDR_Header.write("% Header Offset\n")
    DHDR_Header.write("0\n")
    DHDR_Header.write("% Video Alignment\n")
    DHDR_Header.write("{}\n".format(video_alignment_int))
    DHDR_Header.write("% Number of Fields per Image\n")
    DHDR_Header.write("1\n")
    DHDR_Header.write("% Number of Image\n")
    DHDR_Header.write("{}\n".format(number_of_images))
    DHDR_Header.write("% Frame per second\n")
    DHDR_Header.write("50")
    DHDR_Header.close()

























