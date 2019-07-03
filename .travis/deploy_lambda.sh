LAMBDA_PATH=$1
SRC=src/
LAMBDA_NAME=${LAMBDA_PATH#${SRC}}
LAMBDA_NAME=${LAMBDA_NAME%/}

echo Deploy $LAMBDA_NAME inside $LAMBDA_PATH
pip3 install -r $LAMBDA_PATH"requirements.txt" -t $LAMBDA_PATH --upgrade

cd $LAMBDA_PATH
echo "[INFO] ziping: $LAMBDA_NAME"
zip -r $LAMBDA_NAME.zip .
echo "[INFO] deploy to aws: $LAMBDA_NAME"
aws lambda update-function-code --function-name $LAMBDA_NAME --zip-file fileb://$LAMBDA_NAME.zip
