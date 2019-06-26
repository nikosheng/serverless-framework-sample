import json

def say(event, context):
    body = {
        "message": "Share API Gateway Successfully!!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
