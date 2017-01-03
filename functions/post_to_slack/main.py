import requests

HOOK_URL = os.environ['slackWebhookUrl']

def lambda_handler(event, context):
    data = {
        "text": "hello"
    }
    requests.post(HOOK_URL, json=data)
