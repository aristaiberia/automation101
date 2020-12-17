# Basic postman examples
Basic cxamples about using Postman with EOS and with Cloudvision

EOS and CVP APIs are standard, as such, they can be used with the tool of your choice.

`ARISTA_CVP.postman_collection.json` and `ARISTA_SWITCH.postman_collection.json` are basic Postman example collections on using Postman to make both, EOS and CVP calls. This example EOS and API calls are the same used in the example2 with curl. Like in example2, authentication includes cookies and regular usr/pass passing.

A handy Postman feature is environments, by which you can define a set of variables that you later use in URLs, bodys, etc.

The image below shows the Postman environment used for the tests

![environ](https://github.com/aristaiberia/automation101/blob/main/day2_api/example3_postman/images/EOS.png)

EOS API example call that uses the variables previously defined in the Postman environment:

![eos](https://github.com/aristaiberia/automation101/blob/main/day2_api/example3_postman/images/EOS.png)

CVP API example call that uses the variables previously defined in the Postman environment:

![eos](https://github.com/aristaiberia/automation101/blob/main/day2_api/example3_postman/images/EOS.png)

Note here that all calls that leverage cookie based authentication should first call authentication to obtain teh cookie.
