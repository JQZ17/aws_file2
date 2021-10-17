import json

def lambda_handler(event, context):
    # TODO implement
    message_text = "Device {0} reports a temperature of {1}.".format(
            str(event['device_id']),
            str(event['temperature'])
        )
    print(message_text)
    
    return {
        'statusCode': 200,
        'body': json.dumps(message_text)
    }
