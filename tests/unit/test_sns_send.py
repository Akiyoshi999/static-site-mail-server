import json
import os

from SnsSend import app
from moto import mock_sns
import boto3
import pytest
import botocore

@mock_sns
def test_sns_send_success(apigw_event_success):
    client_sns = boto3.client('sns',region_name='ap-northeast-1')
    res = client_sns.create_topic(Name='test-static-site-notice')
    os.environ['TOPIC_ARN'] = res["TopicArn"]

    ret = app.sns_send_handler(apigw_event_success, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "MessageId" in ret["body"]
    assert type(data["MessageId"]) == str

def test_sns_send_no_sns_endpoint(apigw_event_success):
    with pytest.raises(botocore.exceptions.ClientError):
        os.environ['TOPIC_ARN'] = 'dummy'
        app.sns_send_handler(apigw_event_success, "")

@mock_sns
def test_sns_send_no_body(apigw_event_bad_no_body):
    with pytest.raises(KeyError):
        client_sns = boto3.client('sns',region_name='ap-northeast-1')
        res = client_sns.create_topic(Name='test-static-site-notice')
        os.environ['TOPIC_ARN'] = res["TopicArn"]

        ret = app.sns_send_handler(apigw_event_bad_no_body, "")

@mock_sns
def test_sns_send_no_name(apigw_event_bad_no_name):
    with pytest.raises(KeyError):
        client_sns = boto3.client('sns',region_name='ap-northeast-1')
        res = client_sns.create_topic(Name='test-static-site-notice')
        os.environ['TOPIC_ARN'] = res["TopicArn"]

        ret = app.sns_send_handler(apigw_event_bad_no_name, "")

@mock_sns
def test_sns_send_no_email(apigw_event_bad_no_email):
    with pytest.raises(KeyError):
        client_sns = boto3.client('sns',region_name='ap-northeast-1')
        res = client_sns.create_topic(Name='test-static-site-notice')
        os.environ['TOPIC_ARN'] = res["TopicArn"]

        ret = app.sns_send_handler(apigw_event_bad_no_email, "")

@mock_sns
def test_sns_send_no_message(apigw_event_bad_no_message):
    with pytest.raises(KeyError):
        client_sns = boto3.client('sns',region_name='ap-northeast-1')
        res = client_sns.create_topic(Name='test-static-site-notice')
        os.environ['TOPIC_ARN'] = res["TopicArn"]

        ret = app.sns_send_handler(apigw_event_bad_no_message, "")