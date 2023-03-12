import json
import os

import pytest
from moto import mock_sns
import boto3

@mock_sns
class TestSnsSendGroup:

    def test_test_lambda_handler(self):
        from SnsSend import app
        apigw_event = {"body": "{\"name\": \"Akiyoshi\",\"email\": \"ubuntu@example.co.jp\",\"message\": \"Sender message\"}"}

        client_sns = boto3.client('sns',region_name='ap-northeast-1')
        res = client_sns.create_topic(Name='test-static-site-notice')
        topic_arn = res["TopicArn"]
        res_sub = client_sns.subscribe(
            TopicArn=topic_arn,Protocol='email',Endpoint='akiyoshi20038@yahoo.co.jp'
        )
        os.environ['TOPIC_ARN'] = res["TopicArn"]

        response = client_sns.publish(
            TopicArn=topic_arn,
            Message=json.dumps(apigw_event['body']),
            Subject='test'
        )
        print(os.environ['TOPIC_ARN'])
        print('END')

        # assert 1 == 0
        ret = app.lambda_handler(apigw_event, "")
        data = json.loads(ret["body"])

        assert ret["statusCode"] == 200
        assert "message" in ret["body"]
        assert data["message"] == "hello world"


# @pytest.fixture(scope="module",autouse=True)
# def client():
#     print('START')
#     os.environ['TOPIC_ARN'] = 'arn:aws:sns:ap-northeast-1:705427061380:static-site-notice'

# @pytest.fixture()
# def apigw_event():
#     """ Generates API GW Event"""

#     return {
#         "body": "{\"name\": \"Akiyoshi\",\"email\": \"ubuntu@example.co.jp\",\"message\": \"Sender message\"}",
#         # "body": '{ "test": "body"}',
#         "resource": "/{proxy+}",
#         "requestContext": {
#             "resourceId": "123456",
#             "apiId": "1234567890",
#             "resourcePath": "/{proxy+}",
#             "httpMethod": "POST",
#             "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
#             "accountId": "123456789012",
#             "identity": {
#                 "apiKey": "",
#                 "userArn": "",
#                 "cognitoAuthenticationType": "",
#                 "caller": "",
#                 "userAgent": "Custom User Agent String",
#                 "user": "",
#                 "cognitoIdentityPoolId": "",
#                 "cognitoIdentityId": "",
#                 "cognitoAuthenticationProvider": "",
#                 "sourceIp": "127.0.0.1",
#                 "accountId": "",
#             },
#             "stage": "prod",
#         },
#         "queryStringParameters": {"foo": "bar"},
#         "headers": {
#             "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
#             "Accept-Language": "en-US,en;q=0.8",
#             "CloudFront-Is-Desktop-Viewer": "true",
#             "CloudFront-Is-SmartTV-Viewer": "false",
#             "CloudFront-Is-Mobile-Viewer": "false",
#             "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
#             "CloudFront-Viewer-Country": "US",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#             "Upgrade-Insecure-Requests": "1",
#             "X-Forwarded-Port": "443",
#             "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
#             "X-Forwarded-Proto": "https",
#             "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
#             "CloudFront-Is-Tablet-Viewer": "false",
#             "Cache-Control": "max-age=0",
#             "User-Agent": "Custom User Agent String",
#             "CloudFront-Forwarded-Proto": "https",
#             "Accept-Encoding": "gzip, deflate, sdch",
#         },
#         "pathParameters": {"proxy": "/examplepath"},
#         "httpMethod": "POST",
#         "stageVariables": {"baz": "qux"},
#         "path": "/examplepath",
#     }

