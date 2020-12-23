#!/bin/bash

# Fetch CA cert
curl -s -o /mnt/flash/ca.crt http://10.34.0.253:8200/v1/pki/ca/pem

# Generate switch keys
HOSTNAME=$(hostname)
DOMAIN=lab.local
FastCli -p15 -c "security pki key generate rsa 4096 $HOSTNAME.key"

# Generate CSR
FastCli -p15 -c "security pki certificate generate signing-request key $HOSTNAME.key parameters common-name $HOSTNAME.$DOMAIN subject-alternative-name dns $HOSTNAME.$DOMAIN" > /mnt/flash/$HOSTNAME.csr

# Jsonize CSR
CSR=$(cat /mnt/flash/$HOSTNAME.csr | sed -e ':a;N;$!ba;s/\n/\\n/g')
CSRDATA='{"csr": "'$CSR'"}'
echo $CSRDATA > "$HOSTNAME"json.csr

# Send CSR to CA for signing
RESP=$(curl -s --request POST --header "X-Vault-Token: s.yWEY35xtfT5rWsWK4TP1hEQK" \
--data @/mnt/flash/"$HOSTNAME"json.csr \
http://10.34.0.253:8200/v1/pki/sign/aristalab)
echo $(echo $RESP) | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['certificate'])" > /mnt/flash/$HOSTNAME.crt

# Install certificates in switch cert store
FastCli -p15 -c "copy flash:$HOSTNAME.crt certificate:"
FastCli -p15 -c "copy flash:ca.crt certificate:"

# Configure SSL profile
cat <<EOF | FastCli -p15
configure
management security
ssl profile SSL1
certificate $HOSTNAME.crt key $HOSTNAME.key
trust certificate ca.crt
management api http-commands
protocol https ssl profile SSL1
no shutdown
EOF
