#!/bin/bash

curl -s -b cookiefile -k -X POST -H 'Content-Type: application/json' \
-d '{"jsonrpc": "2.0","method": "runCmds", "params": {"cmds": ["show version"], "version": 1}, "id": "miid1"}' \
https://10.34.0.31/command-api
