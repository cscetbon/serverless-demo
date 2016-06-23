from __future__ import print_function

import json
import logging
import boto3
import sys, os
from os.path import split

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "vendored"))

import magic
from pynamodb.attributes import BinaryAttribute

log = logging.getLogger()
log.setLevel(logging.DEBUG)
dynamodb = boto3.resource('dynamodb')
images = dynamodb.Table('-'.join(['EtlDemoImages',os.environ['SERVERLESS_STAGE']]))

def handler(event, context):
    content = BinaryAttribute(null=True)
    log.debug("Received event {}".format(json.dumps(event)))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    name = message['name']
    content = message['content']
    mime_type = magic.from_buffer(BinaryAttribute().deserialize(content), mime=True)
    tname, stname = split(mime_type)
    if tname != 'image':
      raise TypeError("Only images are supported")
    images.put_item(Item={'name': name, 
                          'content': content, 
                          'format': stname})
    return
