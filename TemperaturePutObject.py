import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    bucket = 'aws-simplified-temperature'
    temperatureToUpload['device'] = event['device']
    temperatureToUpload['temperature'] = event['temperature']
    fileName = 'device_temperature.json'
    uploadByteStream = bytes(json.dumps(temperatureToUpload).encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    print('Put Complete')
