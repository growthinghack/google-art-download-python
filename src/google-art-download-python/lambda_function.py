import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')

def lambda_handler(event, context):
    logger.info(event)
    output = {'purpose': 'Hello World-1'}
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(output)
    }
