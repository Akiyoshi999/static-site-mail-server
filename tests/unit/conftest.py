import pytest

@pytest.fixture()
def apigw_event_success():
    """ Generates API GW Event"""

    return {
        "body": "{\"name\": \"Akiyoshi\",\"email\": \"ubuntu@example.co.jp\",\"message\": \"Sender message\"}",
        # "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


@pytest.fixture()
def apigw_event_bad_no_body():
    """ Generates API GW Event"""

    return {
        "queryStringParameters": {"foo": "bar"},
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "path": "/examplepath",
    }

@pytest.fixture()
def apigw_event_bad_no_name():
    return {
        "body": "{\"email\": \"ubuntu@example.co.jp\",\"message\": \"Sender message\"}",
    }

@pytest.fixture()
def apigw_event_bad_no_email():
    return {
        "body": "{\"name\": \"Akiyoshi\",\"message\": \"Sender message\"}",
    }

@pytest.fixture()
def apigw_event_bad_no_message():
    return {
        "body": "{\"name\": \"Akiyoshi\",\"email\": \"ubuntu@example.co.jp\"}",
    }

@pytest.fixture()
def sns_event_success():
    return {
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:ap-northeast-1:705427061380:static-site-notice:a0547382-b028-47d9-b546-bd68cc66455a",
      "Sns": {
        "Type": "Notification",
        "MessageId": "37c2b830-f9f7-5e8c-9aaf-e4b7a0d383be",
        "TopicArn": "arn:aws:sns:ap-northeast-1:705427061380:static-site-notice",
        "Subject": "自分のHPからのお問い合わせ",
        "Message": "\n差出人 : Akiyoshi\n差出人メール : ubuntu@example.co.jp\n本文 : Sender message",
        "Timestamp": "2023-03-12T04:36:52.649Z",
        "SignatureVersion": "1",
        "Signature": "ItdF2OelXSqPsbewsA8mKjGep7/U2WIcJ+OURX28h7TQmNcZtQzBLhXIRYXMDlIUYeRIWfPF+Ch/WrS1xkeX7L0lU2c/RN5XDScVZt9/gHl2zNHqXxeMb9t79AgbDEBmad0vvMtmVsaXtftvSCkEg7r2ObcppK6n4D5tA8h+jU9OLdirQ1Mc6mi3jU69DNB/ZQNRDRMxY3W1fqlCj1Xp2PnqmGG7FwgvUzlsyewk/ZdYULv+ftewSNitDizuzfqHWoK/sSsAu2wJfCWUTBcgkLxpxdwpi4x49nKyE0YISwMieLgC7KdGREZa2/2xyRH8gx7ETBnhUNlcE6Kegtq0ng==",
        "SigningCertUrl": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
        "UnsubscribeUrl": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:705427061380:static-site-notice:a0547382-b028-47d9-b546-bd68cc66455a",
        "MessageAttributes": {}
      }
    }
  ]
}