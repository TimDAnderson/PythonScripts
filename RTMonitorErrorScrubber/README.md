# RTMonitor Error Scrubber

## Scans RTMonitor error log directory looking for false positives caused by a frame slip

The script takes in two arguments.  The path or the original error directory and the path to the "scrubbed" directory.  The script will migrate false positives due to frame slips from the orig directory to the scrubbed directory.  

Usage:
```sh
$ Python RTMonitorErrorScrubber.py RTMLogDirectory RTMScrubbedDirectory
```

