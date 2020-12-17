#!/bin/bash

curl -s -k -X GET -b cookiefile --header 'Accept: application/json' \
'https://10.34.0.2/cvpservice/user/getUsers.do?startIndex=0&endIndex=100' 
