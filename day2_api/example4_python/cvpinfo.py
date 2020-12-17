#!/bin/python

import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

resp = requests.post(url="https://10.34.0.2/cvpservice/login/authenticate.do",
                     json={"userId":"cvpadmin", "password":"abc123"},
                     verify=False)
auth_cookie = resp.cookies

resp = requests.get(url="https://10.34.0.2/cvpservice/cvpInfo/getCvpInfo.do",
                    cookies=auth_cookie,
                    verify=False)
version = resp.json()["version"]

print("CVP version is {}".format(version))
