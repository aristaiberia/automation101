#!/bin/bash

# Fetch CA cert
curl -s -o ca.crt http://10.34.0.253:8200/v1/pki/ca/pem

# Generate client keys (client.key) and CSR (client.csr)
openssl req -newkey rsa:4096 -nodes -keyout client.key -out client.csr -subj '/CN=admin/O=aristalab/C=ES' > /dev/null 2>&1

# Jsonize CSR
CSR=$(cat client.csr | sed -e ':a;N;$!ba;s/\n/\\n/g')
CSRDATA='{"csr": "'$CSR'"}'
echo $CSRDATA > clientjson.csr

# Send CSR to CA for signing
RESP=$(curl -s --request POST --header "X-Vault-Token: s.yWEY35xtfT5rWsWK4TP1hEQK" \
--data @clientjson.csr \
http://10.34.0.253:8200/v1/pki/sign/aristalab)
echo -e $(echo $RESP| jq .data.certificate | tr -d '"') > client.crt
