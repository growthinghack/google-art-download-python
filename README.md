[![Build Status](https://travis-ci.org/nicor88/aws-python-lambdas.svg?branch=master)](https://travis-ci.org/nicor88/aws-python-lambdas)

# aws-python-lambdas
Collection of python lambda function

## Setup Conda Env
<pre># create env
#conda create --name aws-python-lambdas python=3.6.2
python3 -m venv venv
# activate env
source venv/bin/activate
pip install boto3
pip install pytest
# install libs from the requirements of each single lambda
for i in src/*/; do pip install -r $i"requirements.txt"; done
</pre>




##  Development
```
$ python-lambda-local -f lambda_handler src/google-art-download-python/lambda_function.py mockEvent/googleArtUrlZoom.json -t 20
```


## Zip Deployment
```
$ lambda-google-art-downloader-python wahengchang$ aws lambda update-function-code --function-name google-art-download-python --zip-file fileb://function.zip
```