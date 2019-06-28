LAMBDA_PATH=$1
SRC=src/
LAMBDA_NAME=${LAMBDA_PATH#${SRC}}
LAMBDA_NAME=${LAMBDA_NAME%/}

echo Building $LAMBDA_NAME inside $LAMBDA_PATH

pip install -r $LAMBDA_PATH"requirements.txt" -t $LAMBDA_PATH --upgrade