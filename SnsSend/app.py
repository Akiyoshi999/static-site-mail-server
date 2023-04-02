import json
import os
import boto3
import botocore


def sns_send_handler(event, context):
    sns = boto3.client('sns')
    try:
        formData = json.loads(event['body'])
        message = f"\n差出人 : {formData['name']}\n差出人メール : {formData['email']}\n本文 : {formData['message']}"
        response = sns.publish(
            TopicArn=os.environ['TOPIC_ARN'],
            Message=message,
            Subject='自分のHPからのお問い合わせ',
        )
    except botocore.exceptions.ClientError as error:
        print(error)
        raise error
    
    except Exception as error:
        print(error)
        raise error

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin" : "*",
        },
        'body': json.dumps({'MessageId' : response['MessageId']})
    }
