# VCLabsSorter

## Backend worker for videoclaritylabs.com.  As job.json files begin to download from DropBox this script will begin to process the video files.  Information is probed from the video files and they get queued up for VQ analysis.

This script takes in 1 argument, a job.json file

Usage:
```sh
Python ReadJsonWithSort.py job.json
```