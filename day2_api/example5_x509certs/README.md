# Basic X509 cert authentication example
The following example is about using X509 certificates with EOS API

The example leverages [Hashicorp's Vault](http://https://www.vaultproject.io/) as a Certificate Authority

In particular the example does two independent things:

* In EOS switch:
  * Download and install CA certificate
  * Create keys
  * Create Certificate Signing Request (CSR) with Switch's public key and Switch's identity (hostname)
  * Send CSR to CA for signing
  * Retrieve signed Switch certificate from CA
  * Install keys and Switch certificate
  * Configure SSL profile using the Switch certificate and keys
  * Use SSL profile in Switch's EOS API configuration

* In Client device:
  * Download and install CA certificate
  * Create keys
  * Create Certificate Signing Request (CSR) with Client public key and Client identity (username)
  * Send CSR to CA for signing
  * Retrieve signed Client certificate from CA

Once this is done the Client can do API calls to the Switch beign each side (Client and Switch) authenticated by their corresponding certificates. Note that in this basic example we are just using the Root's X-Vault-Token for all Hashicorp's Vault API calls, however, way more advanced scenarios can be easily implemented for each party to obtain his X-Vault-Token for Vault CA API calls.

## In the EOS switch before execution

Before executing anything note that there are no SSL keys, no certificates (other than auto-signed default ones) and no SSL profile in the switch.

```
vlab31#dir sslkey:
Directory of sslkey:/

No files in directory

No space information available
vlab31#
vlab31#dir certificate:
Directory of certificate:/

       -rw-        2025           Dec 23 10:55  ARISTA_ROOT_CA.crt
       -rw-        2110           Dec 23 10:55  ARISTA_SIGNING_CA.crt

No space information available
vlab31#
vlab31#show running-config section api
management api http-commands
   no shutdown
vlab31#
vlab31#show running-config section ssl
vlab31#
```

Also note that in the Vault CA only one certificate is present (the one for the CA itself).

![cacert](https://github.com/aristaiberia/automation101/blob/main/day2_api/example5_x509certs/images/cacert.png)

## In the EOS switch after execution

Below you can see how `makeit_switch.py` is executed in the switch.

After execution the switch has installed CA certificate, Switch certificate, keys and configured SSL profile to be used in EOS API.

```
vlab31#
vlab31#
vlab31#bash

Arista Networks EOS shell

[admin@vlab31 ~]$ cd /mnt/flash               
[admin@vlab31 flash]$ ./makeit_switch.sh 
Copy completed successfully.
Copy completed successfully.
[admin@vlab31 flash]$ 
[admin@vlab31 flash]$ logout
vlab31#
vlab31#dir certificate:
Directory of certificate:/

       -rw-        2025           Dec 23 10:55  ARISTA_ROOT_CA.crt
       -rw-        2110           Dec 23 10:55  ARISTA_SIGNING_CA.crt
       -rw-        1325           Dec 23 11:22  ca.crt
       -rw-        1712           Dec 23 11:22  vlab31.crt

No space information available
vlab31#
vlab31#dir sslkey:
Directory of sslkey:/

       -rw-        3272           Dec 23 11:22  vlab31.key

No space information available
vlab31#
vlab31#show running-config section api
management api http-commands
   protocol https ssl profile SSL1
   no shutdown
vlab31#show running-config section ssl
username admin privilege 15 role network-admin secret sha512 $6$zg05nuSqCeznzinp$AAMXHmxyacZ0qFxKtsSTLnssLMD8zt29KvBg558jrgPULPfe9WrwfaU07EeWQrw22ud.h5S8e5cR0XwWwZyec0
!
management api http-commands
   protocol https ssl profile SSL1
   no shutdown
!
management security
   ssl profile SSL1
      certificate vlab31.crt key vlab31.key
      trust certificate ca.crt
vlab31#
```

And now you can see as well in the Vault CA that the switch cert has been generated

![switchcert](https://github.com/aristaiberia/automation101/blob/main/day2_api/example5_x509certs/images/switchcert.png)

Provided that you make your browser trust Vault CA it will trust the certificate that the switch uses for API as seen in the image below.

![browser](https://github.com/aristaiberia/automation101/blob/main/day2_api/example5_x509certs/images/browser.png)

## In the client

Similarly, the client runs a script `makeit_client.sh` to fetch CA certificate, generate keys, CSR, get Client certificate, etc.

Note that before executing the script there are only two certificates in the CA (CA's cert and Switch's cert).

![caswitch](https://github.com/aristaiberia/automation101/blob/main/day2_api/example5_x509certs/images/caswitch.png)

Now, after script execution the Client certificate has been signed by the CA as can be expected

![client](https://github.com/aristaiberia/automation101/blob/main/day2_api/example5_x509certs/images/client.png)

And now all crypto material is on the client and ready to be used

```
root@control /lab/api/vault # ls *crt *csr *key
ca.crt  client.crt  client.csr  client.key  clientjson.csr
```

API calls can now be done from the client for instance like in `eos1_cert.sh` that makes an EOS API in which:
* When receiving the API call, the switch authenticates the user making the API call with the Client certificate
* The client Authenticates the switch that is connectecting to with the Switch certificate

```
root@control /lab/api/vault # ./eos1_cert.sh | jq
{
  "jsonrpc": "2.0",
  "id": "miid1",
  "result": [
    {
      "memTotal": 1498328,
      "uptime": 4282.49,
      "modelName": "vEOS",
      "internalVersion": "4.24.0F-16270098.4240F",
      "mfgName": "",
      "serialNumber": "",
      "systemMacAddress": "50:54:00:00:31:31",
      "bootupTimestamp": 1608720882,
      "memFree": 749136,
      "version": "4.24.0F",
      "configMacAddress": "00:00:00:00:00:00",
      "isIntlVersion": false,
      "internalBuildId": "da8d6269-c25f-4a12-930b-c3c42c12c38a",
      "hardwareRevision": "",
      "hwMacAddress": "00:00:00:00:00:00",
      "architecture": "i686"
    }
  ]
}
```
