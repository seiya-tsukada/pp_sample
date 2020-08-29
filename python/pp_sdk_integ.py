#! /usr/bin/env python
# coding: utf-8

import pprint
import datetime
import paypayopa

def createCode(client):

  now = datetime.datetime.now()
  current_time =  now.strftime('%Y%m%d%H%M%S')
  print(current_time)

  request = {
    "merchantPaymentId": "tsuk-qr-{}".format(current_time),
    "codeType": "ORDER_QR",
    "redirectUrl":"https://paypay.ne.jp",
    "redirectType":"WEB_LINK",
    "orderDescription":"tsuk shop",
    "orderItems": [
        {
            "name": "tsuk item",
            "quantity": 1,
            "unitPrice": {
                "amount": 100,
                "currency": "JPY"
            }
        }
    ],
    "amount": {
      "amount": 100,
      "currency": "JPY"
    }
  }

  # Calling the method to create a qr code
  response = client.code.create_qr_code(request)

  # Printing if the method call was SUCCESS
  pprint.pprint(response)


if __name__ == "__main__":

  API_KEY = ""
  API_SECRET = ""
  MERCHANT_ID = ""

  #Set True for Production Environment. By Default this is set False for Sandbox Environment.
  client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
  client.set_assume_merchant(MERCHANT_ID)

  createCode(client)