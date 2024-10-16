import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from CA-CENTRAL-1 with github actions and dynatrace!')
    }
