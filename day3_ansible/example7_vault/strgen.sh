#!/bin/bash

echo -n "secret name:"
read SN
echo -n "what to encrypt:"
read -s WTE
echo
echo -n $WTE | ansible-vault encrypt_string --stdin-name $SN
unset SN
unset WTE
