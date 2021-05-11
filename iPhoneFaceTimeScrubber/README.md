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
