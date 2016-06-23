from __future__ import print_function

import json
import logging
import boto3
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)
sns = boto3.client('sns')
TOPIC_NAME = '-'.join(['EtlDemoImages',os.environ['SERVERLESS_STAGE']])
TOPIC_ARN = sns.create_topic(Name=TOPIC_NAME)['TopicArn']

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    kname, kcontent = 'name', 'content'
    name = event['body'][kname]
    content = event['body'][kcontent]
    message = {kname: name, kcontent: content}
    sns.publish(TargetArn=TOPIC_ARN, Message=json.dumps(message))
    return
