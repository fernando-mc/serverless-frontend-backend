import json


def hello(event, context):
    body = event['body']
    print(body)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello friends!"
        })
    }
    return response
