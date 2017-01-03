import os
import requests

HOOK_URL = os.environ['SLACK_WEBHOOK_URL']

def lambda_handler(event, context):
    data = {
        "text": "event=%s" % event
    }
    requests.post(HOOK_URL, json=data)
