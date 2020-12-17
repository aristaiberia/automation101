#!/usr/bin/python
from cvprac.cvp_client import CvpClient
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

c = CvpClient()
c.connect(["10.34.0.2"], "cvpadmin", "abc123")
r = c.api.get_cvp_info()
version=r["version"]
print("CVP version is {}".format(version))
