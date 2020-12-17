#!/bin/bash

curl -s -k -X POST -H 'Content-Type: application/json' -c cookiefile \
-d '{"userId":"cvpadmin","password":"abc123"}' \
https://10.34.0.2/cvpservice/login/authenticate.do
