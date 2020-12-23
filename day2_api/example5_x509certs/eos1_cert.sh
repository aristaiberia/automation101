#!/bin/bash

curl --cacert ca.crt --cert client.crt --key client.key -s -X POST -H 'Content-Type: application/json' \
-d '{"jsonrpc": "2.0","method": "runCmds", "params": {"cmds": ["show version"], "version": 1}, "id": "miid1"}' \
https://@vlab31.lab.local/command-api
