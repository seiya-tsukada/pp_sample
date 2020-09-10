#! /usr/bin/env python
# coding: utf-8

import pprint
import datetime
import sys
import paypayopa

def payment(client, uaid):

  now = datetime.datetime.now()
  current_time =  now.strftime('%Y%m%d%H%M%S')
  print(current_time)

  request = {
    "merchantPaymentId": "tsuk-pay-{}".format(current_time),
    "userAuthorizationId": uaid,
    "orderDescription":"tsuk shop",
    "amount": {
      "amount": 100,
      "currency": "JPY"
    }
  }

  pprint.pprint(client)
  # Calling the method to create a payment
  response = client.payment.create(request)

  # Printing if the method call was SUCCESS, this does not mean the payment was a success
  pprint.pprint(response)

if __name__ == "__main__":

  API_KEY = ""
  API_SECRET = ""
  MERCHANT_ID = ""

  #Set True for Production Environment. By Default this is set False for Sandbox Environment.
  client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
  client.set_assume_merchant(MERCHANT_ID)

  args = sys.argv
  uaid = args[1]

  payment(client, uaid)
