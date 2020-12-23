#!/bin/bash

curl -s -k -X POST -H 'Content-Type: application/json' \
-d '{"jsonrpc": "2.0","method": "runCmds", "params": {"cmds": ["show version"], "version": 1}, "id": "miid1"}' \
https://admin:abc123@vlab31.lab.local/command-api
