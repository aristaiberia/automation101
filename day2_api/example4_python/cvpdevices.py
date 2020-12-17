#!/bin/python

import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

resp = requests.post(url="https://10.34.0.2/cvpservice/login/authenticate.do",
                     json={"userId":"cvpadmin", "password":"abc123"},
                     verify=False)
auth_cookie = resp.cookies

resp = requests.get(url="https://10.34.0.2/cvpservice/inventory/devices",
                    cookies=auth_cookie,
                    verify=False)

for switch in resp.json():
    hostname = switch.get("hostname")
    version = switch.get("version")
    sysid = switch.get("systemMacAddress")
    ip = switch.get("ipAddress")
    print("{} version is {} sysid id {} and ip is {}".\
          format(hostname, version, sysid, ip))
