#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import requests
from requests import Request, Session

import json
s = Session()

LOGIN = "http://services.tk/api/user/login"
GET_VARIABLE = "http://services.tk/api/system/get_variable/"
HEADERS = {'Accept': 'application/json'}
XToken = {'X-CSRF-Token':None }

req1 = Request(
        method='POST',
        url="http://services.tk/api/user/token",
        headers=HEADERS,
    )
prepped1 = s.prepare_request(req1)
resp1 = s.send(prepped1)
XCSRF = resp1.json()['token']  # xcsrf token

XToken['X-CSRF-Token'] = XCSRF
HEADERS.update(XToken)

data={
        'username': "admin",
        'password': 1,
    }

req2 = Request(
    method='POST',
    url=LOGIN,
    headers=HEADERS,
    data = data
)
prepped2 = s.prepare_request(req2)
resp2 = s.send(prepped2)

XCSRF = resp2.json()['token']
XToken['X-CSRF-Token'] = XCSRF
HEADERS.update(XToken)

req3 = Request(
        method='POST',
        url=GET_VARIABLE,
        headers=HEADERS,
        data= {'name':"site_name",
            'X-CSRF-Token': XCSRF
            }
    )
prepped3 = s.prepare_request(req3)
resp3 = s.send( prepped3 )
pprint ( resp3.json() )
