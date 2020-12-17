#!/bin/bash

curl -s -k -X POST -H 'Content-Type: application/json' \
-d '{"username": "admin", "password": "abc123"}' -c cookiefile \
https://10.34.0.31/login
