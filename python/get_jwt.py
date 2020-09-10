#! /usr/bin/env python
# coding: utf-8

import pprint
import datetime
import sys
import paypayopa

if __name__ == "__main__":

  API_KEY = ""
  API_SECRET = ""
  MERCHANT_ID = ""

  #Set True for Production Environment. By Default this is set False for Sandbox Environment.
  client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
  client.set_assume_merchant(MERCHANT_ID)

  args = sys.argv
  jwt = args[1]

  d_jwt = client.decode_jwt(API_SECRET, jwt)

  pprint.pprint(d_jwt)

