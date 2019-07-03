import logging
import json
import asyncio
import time
from tile_fetch import load_tiles
from upload import upload_file

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')

def lambda_handler(event, context):
    logger.info('-=-=-=-=-=-= event -=-=-=-=-=-=')
    logger.info(event)
    logger.info('-=-=-=-=-=-= queryStringParameters -=-=-=-=-=-=')
    logger.info(event["queryStringParameters"])
    ts = int(str(time.time()).replace('.', ''))

    url = event["queryStringParameters"]["url"]
    zoom = event["queryStringParameters"]["zoom"] or 4
    outfile = '{}.jpg'.format(ts)

    logger.info("url: "+ url)
    logger.info("zoom: {}".format(zoom))
    logger.info("outfile: "+ outfile)

    coro = load_tiles(url, zoom, outfile)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro)

    logger.info("Going to upload S3: ")
    downloadUrl = upload_file(outfile)
    logger.info("Uploaded to S3: "+ downloadUrl)
    output = {'url': downloadUrl}

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(output)
    }
