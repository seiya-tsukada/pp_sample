#! /usr/bin/env python
# coding: utf-8

import pprint
import datetime
import paypayopa

def payment(client):

  now = datetime.datetime.now()
  current_time =  now.strftime('%Y%m%d%H%M%S')
  print(current_time)

  request = {
    "merchantPaymentId": "tsuk-pay-{}".format(current_time),
    "userAuthorizationId": "0a98d27a-f1b3-42c8-b03a-62b61af91d5a",
    "orderDescription":"tsuk shop",
    "amount": {
      "amount": 1000,
      "currency": "JPY"
    }
  }

  pprint.pprint(client)
  # Calling the method to create a payment
  response = client.payment.create(request)

  # Printing if the method call was SUCCESS, this does not mean the payment was a success
  pprint.pprint(response)

if __name__ == "__main__":

  API_KEY = "m_HF1GR6qFFQ_r3Mj"
  API_SECRET = "9Oc1dHRcuhQb7IOjDa1ssvc8hVXUXJtF/6KtcJHZ"
  MERCHANT_ID = "238319566440579072"

  #Set True for Production Environment. By Default this is set False for Sandbox Environment.
  client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
  client.set_assume_merchant(MERCHANT_ID)

  payment(client)
