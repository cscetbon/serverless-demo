from __future__ import print_function

import json
import logging
import os
import boto3
from boto3.dynamodb.conditions import Key

log = logging.getLogger()
log.setLevel(logging.DEBUG)
dynamodb = boto3.resource('dynamodb')
images = dynamodb.Table('-'.join(['EtlDemoImages',os.environ['SERVERLESS_STAGE']]))

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    format = event['params']['format']
    response = images.query(KeyConditionExpression=Key('format').eq(format))
    return len(response['Items'])
