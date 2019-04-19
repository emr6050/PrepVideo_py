import sys
import os
import logging
from datetime import time
import time
import boto3
from botocore.exceptions import ClientError

# when script is run, it must be accompanied with an input file
if len(sys.argv) > 2 or len(sys.argv) < 2:
    exit()

filename = str(sys.argv[1])  # = 'out/trimmed.mp4'
ts = time.time()
objectname = 'uploadFile_' + str(int(ts)) + '.mp4'

# TODO: come up with a better generic file name for the uploads
# TODO: create a json-string as metadata for describing the uploaded file

# connecting to AWS
s3_client = boto3.client('s3')
try:
    response = s3_client.upload_file(
        filename, os.environ['VOD_SRC_BUCKET'], objectname)
except ClientError as e:
    logging.error(e)
    print(e)

print('--finished--')
