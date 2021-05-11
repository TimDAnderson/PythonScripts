# Header Creator for PFSPD video files

PFSPD (Philips File Standard for Pictoral Data) is a file format for the storage of uncompressed video sequences with arbitrary word width, color space and number of components.

The ClearView import application requires a header file for PFSPD imports.  This script creates a header file for the pfspd.yuv file.

The script takes in 1 additional argument, the yuv file

Usage:
```sh
Python CreateHeader.py YUVfile
```

