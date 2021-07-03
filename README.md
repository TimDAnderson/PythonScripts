# PythonScripts
Online backup of various Python scripts written by Tim Anderson.  All ReadMe's listed below:

# DVD Tester

## Sends IR commands to turn on and configure a DVD Player, then triggers a ClearView recording

A device called IRTrans is used to control / configure a DVD player.  
- The DVD player must have an external thumbdrive connected to it wtih MPEG .ts files
- The IRTrans client must be pre-configured on the local machine

Usage:
```sh
$ Python DVDtester.py
```

# Free Run Record

## Simple script that does the following:
- Gets current ClearView Library
- Sets up recording on input 1, board 1
- Begins free run record with sequence name set to current date / time



Usage:
```sh
$ Python FreeRunRecordStart.py
```

# Header Creator for PFSPD video files

PFSPD (Philips File Standard for Pictoral Data) is a file format for the storage of uncompressed video sequences with arbitrary word width, color space and number of components.

The ClearView import application requires a header file for PFSPD imports.  This script creates a header file for the pfspd.yuv file.

The script takes in 1 additional argument, the yuv file

Usage:
```sh
Python CreateHeader.py YUVfile
```

# Apple iPhone FaceTime Scrubber

## Used for testing FaceTime on iPhones with network impairments.  Scrubs through iPhone FaceTime recordings and removes the static frames that say "Poor Network Conditions" since these frames do not exist in the source.  

## Once the frames are removed objective video metrics can run on the remaining video

The script requires four additional arguments:
- ClearView Library name
- Recording
- Poor Connection reference frame
- PSNR threshold used for comparisson

Usage:
```sh
Python RemovePoorConnectionFrames.py CVLibrary Recording RefFrame PSNRThreshold
```

# RTMonitor Error Scrubber

## Scans RTMonitor error log directory looking for false positives caused by a frame slip

The script takes in two arguments.  The path or the original error directory and the path to the "scrubbed" directory.  The script will migrate false positives due to frame slips from the orig directory to the scrubbed directory.  

Usage:
```sh
$ Python RTMonitorErrorScrubber.py RTMLogDirectory RTMScrubbedDirectory
```

# VCLabsSorter

## Backend worker for videoclaritylabs.com.  As job.json files begin to download from DropBox this script will begin to process the video files.  Information is probed from the video files and they get queued up for VQ analysis.

This script takes in 1 argument, a job.json file

Usage:
```sh
Python ReadJsonWithSort.py job.json
```

# .bat script repo

misc. Windows batch scripts
