import json

import pytest
from moto import mock_ssm
import requests_mock
import boto3
import botocore
from LineNotice import app


@pytest.fixture(scope='function')
def request_mock_success():
    with requests_mock.Mocker() as m:
        yield m.post('https://notify-api.line.me/api/notify',
                     text='{"status":200,"message":"ok"}', status_code=200)


@pytest.fixture(scope='function')
def request_mock_invalid_token():
    with requests_mock.Mocker() as m:
        yield m.post('https://notify-api.line.me/api/notify',
                     text='{"status":401,"message":"nvalid access token"}', status_code=401)


@mock_ssm
def test_line_notice_success(sns_event_success, request_mock_success):
    """
    LINEの通知が成功した場合
    """
    client_ssm = boto3.client('ssm', region_name='ap-northeast-1')
    client_ssm.put_parameter(
        Name='LineNotice-WebhookURL',
        Value='https://notify-api.line.me/api/notify',
        Type='SecureString',
    )
    client_ssm.put_parameter(
        Name='LineNotice-Token',
        Value='dummyToken',
        Type='SecureString',
    )

    res = app.line_notice_handler(sns_event_success, "")
    body = json.loads(res['body'])

    assert res["statusCode"] == 200
    assert "message" in res["body"]
    assert body['message'] == 'ok'


@mock_ssm
def test_line_notice_no_ssm(sns_event_success, request_mock_success):
    """
    SSMにパラメータがない場合
    """
    with pytest.raises(botocore.exceptions.ClientError):
        client_ssm = boto3.client('ssm', region_name='ap-northeast-1')
        client_ssm.put_parameter(
            Name='LineNotice-Token',
            Value='dummyToken',
            Type='SecureString',
        )

        app.line_notice_handler(sns_event_success, "")


@mock_ssm
def test_line_notice_invalid_token(sns_event_success, request_mock_invalid_token):
    """
    アクセストークンが無効の場合
    """
    client_ssm = boto3.client('ssm', region_name='ap-northeast-1')
    client_ssm.put_parameter(
        Name='LineNotice-WebhookURL',
        Value='https://notify-api.line.me/api/notify',
        Type='SecureString',
    )
    client_ssm.put_parameter(
        Name='LineNotice-Token',
        Value='dummyToken',
        Type='SecureString',
    )

    res = app.line_notice_handler(sns_event_success, "")
    body = json.loads(res['body'])

    assert res["statusCode"] == 401
    assert "message" in res["body"]
    assert body['message'] == 'nvalid access token'

