#! /bin/bash

$FILE_PATH='$PWD/handler/__init__.py'
$HANDLER='test.lambda_handler'

kubeless function deploy FUNCTION_NAME --runtime python3.6
                                        -from-file $FILE_PATH
                                        --handler $HANDLER
