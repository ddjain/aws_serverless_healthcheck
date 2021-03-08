import json
import os
import requests

def sendSlackMessage(payload,event):
    slack_url = str(event.get("slack_url"))
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", slack_url, headers=headers, data=payload)
    print(response.text)

def lambda_handler(event, context):
    url = str(event.get("url"))
    response_code = str(event.get("code"))
    print("Sending request to "+url+". expecting response_code as "+response_code)
    r = requests.get(url)
    pload={ "text": "Healthcheck-bot", "pretext": "Service Is down", "color": "#36a64f", "fields": [ { "title": "Service Name :" + event.get("serviceName"), "value": "Details: "+str(r.content), "short": True } ] }
    if  str(r.status_code) != response_code:
        sendSlackMessage(json.dumps(pload), event)
        raise Exception("{url} is down".format(url=url))
    return {
        'statusCode': response_code,
        'body': str(r.content)
    }
